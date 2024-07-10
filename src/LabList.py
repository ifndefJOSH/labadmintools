
from PyQt5 import *
from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore

class LabComputer:
	def __init__(self, username : str, ip : str, hostname : str) -> None:
		self.username = username
		self.ip = ip
		self.hostname = hostname
		if self.ip == "":
			self.ip = None
		if self.hostname == "":
			self.hostname = None
		if self.username == "":
			self.username = None
		assert(ip is not None or hostname is not None)
		assert(username is not None)

	def __str__(self) -> str:
		# Prefer the hostname but fallback to the IP address
		return f"{self.username}@{self.hostname if self.hostname is not None else self.ip}"

	def asRow(self) -> str:
		return f"{self.username},{self.ip if self.ip is not None else ""},{self.hostname if self.hostname is not None else ""}"

class LabComputerRow:
	def __init__(self
			  , selectedBox : QCheckBox
			  , unameBox : QTableWidgetItem
			  , ipBox : QTableWidgetItem
			  , hostBox : QTableWidgetItem) -> None:
		self.__selectedBox = selectedBox
		self.__unameBox = unameBox
		self.__ipBox = ipBox
		self.__hostBox = hostBox

	def widgets(self) -> tuple:
		return self.__selectedBox, self.__unameBox, self.__ipBox, self.__hostBox

	def asComputer(self) -> LabComputer:
		return LabComputer(self.__unameBox.text(), self.__ipBox.text(), self.__hostBox.text())

	def selected(self) -> bool:
		return self.__selectedBox.checked()

	def select(self, selected : bool = True):
		self.__selectedBox.setChecked(selected)

	def toggleSelection(self):
		self.__selectedBox.setChecked(not self.selected())

	def delete(self):
		# TODO
		pass

	def asRow(self) -> str:
		return self.asComputer().asRow()

class Lab:
	def __init__(self, filename : str = None):
		self.__labComputerList = []
		if filename is None:
			return
		with open(filename, 'r') as f:
			for line in f:
				uname, ip, host = [s.strip() for s in line.split(",")]
				unameBox = QTableWidgetItem()
				unameBox.setText(uname)
				ipBox = QTableWidgetItem()
				ipBox.setText(ip)
				hostBox = QTableWidgetItem()
				hostBox.setText(host)
				# The UI will have to use widgets() to add these to the table
				self.__labComputerList.append(LabComputerRow(QCheckBox(), unameBox, ipBox, hostBox))

	def save(self, filename):
		with open(filename, 'w') as f:
			f.writelines([c.asLine() for c in self.__labComputerList])

	def addLabComputerRow(self, labComputerRow : LabComputerRow):
		self.__labComputerList.append(labComputerRow)

	def widgets(self) -> list:
		return [l.widgets() for l in self.__labComputerList]

	def selectAll(self):
		for a in self.__labComputerList:
			a.select()

	def toggleSelected(self):
		for a in self.__labComputerList:
			a.toggleSelection()

	def deselectAll(self):
		for a in self.__labComputerList:
			a.select(False)

	def deleteSelected(self):
		for a in self.__labComputerList:
			if a.selected():
				a.delete()
				pass

	def toStrList(self) -> list:
		return [str(l.asComputer()) for l in self.__labComputerList]




