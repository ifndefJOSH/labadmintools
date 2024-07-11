'''
A graphical tool that makes IT peoples' lives easier

Written by Josh Jeppson (ifndefJOSH)

Copyright 2024 (c) Josh Jeppson, Utah State University

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import os

from PyQt5 import *
from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *
from fabric.group import GroupException
from invoke import call  # type: ignore

from LabList import LabComputer, Lab
from ui.FileCopyWidget import CommandWidget, DataLineWidget, FileCopyWidget, ShellScriptWidget
from Logs import *

import fabric

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
		result : fabric.GroupResult = None
		self.__status = Action.RUNNING
		try:
			if self.__actionType == Action.COMMAND:
				print(f"Running command `{self.__data}` on group")
				# privilege escalation
				if self.__needsSudo:
					result = connectionGroup.sudo(self.__data, hide=True)
				else:
					result = connectionGroup.run(self.__data, hide=True)
			elif self.__actionType == Action.FILE_COPY:
				# TODO: do we need any form of sudo?
				source, destination = [s.strip() for s in self.__data.split(" ")]
				print(f"Copying file `{source}` to group at path {destination}")
				result = connectionGroup.put(source, remote=destination)
			elif self.__actionType == Action.SHELL_SCRIPT:
				SHELL_PATH="/tmp/tempShellScriptLabAdmin"
				# First, copy the file to /tmp/tempShellScript
				print(f"Attempting to copy shell script `{self.__data}` to group...", end="")
				results = fabric.GroupResult()
				for c in connectionGroup:
					r = c.put(self.__data, remote=SHELL_PATH)
					if r.ok:
						print("ok. Now running script.")
						# second, execute the file, overwriting 'result' variable
						if self.__needsSudo:
							r = c.sudo(SHELL_PATH, hide=True)
						else:
							r = c.run(SHELL_PATH)
						# delete the file
						c.run(f"rm {SHELL_PATH}")
					results[c] = r
				result = results
		except GroupException as ge:
			# Report the errors in the logs viewer
			result = ge.result

		self.__logs = result # Logs(result.stdout, result.stderr)
		# self.__status = Action.SUCCEEDED if result.ok else Action.FAILED
		# print(f"{'Succeeded' if result.ok else 'Failed'}")
		self.__executed = True

	def asRow(self) -> str:
		return f"{self.__actionType},{self.__data},{self.__comment},{self.__needsSudo}\n"

	def getLogs(self) -> fabric.GroupResult | None:
		return self.__logs

	def statusMessage(self) -> str:
		if self.__actionType == Action.COMMAND:
			return f"command {self.__data}"
		elif self.__actionType == Action.FILE_COPY:
			frm, to = self.__data.split(" ")
			return f"copy file {frm} to HOST:{to}"
		else:
			return f"script {self.__data}"

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
			valid, _ = self.createAction()
			if not valid:
				return False
		# Redundant at this point
		assert(self.__action is not None)
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

	def statusMessage(self) -> str:
		self.createAction()
		if self.__action is None:
			return ""
		return self.__action.statusMessage()

	def getLogs(self) -> fabric.GroupResult | None:
		if self.__action is None:
			return None
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

class ActionList(QObject):
	finished = pyqtSignal()
	progress = pyqtSignal(int)
	progressMessage = pyqtSignal(str)
	def __init__(self, filename : str = None):
		super().__init__(None)
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
		config = fabric.Config(overrides={'sudo': {'password': passwd}, 'password':passwd})
		hosts = lab.toStrList(selectedMachinesOnly)
		connectionGroup = fabric.group.ThreadingGroup(*hosts
									, config=config
									, connect_kwargs={"password":passwd})
		completed = 0
		for a in self.__actionList:
			self.progressMessage.emit(f"Running `{a.statusMessage()}`")
			a.executeAction(connectionGroup)
			completed += 1
			self.progress.emit(completed)

		self.finished.emit()

	def executeSelected(self, lab : Lab, passwd : str, selectedMachinesOnly : bool = False):
		print("Attempting to execute actions just on selected machines")
		# Create one threading group that executes all actions concurrently
		config = fabric.Config(overrides={'sudo': {'password': passwd}})
		hosts = lab.toStrList(selectedMachinesOnly)
		connectionGroup = fabric.group.ThreadingGroup(*hosts
									, config=config
									, connect_kwargs={"password":passwd})
		completed = 0
		for a in self.__actionList:
			if a.selected():
				self.progressMessage.emit(f"Running `{a.statusMessage()}`")
				a.executeAction(connectionGroup)
				completed += 1
				self.progress.emit(completed)
		self.finished.emit()

	def selectedActionCount(self) -> int:
		return len(filter(lambda a: a.selected(), self.__actionList))

	def actionCount(self) -> int:
		return len(self.__actionList)

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

	def allLogs(self) -> list:
		return [a.getLogs() for a in self.__actionList]

if __name__ == "__main__":
	print("Cannot run this file!")
	exit(1)
