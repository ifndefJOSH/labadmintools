
from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *
from fabric import GroupResult, Result  # type: ignore

import datetime
import os
import socket
import paramiko.ssh_exception

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
	def __init__(self
			  , host : str
			  , result : Result | socket.gaierror | paramiko.ssh_exception.AuthenticationException
			  , parentItem : QTreeWidgetItem
			  , logViewer : QTextEdit) -> None:
		self.__host = host
		self.__result = result
		self.__parentItem = parentItem
		self.__item = QTreeWidgetItem(parentItem)
		self.__item.setText(0, host)
		if isinstance(result, Result):
			self.__item.setText(1, "Succeeded" if result.ok else "Failed")
			self.__item.setText(2, str(result.return_code))
			LogTree.callbacks[id(self.__item)] = lambda : logViewer.setText(result.shell)
			self.__stdoutItem = QTreeWidgetItem(self.__item)
			self.__stdoutItem.setText(0, "Logs on STDOUT")
			LogTree.callbacks[id(self.__stdoutItem)] = lambda : logViewer.setText(result.stdout)
			self.__stderrItem = QTreeWidgetItem(self.__item)
			self.__stderrItem.setText(0, "Logs on STDERR")
			LogTree.callbacks[id(self.__stderrItem)] = lambda : logViewer.setText(result.stderr)
		elif isinstance(result, socket.gaierror):
			self.__item.setText(1, "Network Error")
			LogTree.callbacks[id(self.__item)] = lambda : logViewer.setText(str(result))
		elif isinstance(result, paramiko.ssh_exception.AuthenticationException):
			self.__item.setText(1, "Authentication Error")
			LogTree.callbacks[id(self.__item)] = lambda : logViewer.setText(str(result))
		else:
			self.__item.setText(1, "Error")
			LogTree.callbacks[id(self.__item)] = lambda : logViewer.setText(str(result))


	def saveLogs(self, folder):
		if not isinstance(self.__result, Result):
			return
		with open(os.path.join(folder, f"{self.__result.command}.stdout.log"), 'w') as f:
			f.write(self.__result.stdout)
		with open(os.path.join(folder, f"{self.__result.command}.stderr.log"), 'w') as f:
			f.write(self.__result.stderr)


# A leaf node in the tree view showing the results on all machines for one action
class ActionMachineLogBranch:
	def __init__(self
			  , groupResult : GroupResult | None
			  , parent : QTreeWidgetItem
			  , logViewer : QTextEdit) -> None:
		self.__gResult = groupResult
		self.__parent = parent
		self.__treeItem = QTreeWidgetItem(parent)
		self.__treeItem.setText(0, f"Action `{self.getCommand()}`")
		LogTree.callbacks[id(self.__treeItem)] = lambda : logViewer.setText("Click on a machine to see its logs")
		if groupResult is not None:
			self.__children = [ActionLogNode(c.host, r, self.__treeItem, logViewer) for c, r in groupResult.items()]
		else:
			self.__children = None

	def getCommand(self) -> str:
		if self.__gResult is None or len(self.__gResult) == 0:
			return "[UNKNOWN]"
		for c, r in self.__gResult.items():
			if isinstance(r, Result):
				return r.command
		return "[UNKNOWN]"

	def saveLogs(self, folder : str):
		if self.__children is None:
			return
		for c in self.__children:
			c.saveLogs(folder)


class LogTree:
	callbacks = dict()
	def __init__(self, widget : QTreeWidget, groupResults : list, logViewer : QTextEdit) -> None:
		self.__widget = widget
		self.__widgetItem = QTreeWidgetItem(widget)
		self.__time = datetime.datetime.now()
		self.__widgetItem.setText(0, f"{self.__time} ({len(groupResults)} actions)")
		self.__logTreeItems = [ActionMachineLogBranch(gr, self.__widgetItem, logViewer) for gr in groupResults]
		def callback(item : QTreeWidgetItem, idx : int):
			if id(item) in LogTree.callbacks:
				LogTree.callbacks[id(item)]()
		self.__widget.itemClicked.connect(callback)

	def saveLogs(self, folder : str):
		subfolder = os.path.join(folder, str(self.__time))
		if not os.path.exists(subfolder):
			os.makedirs(subfolder)
		for ti in self.__logTreeItems:
			ti.saveLogs(subfolder)

