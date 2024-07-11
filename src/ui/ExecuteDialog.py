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

import sys

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore

def getExecutionOptions() -> tuple:
	dialog = QDialog()
	ed = ExecuteDialog()
	ed.setupUi(dialog)
	dialog.show()
	print("Done")


class ExecuteDialog(object):
	def setupUi(self, executeDialog):
		if not executeDialog.objectName():
			executeDialog.setObjectName(u"executeDialog")
		executeDialog.resize(380, 240)
		executeDialog.setMaximumSize(QSize(380, 240))
		icon = QIcon()
		iconThemeName = u"media-playback-start"
		if QIcon.hasThemeIcon(iconThemeName):
			icon = QIcon.fromTheme(iconThemeName)
		else:
			icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

		executeDialog.setWindowIcon(icon)
		self.formLayout = QFormLayout(executeDialog)
		self.formLayout.setObjectName(u"formLayout")
		self.machinesWidget = QWidget(executeDialog)
		self.machinesWidget.setObjectName(u"machinesWidget")
		self.verticalLayout_2 = QVBoxLayout(self.machinesWidget)
		self.verticalLayout_2.setObjectName(u"verticalLayout_2")
		self.actionsOnAllMachines = QRadioButton(self.machinesWidget)
		self.actionsOnAllMachines.setObjectName(u"actionsOnAllMachines")
		self.actionsOnAllMachines.setChecked(True)

		self.verticalLayout_2.addWidget(self.actionsOnAllMachines)

		self.actionsOnSelectedMachines = QRadioButton(self.machinesWidget)
		self.actionsOnSelectedMachines.setObjectName(u"actionsOnSelectedMachines")

		self.verticalLayout_2.addWidget(self.actionsOnSelectedMachines)


		self.formLayout.setWidget(1, QFormLayout.FieldRole, self.machinesWidget)

		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.password = QLineEdit(executeDialog)
		self.password.setObjectName(u"password")
		self.password.setEchoMode(QLineEdit.Password)
		self.password.setClearButtonEnabled(True)

		self.horizontalLayout.addWidget(self.password)

		self.previewPassword = QToolButton(executeDialog)
		self.previewPassword.setObjectName(u"previewPassword")
		icon1 = QIcon()
		iconThemeName = u"view-visible"
		if QIcon.hasThemeIcon(iconThemeName):
			icon1 = QIcon.fromTheme(iconThemeName)
		else:
			icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

		self.previewPassword.setIcon(icon1)
		self.previewPassword.setCheckable(True)
		self.previewPassword.setAutoRaise(True)

		self.horizontalLayout.addWidget(self.previewPassword)


		self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout)

		self.buttonBox = QDialogButtonBox(executeDialog)
		self.buttonBox.setObjectName(u"buttonBox")
		self.buttonBox.setOrientation(Qt.Horizontal)
		self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

		self.formLayout.setWidget(6, QFormLayout.FieldRole, self.buttonBox)

		self.actionsWidget = QWidget(executeDialog)
		self.actionsWidget.setObjectName(u"actionsWidget")
		self.verticalLayout = QVBoxLayout(self.actionsWidget)
		self.verticalLayout.setObjectName(u"verticalLayout")
		self.allActions = QRadioButton(self.actionsWidget)
		self.allActions.setObjectName(u"allActions")
		self.allActions.setChecked(True)

		self.verticalLayout.addWidget(self.allActions)

		self.selectedActions = QRadioButton(self.actionsWidget)
		self.selectedActions.setObjectName(u"selectedActions")

		self.verticalLayout.addWidget(self.selectedActions)


		self.formLayout.setWidget(2, QFormLayout.FieldRole, self.actionsWidget)

		self.actionsLabel = QLabel(executeDialog)
		self.actionsLabel.setObjectName(u"actionsLabel")

		self.formLayout.setWidget(2, QFormLayout.LabelRole, self.actionsLabel)

		self.machinesLabel = QLabel(executeDialog)
		self.machinesLabel.setObjectName(u"machinesLabel")

		self.formLayout.setWidget(1, QFormLayout.LabelRole, self.machinesLabel)

		self.passwordLabel = QLabel(executeDialog)
		self.passwordLabel.setObjectName(u"passwordLabel")

		self.formLayout.setWidget(5, QFormLayout.LabelRole, self.passwordLabel)


		self.retranslateUi(executeDialog)
		self.buttonBox.accepted.connect(executeDialog.accept)
		self.buttonBox.rejected.connect(executeDialog.reject)

		QMetaObject.connectSlotsByName(executeDialog)
	# setupUi

	def retranslateUi(self, executeDialog):
		executeDialog.setWindowTitle(QCoreApplication.translate("executeDialog", u"Execution Options", None))
		self.actionsOnAllMachines.setText(QCoreApplication.translate("executeDialog", u"Execute Actions on All Machines", None))
		self.actionsOnSelectedMachines.setText(QCoreApplication.translate("executeDialog", u"Execute Actions Only on Selected Machines", None))
		self.previewPassword.setText(QCoreApplication.translate("executeDialog", u"...", None))
		self.allActions.setText(QCoreApplication.translate("executeDialog", u"Execute All Actions", None))
		self.selectedActions.setText(QCoreApplication.translate("executeDialog", u"Execute Only Selected Actions", None))
		self.actionsLabel.setText(QCoreApplication.translate("executeDialog", u"Actions", None))
		self.machinesLabel.setText(QCoreApplication.translate("executeDialog", u"Machines", None))
		self.passwordLabel.setText(QCoreApplication.translate("executeDialog", u"Password", None))
		self.setupSlots()
	# retranslateUi

	def setupSlots(self):
		self.previewPassword.clicked.connect(lambda : self.password.setEchoMode(QLineEdit.Normal if self.previewPassword.isChecked() else QLineEdit.Password))

if __name__ == "__main__":
	app = QApplication(sys.argv)
	# getExecutionOptions()
	window = QDialog()
	fcw = ExecuteDialog()
	fcw.setupUi(window)
	window.show()

	app.exec()
