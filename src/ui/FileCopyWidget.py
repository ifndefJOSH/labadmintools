# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designernfweuN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import os
import sys

from PyQt5 import *
from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore

def tr(s : str) -> str:
	return s

class FileCopyWidget(object):
	def setupUi(self, Form):
		self.__form = Form
		if not Form.objectName():
			Form.setObjectName(u"File Copy Widget")
		Form.resize(258, 46)
		sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
		Form.setSizePolicy(sizePolicy)
		Form.setMaximumSize(QSize(16777215, 46))
		self.horizontalLayout = QHBoxLayout(Form)
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.sourcePathBox = QLineEdit(Form)
		self.sourcePathBox.setObjectName(u"sourcePathBox")

		self.horizontalLayout.addWidget(self.sourcePathBox)

		self.browseSourceFile = QToolButton(Form)
		self.browseSourceFile.setObjectName(u"browseSourceFile")

		self.horizontalLayout.addWidget(self.browseSourceFile)

		self.targetPathBox = QLineEdit(Form)
		self.targetPathBox.setObjectName(u"targetPathBox")

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
	# retranslateUi

	def browse(self):
		fileName = QFileDialog.getOpenFileName(self.__form, tr("Open File"), os.getcwd(), tr("All Files (*)"))
		self.sourcePathBox.setText(fileName[0])

	def toData(self, target, uname="admin"):
		assert(self.sourcePathBox.text() != "")
		return f"{self.sourcePathBox.text()} {uname}@{target}:{self.targetPathBox.text()}"

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = QWidget()
	fcw = FileCopyWidget()
	fcw.setupUi(window)
	window.show()

	app.exec()
