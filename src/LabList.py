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

from os import uname
from types import FunctionType

from PyQt5 import *
from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore

class LabComputer:
	AUTH_BY_PASSWORD = 0
	AUTH_BY_KEY = 1
	def __init__(self, username : str, ip : str, hostname : str, authMethod : int = AUTH_BY_PASSWORD) -> None:
		self.username = username
		self.ip = ip
		self.hostname = hostname
		if self.ip == "":
			self.ip = None
		if self.hostname == "":
			self.hostname = None
		if self.username == "":
			self.username = None
		self.authMethod = authMethod
		assert(ip is not None or hostname is not None)
		assert(username is not None)

	def __str__(self) -> str:
		# Prefer the hostname but fallback to the IP address
		return f"{self.username}@{self.hostname if self.hostname is not None else self.ip}"

	def asRow(self) -> str:
		host = self.hostname if self.hostname is not None else ''
		ip = self.ip if self.ip is not None else ''
		return f"{self.username},{ip},{host}\n"

class LabComputerRow:
	def __init__(self
			  , selectedBox : QCheckBox
			  , unameBox : QLineEdit
			  , ipBox : QLineEdit
			  , hostBox : QLineEdit
			  , authMethodBox : QComboBox) -> None:
		self.__selectedBox = selectedBox
		self.__unameBox = unameBox
		self.__ipBox = ipBox
		self.__hostBox = hostBox
		self.__authMethodBox = authMethodBox
		unameBox.setFrame(False)
		ipBox.setFrame(False)
		hostBox.setFrame(False)
		authMethodBox.setFrame(False)


	def widgets(self) -> tuple:
		return self.__selectedBox, self.__unameBox, self.__ipBox, self.__hostBox, self.__authMethodBox

	def asComputer(self) -> LabComputer:
		return LabComputer(self.__unameBox.text(), self.__ipBox.text(), self.__hostBox.text(), self.__authMethodBox.currentIndex())

	def selected(self) -> bool:
		return self.__selectedBox.isChecked()

	def select(self, selected : bool = True):
		self.__selectedBox.setChecked(selected)

	def toggleSelection(self):
		self.__selectedBox.setChecked(not self.selected())

	def delete(self, tableWidget : QTableWidget):
		tableWidget.removeRow(tableWidget.indexAt(self.__unameBox.pos()).row())

	def asRow(self) -> str:
		return self.asComputer().asRow()

class Lab:
	def __init__(self, filename : str | None, tableWidget : QTableWidget):
		self.__labComputerList = []
		self.__filename = filename
		self.__uiWidget = tableWidget
		if filename is None:
			return
		with open(filename, 'r') as f:
			for line in f:
				uname, ip, host, authMethod = [s.strip() for s in line.split(",")]
				unameBox = QLineEdit()
				unameBox.setText(uname)
				ipBox = QLineEdit()
				ipBox.setText(ip)
				hostBox = QLineEdit()
				hostBox.setText(host)
				authMethodBox = QComboBox()
				authMethodBox.addItems(["Password", "Keypair"])
				authMethodBox.setCurrentIndex(int(authMethod))
				# The UI will have to use widgets() to add these to the table
				self.__labComputerList.append(LabComputerRow(QCheckBox(), unameBox, ipBox, hostBox, authMethodBox))
		print(f"Loaded lab with {len(self.__labComputerList)} computers")

	def save(self, filename : str | None = None):
		if filename is None:
			filename = self.__filename
		assert(filename is not None)
		with open(filename, 'w') as f:
			f.writelines([c.asRow() for c in self.__labComputerList])

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
		# TODO: this doesn't update the UI
		# i = 0
		# for comp in self.__labComputerList:
		# 	if comp.selected():
		# 		comp.delete()
		# 		del self.__labComputerList[i]
		# 	else:
		# 		i += 1
		def machineFilter(a : LabComputerRow) -> bool:
			kept = not a.selected()
			if not kept:
				a.delete(self.__uiWidget)
			return kept
		self.__labComputerList = list(filter(machineFilter, reversed(self.__labComputerList)))

		print(self.__labComputerList)

	def toStrList(self, onlySelected : bool=False) -> list:
		return [str(l.asComputer()) for l in filter(lambda l : not onlySelected or l.selected() \
				, self.__labComputerList)]

	def empty(self) -> bool:
		return len(self.__labComputerList) == 0




