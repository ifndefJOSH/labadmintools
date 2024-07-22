# -*- coding: utf-8 -*-
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
import sys

from PyQt5 import *
from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore

def tr(s : str) -> str:
	return s

class DataLineWidget(object):
	def toData(self) -> str:
		print("Warning! You do not want to call this! You should have overridden this")
		return ""

	def parseData(self, data : str):
		print("Warning! You do not want to call this! You should have overridden this")

	def hasData(self) -> bool:
		print("Warning! You do not want to call this! You should have overridden this")
		return False

	def deMarginLayout(self, layout : QHBoxLayout):
		layout.setContentsMargins(0, 0, 0, 0)

class FileCopyWidget(DataLineWidget):
	def setupUi(self, Form):
		self.__form = Form
		if not Form.objectName():
			Form.setObjectName(u"File Copy Widget")
		Form.resize(258, 46)
		sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
		Form.setSizePolicy(sizePolicy)
		Form.setMaximumSize(QSize(16777215, 16777215))
		self.horizontalLayout = QHBoxLayout(Form)
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.sourcePathBox = QLineEdit(Form)
		self.sourcePathBox.setObjectName(u"sourcePathBox")
		self.sourcePathBox.setFrame(False)
		self.sourcePathBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

		self.horizontalLayout.addWidget(self.sourcePathBox)

		self.browseSourceFile = QToolButton(Form)
		self.browseSourceFile.setObjectName(u"browseSourceFile")

		self.horizontalLayout.addWidget(self.browseSourceFile)

		self.targetPathBox = QLineEdit(Form)
		self.targetPathBox.setObjectName(u"targetPathBox")
		self.targetPathBox.setFrame(False)
		self.targetPathBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

		self.horizontalLayout.addWidget(self.targetPathBox)


		self.retranslateUi(Form)

		QMetaObject.connectSlotsByName(Form)
		self.browseSourceFile.clicked.connect(self.browse)
	# setupUi

	def retranslateUi(self, Form):
		Form.setWindowTitle(QCoreApplication.translate("Form", u"File Copy Widget", None))
		self.sourcePathBox.setPlaceholderText(QCoreApplication.translate("Form", u"Source File", None))
		self.browseSourceFile.setText(QCoreApplication.translate("Form", u"...", None))
		self.targetPathBox.setPlaceholderText(QCoreApplication.translate("Form", u"Target Path (defaults to $HOME)", None))
		self.deMarginLayout(self.horizontalLayout)
	# retranslateUi

	def browse(self):
		fileName = QFileDialog.getOpenFileName(self.__form, tr("Open File"), os.getcwd(), tr("All Files (*)"))
		self.sourcePathBox.setText(fileName[0])

	def toData(self):
		assert(self.sourcePathBox.text() != "")
		return f"{self.sourcePathBox.text()} {self.targetPathBox.text()}"

	def parseData(self, data : str):
		try:
			frm, to = data.split(" ")
			self.sourcePathBox.setText(frm)
			self.targetPathBox.setText(to)
		except ValueError:
			self.sourcePathBox.setText(data)

	def hasData(self) -> bool:
		return self.sourcePathBox.text() != ""


class ShellScriptWidget(DataLineWidget):
	def setupUi(self, Form):
		self.__form = Form
		if not Form.objectName():
			Form.setObjectName(u"Shell Script Widget")
		Form.resize(258, 46)
		sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
		Form.setSizePolicy(sizePolicy)
		Form.setMaximumSize(QSize(16777215, 16777215))
		self.horizontalLayout = QHBoxLayout(Form)
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.sourcePathBox = QLineEdit(Form)
		self.sourcePathBox.setObjectName(u"sourcePathBox")
		self.sourcePathBox.setFrame(False)
		self.sourcePathBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

		self.horizontalLayout.addWidget(self.sourcePathBox)

		self.browseSourceFile = QToolButton(Form)
		self.browseSourceFile.setObjectName(u"browseSourceFile")

		self.horizontalLayout.addWidget(self.browseSourceFile)


		self.retranslateUi(Form)

		QMetaObject.connectSlotsByName(Form)
		self.browseSourceFile.clicked.connect(self.browse)
	# setupUi

	def retranslateUi(self, Form):
		Form.setWindowTitle(QCoreApplication.translate("Form", u"Shell Script Widget", None))
		self.sourcePathBox.setPlaceholderText(QCoreApplication.translate("Form", u"Path to Script", None))
		self.browseSourceFile.setText(QCoreApplication.translate("Form", u"...", None))
		self.deMarginLayout(self.horizontalLayout)
	# retranslateUi

	def browse(self):
		fileName = QFileDialog.getOpenFileName(self.__form, tr("Open File"), os.getcwd(), tr("Shell scripts (*.sh)\nAll files (*)"))
		self.sourcePathBox.setText(fileName[0])

	def toData(self):
		assert(self.sourcePathBox.text() != "")
		return f"{self.sourcePathBox.text()}"

	def parseData(self, data : str):
		self.sourcePathBox.setText(data)

	def hasData(self) -> bool:
		return self.sourcePathBox.text() != ""

class CommandWidget(DataLineWidget):
	def setupUi(self, Form):
		self.__form = Form
		if not Form.objectName():
			Form.setObjectName(u"Command Widget")
		Form.resize(258, 46)
		sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
		Form.setSizePolicy(sizePolicy)
		Form.setMaximumSize(QSize(16777215, 16777215))
		self.horizontalLayout = QHBoxLayout(Form)
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		commandBoxFont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
		self.commandBox = QLineEdit(Form)
		self.commandBox.setObjectName(u"commandBox")
		self.commandBox.setFont(commandBoxFont)
		self.commandBox.setFrame(False)
		self.commandBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

		self.horizontalLayout.addWidget(self.commandBox)

		self.retranslateUi(Form)

		QMetaObject.connectSlotsByName(Form)
	# setupUi

	def retranslateUi(self, Form):
		Form.setWindowTitle(QCoreApplication.translate("Form", u"Command Widget", None))
		self.commandBox.setPlaceholderText(QCoreApplication.translate("Form", u"Command", None))
		self.deMarginLayout(self.horizontalLayout)
	# retranslateUi

	def toData(self) -> str:
		return self.commandBox.text()

	def hasData(self) -> bool:
		return self.commandBox.text() != ""

	def parseData(self, data : str):
		self.commandBox.setText(data)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = QWidget()
	fcw = CommandWidget()
	fcw.setupUi(window)
	window.show()

	app.exec()
