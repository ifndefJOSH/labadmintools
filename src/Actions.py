import os

from PyQt5 import *
from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore

from LabList import LabComputer, Lab
from ui.FileCopyWidget import CommandWidget, DataLineWidget, FileCopyWidget, ShellScriptWidget

import fabric

class Logs:
	def __init__(self, stdout : str, stderr : str) -> None:
		self.stdout = stdout
		self.stderr = stderr

	def append(self, stdout : str, stderr : str) -> None:
		self.stdout += f"\n{stdout}"
		self.stderr += f"\n{stderr}"

	def __str__(self) -> str:
		return f"STDOUT:\n{self.stdout}\nSTDERR:\n{self.stderr}"

class Action:
	# Types of actions
	COMMAND=0
	FILE_COPY=1
	SHELL_SCRIPT=2

	# Statuses for actions
	NOT_STARTED=0
	RUNNING=1
	SUCCEEDED=2
	FAILED=3

	@staticmethod
	def statusToString(status : int):
		return ["Not Started", "Running", "Succeeded", "Failed"][status]

	def __init__(self, actionType : int, data : str, comment : str, needsSudo : bool) -> None:
		self.__actionType = actionType
		self.__data = data
		self.__comment = comment
		self.__needsSudo = needsSudo
		self.__executed = False
		self.__logs = None
		self.__status = Action.NOT_STARTED

	def validate(self) -> tuple:
		'''
	Returns a tuple as to whether the Action is valid or not, and an error message
		'''
		if self.__actionType == Action.COMMAND:
			return (True, None)
		elif self.__actionType == Action.FILE_COPY:
			toFromPath = self.__data.split(" ")
			if len(toFromPath) != 2:
				print(toFromPath, self.__data)
				return (False, "Requires to and from location")
			elif not os.path.isfile(toFromPath[0]):
				return (False, f"File to copy '{toFromPath[0]}' does not exist")
			return (True, None)
		elif self.__actionType == Action.SHELL_SCRIPT:
			exists = os.path.isfile(self.__data)
			if not exists:
				return (False, f"Script '{self.__data}' does not exist")
			return (True, None)
		else:
			return (False, "Action Type is Invalid")

	def status(self) -> int:
		return self.__status

	def execute(self, connectionGroup : fabric.group.ThreadingGroup) -> None:
		valid, msg = self.validate()
		if not valid:
			print(f"Action cannot be executed! Reason {msg}")
			return
		if self.__executed:
			print(f"Warning: this action was already executed")

		# Run the bad boi
		result : fabric.Result = None
		self.__status = Action.RUNNING
		if self.__actionType == Action.COMMAND:
			print(f"Running command `{self.__data}` on group")
			# privilege escalation
			if self.__needsSudo:
				result = connectionGroup.sudo(self.__data, hide=True)
			else:
				result = connectionGroup.run(self.__data, hide=True)
			self.__logs = Logs(result.stdout, result.stderr)
		elif self.__actionType == Action.FILE_COPY:
			# TODO: do we need any form of sudo?
			source, destination = [s.strip() for s in self.__data.split(" ")]
			print(f"Copying file `{source}` to group at path {destination}")
			result = connectionGroup.put(source, remote=destination)
		elif self.__actionType == Action.SHELL_SCRIPT:
			SHELL_PATH="/tmp/tempShellScriptLabAdmin"
			# First, copy the file to /tmp/tempShellScript
			print(f"Attempting to copy shell script `{self.__data}` to group...", end="")
			result = connectionGroup.put(self.__data, remote=SHELL_PATH)
			if result.ok:
				print("ok. Now running script.")
				# second, execute the file, overwriting 'result' variable
				if self.__needsSudo:
					result = connectionGroup.sudo(SHELL_PATH)
				else:
					result = connectionGroup.run(SHELL_PATH)
				self.__logs = Logs(result.stdout, result.stderr)
				# delete the file
				connectionGroup.run(f"rm {SHELL_PATH}")

		self.__status = Action.SUCCEEDED if result.ok else Action.FAILED
		print(f"{'Succeeded' if result.ok else 'Failed'}")
		self.__executed = True

	def asRow(self) -> str:
		return f"{self.__actionType},{self.__data},{self.__comment},{self.__needsSudo}\n"

	def getLogs(self, stderr : bool = True, stdout : bool = True) -> str:
		assert(stderr or stdout)
		if self.__logs is None:
			return "[No logs. Perhaps action hasn't been run?]"
		elif not stderr:
			return self.__logs.stdout
		elif not stdout:
			return self.__logs.stderr
		else:
			return str(self.__logs)

class ActionRow:
	DATA_COLUMN_IDX=2
	def __init__(self
			  , idx : int
			  , actionTypeComboBox : QComboBox
			  , dataLine : DataLineWidget
			  , commentLine : QLineEdit
			  , needsSudoCheckBox : QCheckBox
			  , selectedCheckBox : QCheckBox
			  , parent : QTableWidget) -> None:
		self.__idx = idx
		self.__actionTypeComboBox = actionTypeComboBox
		self.__dataLine = dataLine
		self.__commentLine = commentLine
		self.__needsSudoCheckBox = needsSudoCheckBox
		self.__action = None
		self.__selectedCheckBox = selectedCheckBox
		self.__parent = parent
		actionTypeComboBox.currentIndexChanged.connect(self.changeDataLineWidget)

	def createAction(self) -> tuple:
		action = Action(
				self.__actionTypeComboBox.currentIndex()
				, self.__dataLine.toData()
				, self.__commentLine.text()
				, self.__needsSudoCheckBox.isChecked())
		valid, msg = action.validate()
		if valid:
			self.__action = action
		return valid, msg

	def executeAction(self, connectionGroup : fabric.group.ThreadingGroup) -> bool:
		if self.__action is None:
			return False
		self.__action.execute(connectionGroup)
		return True

	def status(self) -> int:
		if self.__action is None:
			return Action.NOT_STARTED
		else:
			return self.__action.status()

	def delete(self):
		self.__parent.removeRow(self.__idx)

	def select(self, selected : bool = True):
		self.__selectedCheckBox.setChecked(selected)

	def toggleSelection(self):
		self.__selectedCheckBox.setChecked(not self.selected())

	def selected(self) -> bool:
		return self.__selectedCheckBox.isChecked()

	def asRow(self) -> str:
		valid, msg = self.createAction()
		if not valid:
			raise Exception(f"Action {self.__idx} not valid: {msg}")
		# assertion should be redundant at this point but here we are
		# if you fail this assertion the program is in an error state
		assert(self.__action is not None)
		return self.__action.asRow()

	def getLogs(self) -> str:
		if self.__action is None:
			return "[No logs. Action has not been run.]"
		else:
			return self.__action.getLogs()

	def changeDataLineWidget(self):
		actionType = self.__actionTypeComboBox.currentIndex()
		if actionType == Action.COMMAND:
			newDataWidget = CommandWidget()
		elif actionType == Action.FILE_COPY:
			newDataWidget = FileCopyWidget()
		elif actionType == Action.SHELL_SCRIPT:
			newDataWidget = ShellScriptWidget()
		else:
			raise Exception("Invalid action type!")
		w = QWidget()
		newDataWidget.setupUi(w)
		self.__dataLine = newDataWidget
		self.__parent.setCellWidget(self.__idx, ActionRow.DATA_COLUMN_IDX, w)

	def resetIndex(self, idx : int):
		self.__idx = idx

class ActionList:
	def __init__(self, filename : str = None):
		self.__actionList = []
		if filename is None:
			return
		with open(filename, 'r') as f:
			idx = 0
			for line in f:
				actionType, data, comment, sudo = [s.strip() for s in line.split(",")]
				actionType = int(actionType)
				assert(actionType < 3)
				sudo = sudo.lower() == "true"
				actionTypeComboBox = QComboBox()
				actionTypeComboBox.addItems(["Command", "File Copy", "Shell Script"])
				actionTypeComboBox.setIndex(actionType)
				# TODO: from here
				idx += 1

	def addActionRow(self, actionRow : ActionRow):
		self.__actionList.append(actionRow)

	def executeAll(self, lab : Lab, passwd : str, selectedMachinesOnly : bool = False):
		print("Attempting to execute actions on all machines")
		# Create one threading group that executes all actions concurrently
		config = fabric.Config(overrides={'sudo': {'password': passwd}})
		connectionGroup = fabric.group.ThreadingGroup(' '.join(lab.toStrList(selectedMachinesOnly))
												, config=config)
		for a in self.__actionList:
			a.executeAction(connectionGroup)

	def executeSelected(self, lab : Lab, passwd : str, selectedMachinesOnly : bool = False):
		print("Attempting to execute actions just on selected machines")
		# Create one threading group that executes all actions concurrently
		config = fabric.Config(overrides={'sudo': {'password': passwd}})
		connectionGroup = fabric.group.ThreadingGroup(' '.join(lab.toStrList(selectedMachinesOnly))
												, config=config)
		for a in self.__actionList:
			if a.selected():
				a.executeAction(connectionGroup)

	def selectAll(self):
		for a in self.__actionList:
			a.select()

	def toggleSelected(self):
		for a in self.__actionList:
			a.toggleSelection()

	def deselectAll(self):
		for a in self.__actionList:
			a.select(False)

	def deleteSelected(self):
		def actionFilter(a : ActionRow) -> bool:
			kept = not a.selected()
			if not kept:
				a.delete()
			return kept
		self.__actionList = list(filter(actionFilter, reversed(self.__actionList)))
		# Reset actions' indexes
		for i in range(len(self.__actionList)):
			self.__actionList[i].resetIndex(i)

	def save(self, filename):
		with open(filename, 'w') as f:
			f.writelines([a.asRow() for a in self.__actionList])

	def empty(self) -> bool:
		return len(self.__actionList) == 0


if __name__ == "__main__":
	print("Cannot run this file!")
	exit(1)
