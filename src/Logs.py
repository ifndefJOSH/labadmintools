
from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore

class Logs:
	def __init__(self, stdout : str, stderr : str) -> None:
		self.stdout = stdout
		self.stderr = stderr

	def append(self, stdout : str, stderr : str) -> None:
		self.stdout += f"\n{stdout}"
		self.stderr += f"\n{stderr}"

	def __str__(self) -> str:
		return f"STDOUT:\n{self.stdout}\nSTDERR:\n{self.stderr}"

# A node in the tree view showing the results on each machine for one action
class ActionLogNode:
	pass # TODO

# A leaf node in the tree view showing the results on one machine for one action
class ActionMachineLogBranch:
	pass # TODO

class LogList:
	def __init__(self) -> None:
		self.__logList = []
