import os

import fabric

class Logs:
	def __init__(self, stdout : str, stderr : str) -> None:
		self.stdout = stdout
		self.stderr = stderr

	def append(self, stdout : str, stderr : str) -> None:
		self.stdout += f"\n{stdout}"
		self.stderr += f"\n{stderr}"

class Action:
	COMMAND=0
	FILE_COPY=1
	SHELL_SCRIPT=2

	def __init__(self, actionType : int, data : str, comment : str, needsSudo : bool) -> None:
		self.__actionType = actionType
		self.__data = data
		self.__comment = comment
		self.__needsSudo = needsSudo
		self.__executed = False
		self.__logs = None

	def validate(self) -> tuple:
		'''
	Returns a tuple as to whether the Action is valid or not, and an error message
		'''
		if self.__actionType == Action.COMMAND:
			return (True, None)
		elif self.__actionType == Action.FILE_COPY:
			toFromPath = self.__data.split(" ")
			if len(toFromPath != 2):
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

	def execute(self, host : str, username : str="admin") -> None:
		valid, msg = self.validate()
		if not valid:
			print(f"Action cannot be executed! Reason {msg}")
			return
		if self.__executed:
			print(f"Warning: this action was already executed")

		endpoint = f"{username}@{host}"
		# Run the bad boi
		if self.__actionType == Action.COMMAND:
			# TODO: privilege escalation
			result = fabric.Connection(endpoint).run(self.__data, hide=True)
			self.__logs = Logs(result.stdout, result.stderr)
		elif self.__actionType == Action.FILE_COPY:
			# TODO
			pass
		elif self.__actionType == Action.SHELL_SCRIPT:
			SHELL_PATH="/tmp/tempShellScript"
			# First, copy the file to /tmp/tempShellScript
			# second, execute the file
			result = fabric.Connection(endpoint).run(SHELL_PATH)
			# delete the file


		self.__executed = True

class ActionRow:
	def __init__(self, idx : int, actionTypeComboBox : QComboBox, dataLine : DataLineWidget, commentLine : QLineEdit, needsSudoCheckBox : QCheckBox) -> None:
		self.__idx = idx
		self.__actionTypeComboBox = actionTypeComboBox
		self.__dataLine = dataLine
		self.__commentLine = commentLine
		self.__needsSudoCheckBox = needsSudoCheckBox
		self.__action = None

	def createAction(self) -> tuple:
		action = Action(
				self.__actionTypeComboBox.currentIndex()
				, self.__dataLine.toDataLineString()
				, self.__commentLine.text()
				, self.__needsSudoCheckBox.checked())
		valid, msg = action.validate()
		if valid:
			self.__action = action
		return valid, msg

	def executeAction(self, host : str, username : str = "admin") -> bool:
		if self.__action is None:
			return False
		self.__action.execute(host, username)
		return True

	def delete(self):
		# TODO
		pass

class ActionList:
	def __init__(self):
		self.__actionList = []

	def addActionRow(self, actionRow : ActionRow):
		self.__actionList.append(actionRow)

if __name__ == "__main__":
	print("Cannot run this file!")
	exit(1)
