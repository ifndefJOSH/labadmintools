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
from threading import Thread

from PyQt5 import *
from PyQt5 import QtCore
from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *

from invoke.terminals import select  # type: ignore

from Actions import *
from LabList import *
from Logs import *
from ui.ExecuteDialog import createExecutionOptions
from ui.TemplateCommands import PossibleCommandDialog
from ui.uiUtils import *
from ui.About import AboutDialog

class MainWindow(object):
	def setupUi(self, mainWindow):
		if not mainWindow.objectName():
			mainWindow.setObjectName(u"mainWindow")
		self.__mainWindow = mainWindow
		mainWindow.setWindowIcon(QIcon(":/app-icon.svg"))
		mainWindow.resize(800, 639)
		self.actionNew_Lab_List = QAction(mainWindow)
		self.actionNew_Lab_List.setObjectName(u"actionNew_Lab_List")
		docNewIcon = createIcon(u"document-new")

		self.actionNew_Lab_List.setIcon(docNewIcon)
		self.actionOpen_Lab_List = QAction(mainWindow)
		self.actionOpen_Lab_List.setObjectName(u"actionOpen_Lab_List")
		openIcon = createIcon(u"document-open")

		self.actionOpen_Lab_List.setIcon(openIcon)
		self.actionSave_Lab_List = QAction(mainWindow)
		self.actionSave_Lab_List.setObjectName(u"actionSave_Lab_List")
		saveIcon = createIcon(u"document-save")

		self.actionSave_Lab_List.setIcon(saveIcon)
		self.actionExit = QAction(mainWindow)
		self.actionExit.setObjectName(u"actionExit")
		exitIcon = createIcon(u"exit")

		self.actionExit.setIcon(exitIcon)
		self.actionDelete_Action = QAction(mainWindow)
		self.actionDelete_Action.setObjectName(u"actionDelete_Action")
		deleteIcon = createIcon(u"delete")

		self.actionDelete_Action.setIcon(deleteIcon)
		self.actionTemplate_Action = QAction(mainWindow)
		self.actionTemplate_Action.setCheckable(True)
		self.actionDelete_Action.setObjectName(u"actionTemplate_Action")
		# self.actionstdout_Logs = QAction(mainWindow)
		# self.actionstdout_Logs.setObjectName(u"actionstdout_Logs")
		# self.actionstdout_Logs.setCheckable(True)
		# self.actionstdout_Logs.setChecked(True)
		# self.actionstderr_Logs = QAction(mainWindow)
		# self.actionstderr_Logs.setObjectName(u"actionstderr_Logs")
		# self.actionstderr_Logs.setCheckable(True)
		# self.actionstderr_Logs.setChecked(True)
		self.actionScript_Action = QAction(mainWindow)
		self.actionScript_Action.setObjectName(u"actionScript_Action")
		self.actionCommand_Action = QAction(mainWindow)
		self.actionCommand_Action.setObjectName(u"actionCommand_Action")
		self.actionFile_Copy_Action = QAction(mainWindow)
		self.actionFile_Copy_Action.setObjectName(u"actionFile_Copy_Action")
		self.actionRun = QAction(mainWindow)
		self.actionRun.setObjectName(u"actionRun")
		startIcon = createIcon(u"media-playback-start")

		self.actionRun.setIcon(startIcon)
		self.actionSave_Action_List = QAction(mainWindow)
		self.actionSave_Action_List.setObjectName(u"actionSave_Action_List")
		self.actionSave_Action_List.setIcon(saveIcon)
		self.actionExport_Script = QAction(mainWindow)
		self.actionExport_Script.setObjectName(u"actionExport_Script")
		self.actionLoad_Action_List = QAction(mainWindow)
		self.actionLoad_Action_List.setObjectName(u"actionLoad_Action_List")
		self.actionLoad_Action_List.setIcon(openIcon)
		self.actionSave_Logs = QAction(mainWindow)
		self.actionSave_Logs.setObjectName(u"actionSave_Logs")
		self.actionSave_Logs.setIcon(saveIcon)
		self.actionClear_Logs = QAction(mainWindow)
		self.actionClear_Logs.setObjectName(u"actionClear_Logs")
		self.actionClear_Logs.setIcon(deleteIcon)
		self.centralwidget = QWidget(mainWindow)
		self.centralwidget.setObjectName(u"centralwidget")
		self.verticalLayout = QVBoxLayout(self.centralwidget)
		self.verticalLayout.setObjectName(u"verticalLayout")
		self.tabWidget = QTabWidget(self.centralwidget)
		self.tabWidget.setObjectName(u"tabWidget")
		self.tabWidget.setLayoutDirection(Qt.LeftToRight)
		self.tabWidget.setTabPosition(QTabWidget.West)
		self.tab = QWidget()
		self.tab.setObjectName(u"tab")
		self.verticalLayout_2 = QVBoxLayout(self.tab)
		self.verticalLayout_2.setObjectName(u"verticalLayout_2")
		self.machineListWidget = QTableWidget(self.tab)
		if (self.machineListWidget.columnCount() < 4):
			self.machineListWidget.setColumnCount(4)
		__qtablewidgetitem = QTableWidgetItem()
		self.machineListWidget.setHorizontalHeaderItem(1, __qtablewidgetitem)
		__qtablewidgetitem1 = QTableWidgetItem()
		self.machineListWidget.setHorizontalHeaderItem(2, __qtablewidgetitem1)
		__qtablewidgetitem2 = QTableWidgetItem()
		self.machineListWidget.setHorizontalHeaderItem(3, __qtablewidgetitem2)
		__qtablewidgetitem8 = QTableWidgetItem()
		self.machineListWidget.setHorizontalHeaderItem(0, __qtablewidgetitem8)
		self.machineListWidget.setObjectName(u"machineListWidget")

		self.verticalLayout_2.addWidget(self.machineListWidget)

		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.addMachine = QToolButton(self.tab)
		self.addMachine.setObjectName(u"addMachine")
		addIcon = createIcon(u"edit-add")

		self.addMachine.setIcon(addIcon)

		self.horizontalLayout.addWidget(self.addMachine)

		self.deleteMachine = QToolButton(self.tab)
		self.deleteMachine.setObjectName(u"deleteMachine")
		self.deleteMachine.setIcon(deleteIcon)

		self.horizontalLayout.addWidget(self.deleteMachine)

		self.line_3 = QFrame(self.tab)
		self.line_3.setObjectName(u"line_3")
		self.line_3.setFrameShape(QFrame.VLine)
		self.line_3.setFrameShadow(QFrame.Sunken)

		self.horizontalLayout.addWidget(self.line_3)

		self.selectAllMachines = QToolButton(self.tab)
		self.selectAllMachines.setObjectName(u"selectAllMachines")
		selectAllIcon = createIcon(u"edit-select-all")

		self.selectAllMachines.setIcon(selectAllIcon)

		self.horizontalLayout.addWidget(self.selectAllMachines)

		self.invertMachineSelection = QToolButton(self.tab)
		self.invertMachineSelection.setObjectName(u"invertMachineSelection")
		invertSelectionIcon = createIcon(u"edit-select-invert")

		self.invertMachineSelection.setIcon(invertSelectionIcon)

		self.horizontalLayout.addWidget(self.invertMachineSelection)

		self.deselectAllMachines = QToolButton(self.tab)
		self.deselectAllMachines.setObjectName(u"deselectAllMachines")
		deselectIcon = createIcon(u"edit-select-none")

		self.deselectAllMachines.setIcon(deselectIcon)

		self.horizontalLayout.addWidget(self.deselectAllMachines)

		self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout.addItem(self.horizontalSpacer)


		self.verticalLayout_2.addLayout(self.horizontalLayout)

		self.tabWidget.addTab(self.tab, "")
		self.actionsTab = QWidget()
		self.actionsTab.setObjectName(u"actionsTab")
		self.actionsVerticalLayout = QVBoxLayout(self.actionsTab)
		self.actionsVerticalLayout.setObjectName(u"actionsVerticalLayout")
		self.actionListWidget = QTableWidget(self.actionsTab)
		if (self.actionListWidget.columnCount() < 5):
			self.actionListWidget.setColumnCount(5)
		__qtablewidgetitem7 = QTableWidgetItem()
		self.actionListWidget.setHorizontalHeaderItem(0, __qtablewidgetitem7)
		__qtablewidgetitem3 = QTableWidgetItem()
		self.actionListWidget.setHorizontalHeaderItem(1, __qtablewidgetitem3)
		__qtablewidgetitem4 = QTableWidgetItem()
		self.actionListWidget.setHorizontalHeaderItem(2, __qtablewidgetitem4)
		__qtablewidgetitem5 = QTableWidgetItem()
		self.actionListWidget.setHorizontalHeaderItem(3, __qtablewidgetitem5)
		__qtablewidgetitem6 = QTableWidgetItem()
		self.actionListWidget.setHorizontalHeaderItem(4, __qtablewidgetitem6)
		self.actionListWidget.setObjectName(u"actionListWidget")

		self.actionsVerticalLayout.addWidget(self.actionListWidget)

		self.actionsHorizontalLayout = QHBoxLayout()
		self.actionsHorizontalLayout.setObjectName(u"actionsHorizontalLayout")
		self.newAction = QToolButton(self.actionsTab)
		self.newAction.setObjectName(u"newAction")
		self.newAction.setIcon(docNewIcon)

		self.actionsHorizontalLayout.addWidget(self.newAction)

		self.openActionList = QToolButton(self.actionsTab)
		self.openActionList.setObjectName(u"openActionList")
		self.openActionList.setIcon(openIcon)

		self.actionsHorizontalLayout.addWidget(self.openActionList)

		self.saveActionList = QToolButton(self.actionsTab)
		self.saveActionList.setObjectName(u"saveActionList")
		self.saveActionList.setIcon(saveIcon)

		self.actionsHorizontalLayout.addWidget(self.saveActionList)

		self.line_2 = QFrame(self.actionsTab)
		self.line_2.setObjectName(u"line_2")
		self.line_2.setFrameShape(QFrame.VLine)
		self.line_2.setFrameShadow(QFrame.Sunken)

		self.actionsHorizontalLayout.addWidget(self.line_2)

		self.selectAllActions = QToolButton(self.actionsTab)
		self.selectAllActions.setObjectName(u"selectAllActions")
		self.selectAllActions.setIcon(selectAllIcon)

		self.actionsHorizontalLayout.addWidget(self.selectAllActions)

		self.selectInvertedActions = QToolButton(self.actionsTab)
		self.selectInvertedActions.setObjectName(u"selectInvertedActions")
		self.selectInvertedActions.setIcon(invertSelectionIcon)

		self.actionsHorizontalLayout.addWidget(self.selectInvertedActions)

		self.deselectAllActions = QToolButton(self.actionsTab)
		self.deselectAllActions.setObjectName(u"deselectAllActions")
		self.deselectAllActions.setIcon(deselectIcon)

		self.actionsHorizontalLayout.addWidget(self.deselectAllActions)

		self.line_4 = QFrame(self.actionsTab)
		self.line_4.setObjectName(u"line_4")
		self.line_4.setFrameShape(QFrame.VLine)
		self.line_4.setFrameShadow(QFrame.Sunken)

		self.actionsHorizontalLayout.addWidget(self.line_4)

		self.deleteSelectedActions = QToolButton(self.actionsTab)
		self.deleteSelectedActions.setObjectName(u"deleteSelectedActions")
		self.deleteSelectedActions.setIcon(deleteIcon)

		self.actionsHorizontalLayout.addWidget(self.deleteSelectedActions)

		self.runActions = QToolButton(self.actionsTab)
		self.runActions.setObjectName(u"runActions")
		self.runActions.setIcon(startIcon)
		self.runActions.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

		self.actionsHorizontalLayout.addWidget(self.runActions)

		self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.actionsHorizontalLayout.addItem(self.horizontalSpacer_3)


		self.actionsVerticalLayout.addLayout(self.actionsHorizontalLayout)

		self.tabWidget.addTab(self.actionsTab, "")
		self.logsTab = QWidget()
		self.logsTab.setObjectName(u"logsTab")
		self.horizontalLayout_3 = QHBoxLayout(self.logsTab)
		self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
		self.verticalLayout_4 = QVBoxLayout()
		self.verticalLayout_4.setObjectName(u"verticalLayout_4")
		self.logTree = QTreeWidget(self.logsTab)
		self.logTree.setObjectName(u"logTree")

		self.verticalLayout_4.addWidget(self.logTree)

		self.horizontalLayout_2 = QHBoxLayout()
		self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
		self.selectAllMachineLogs = QToolButton(self.logsTab)
		self.selectAllMachineLogs.setObjectName(u"selectAllMachineLogs")
		self.selectAllMachineLogs.setIcon(selectAllIcon)

		self.horizontalLayout_2.addWidget(self.selectAllMachineLogs)

		self.invertMachineLogSelection = QToolButton(self.logsTab)
		self.invertMachineLogSelection.setObjectName(u"invertMachineLogSelection")
		self.invertMachineLogSelection.setIcon(invertSelectionIcon)

		self.horizontalLayout_2.addWidget(self.invertMachineLogSelection)

		self.deselectAllMachineLogs = QToolButton(self.logsTab)
		self.deselectAllMachineLogs.setObjectName(u"deselectAllMachineLogs")
		self.deselectAllMachineLogs.setIcon(deselectIcon)

		self.horizontalLayout_2.addWidget(self.deselectAllMachineLogs)

		self.line = QFrame(self.logsTab)
		self.line.setObjectName(u"line")
		self.line.setFrameShape(QFrame.VLine)
		self.line.setFrameShadow(QFrame.Sunken)

		self.horizontalLayout_2.addWidget(self.line)

		self.deleteSelectedLogs = QToolButton(self.logsTab)
		self.deleteSelectedLogs.setObjectName(u"deleteSelectedLogs")
		self.deleteSelectedLogs.setIcon(deleteIcon)
		self.horizontalLayout_2.addWidget(self.deleteSelectedLogs)

		self.saveLogs = QToolButton(self.logsTab)
		self.saveLogs.setObjectName(u"saveLogs")
		self.saveLogs.setIcon(saveIcon)

		self.horizontalLayout_2.addWidget(self.saveLogs)

		self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


		self.verticalLayout_4.addLayout(self.horizontalLayout_2)


		self.horizontalLayout_3.addLayout(self.verticalLayout_4)

		self.logViewer = QTextEdit(self.logsTab)
		self.logViewer.setObjectName(u"logViewer")
		self.logViewer.setReadOnly(True)
		monoFont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
		self.logViewer.setFont(monoFont)

		self.horizontalLayout_3.addWidget(self.logViewer)

		self.tabWidget.addTab(self.logsTab, "")

		self.verticalLayout.addWidget(self.tabWidget)

		mainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QMenuBar(mainWindow)
		self.menubar.setObjectName(u"menubar")
		self.menubar.setGeometry(QRect(0, 0, 800, 30))
		self.menuLab = QMenu(self.menubar)
		self.menuLab.setObjectName(u"menuLab")
		self.menuScript = QMenu(self.menubar)
		self.menuScript.setObjectName(u"menuScript")
		self.menuAdd_Action = QMenu(self.menuScript)
		self.menuAdd_Action.setObjectName(u"menuAdd_Action")
		plusIcon = createIcon(u"add")

		self.menuAdd_Action.setIcon(plusIcon)
		self.menuLogs = QMenu(self.menubar)
		self.menuLogs.setObjectName(u"menuLogs")

		self.menuAbout = QMenu(self.menubar)
		self.actionAbout = QAction(self.menuAbout)
		self.actionDocumentation = QAction(self.menuAbout)
		self.menuAbout.addAction(self.actionDocumentation)
		self.menuAbout.addAction(self.actionAbout)
		# self.menuShow_Logs = QMenu(self.menuLogs)
		# self.menuShow_Logs.setObjectName(u"menuShow_Logs")
		mainWindow.setMenuBar(self.menubar)
		self.statusbar = QStatusBar(mainWindow)
		self.statusbar.setObjectName(u"statusbar")
		mainWindow.setStatusBar(self.statusbar)

		self.menubar.addAction(self.menuLab.menuAction())
		self.menubar.addAction(self.menuScript.menuAction())
		self.menubar.addAction(self.menuLogs.menuAction())
		self.menubar.addAction(self.menuAbout.menuAction())
		self.menuLab.addAction(self.actionNew_Lab_List)
		self.menuLab.addAction(self.actionOpen_Lab_List)
		self.menuLab.addAction(self.actionSave_Lab_List)
		self.menuLab.addSeparator()
		self.menuLab.addAction(self.actionExit)
		self.menuScript.addAction(self.menuAdd_Action.menuAction())
		self.menuScript.addAction(self.actionDelete_Action)
		self.menuScript.addAction(self.actionTemplate_Action)
		self.menuScript.addSeparator()
		self.menuScript.addAction(self.actionRun)
		self.menuScript.addSeparator()
		self.menuScript.addAction(self.actionSave_Action_List)
		self.menuScript.addAction(self.actionLoad_Action_List)
		self.menuAdd_Action.addAction(self.actionCommand_Action)
		self.menuAdd_Action.addAction(self.actionFile_Copy_Action)
		self.menuAdd_Action.addAction(self.actionScript_Action)
		self.menuScript.addSeparator()
		self.menuScript.addAction(self.actionExport_Script)
		self.menuLogs.addAction(self.actionSave_Logs)
		self.menuLogs.addAction(self.actionClear_Logs)

		self.progressBar = QProgressBar()
		self.progressBar.setRange(0, 0)
		self.progressBar.setVisible(False)
		self.statusbar.addPermanentWidget(self.progressBar)

		self.retranslateUi(mainWindow)

		self.tabWidget.setCurrentIndex(1)


		QMetaObject.connectSlotsByName(mainWindow)
	# setupUi

	def retranslateUi(self, mainWindow):
		mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Lab Admin Tools", None))
		self.actionNew_Lab_List.setText(QCoreApplication.translate("mainWindow", u"New Lab List", None))
		self.actionNew_Lab_List.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+N", None))
		self.actionOpen_Lab_List.setText(QCoreApplication.translate("mainWindow", u"Open Lab List", None))
		self.actionOpen_Lab_List.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+O", None))
		self.actionSave_Lab_List.setText(QCoreApplication.translate("mainWindow", u"Save Lab List", None))
		self.actionSave_Lab_List.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+S", None))
		self.actionExit.setText(QCoreApplication.translate("mainWindow", u"Exit", None))
		self.actionDelete_Action.setText(QCoreApplication.translate("mainWindow", u"Delete Action", None))
		self.actionTemplate_Action.setText(QCoreApplication.translate("mainWindow", u"Show Template Actions", None))
		# self.actionstdout_Logs.setText(QCoreApplication.translate("mainWindow", u"stdout Logs", None))
		# self.actionstderr_Logs.setText(QCoreApplication.translate("mainWindow", u"stderr Logs", None))
		self.actionScript_Action.setText(QCoreApplication.translate("mainWindow", u"Script Action", None))
		self.actionCommand_Action.setText(QCoreApplication.translate("mainWindow", u"Command Action", None))
		self.actionFile_Copy_Action.setText(QCoreApplication.translate("mainWindow", u"File Copy Action", None))
		self.actionRun.setText(QCoreApplication.translate("mainWindow", u"Run", None))
		self.actionSave_Action_List.setText(QCoreApplication.translate("mainWindow", u"Save Action List", None))
		self.actionSave_Action_List.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+Shift+S", None))
		self.actionLoad_Action_List.setText(QCoreApplication.translate("mainWindow", u"Load Action List", None))
		self.actionLoad_Action_List.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+Shift+O", None))
		self.actionTemplate_Action.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+Shift+T", None))
		self.actionExport_Script.setText(QCoreApplication.translate("mainWindow", u"Export Action List as Shell Script", None))
		self.actionExport_Script.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+Shift+E", None))
		self.actionSave_Logs.setText(QCoreApplication.translate("mainWindow", u"Save Logs", None))
		self.actionClear_Logs.setText(QCoreApplication.translate("mainWindow", u"Clear Logs", None))
		selectedLogsHeaderItem = self.machineListWidget.horizontalHeaderItem(0)
		selectedLogsHeaderItem.setText(QCoreApplication.translate("mainWindow", u"Selected", None));
		usernameHeaderItem = self.machineListWidget.horizontalHeaderItem(1)
		usernameHeaderItem.setText(QCoreApplication.translate("mainWindow", u"Username", None));
		ipAddressHeaderItem = self.machineListWidget.horizontalHeaderItem(2)
		ipAddressHeaderItem.setText(QCoreApplication.translate("mainWindow", u"IP Address", None));
		hostnameHeaderItem = self.machineListWidget.horizontalHeaderItem(3)
		hostnameHeaderItem.setText(QCoreApplication.translate("mainWindow", u"Hostname", None));
		self.addMachine.setText(QCoreApplication.translate("mainWindow", u"+", None))
		self.deleteMachine.setText(QCoreApplication.translate("mainWindow", u"-", None))
		self.selectAllMachines.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.invertMachineSelection.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.deselectAllMachines.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("mainWindow", u"Lab Machines", None))
		actionTypeHeaderItem = self.actionListWidget.horizontalHeaderItem(0)
		actionTypeHeaderItem.setText(QCoreApplication.translate("mainWindow", u"Selected", None));
		typeHeaderItem = self.actionListWidget.horizontalHeaderItem(1)
		typeHeaderItem.setText(QCoreApplication.translate("mainWindow", u"Type", None));
		dataHeaderItem = self.actionListWidget.horizontalHeaderItem(2)
		dataHeaderItem.setText(QCoreApplication.translate("mainWindow", u"Data", None));
		commentHeaderItem = self.actionListWidget.horizontalHeaderItem(3)
		commentHeaderItem.setText(QCoreApplication.translate("mainWindow", u"Comment", None));
		privHeaderItem = self.actionListWidget.horizontalHeaderItem(4)
		privHeaderItem.setText(QCoreApplication.translate("mainWindow", u"Privileged", None));
		self.newAction.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.openActionList.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.saveActionList.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.selectAllActions.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.selectInvertedActions.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.deselectAllActions.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.runActions.setText(QCoreApplication.translate("mainWindow", u"Run Action List", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.actionsTab), QCoreApplication.translate("mainWindow", u"Actions", None))
		logsHeader = self.logTree.headerItem()
		logsHeader.setText(2, QCoreApplication.translate("mainWindow", u"Return Code", None));
		logsHeader.setText(1, QCoreApplication.translate("mainWindow", u"Status", None));
		logsHeader.setText(0, QCoreApplication.translate("mainWindow", u"Computer and Actions", None));
		self.selectAllMachineLogs.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.invertMachineLogSelection.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.deselectAllMachineLogs.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.saveLogs.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.logsTab), QCoreApplication.translate("mainWindow", u"Logs", None))
		self.menuLab.setTitle(QCoreApplication.translate("mainWindow", u"Lab", None))
		self.menuScript.setTitle(QCoreApplication.translate("mainWindow", u"Actions", None))
		self.menuAdd_Action.setTitle(QCoreApplication.translate("mainWindow", u"Add Action", None))
		self.menuLogs.setTitle(QCoreApplication.translate("mainWindow", u"Logs", None))
		self.menuAbout.setTitle(QCoreApplication.translate("mainWindow", u"About", None))
		self.actionAbout.setText(QCoreApplication.translate("mainWindow", u"About", None))
		self.actionDocumentation.setText(QCoreApplication.translate("mainWindow", u"Documentation", None))
		# self.menuShow_Logs.setTitle(QCoreApplication.translate("mainWindow", u"Show Logs", None))
		self.setupSlots()
		self.flattenButtons(mainWindow)
		self.flattenButtons(self.actionsTab)
		self.flattenButtons(self.logsTab)
		self.flattenButtons(self.tab)
	# retranslateUi

	def showAbout(self):
		self.__abt = AboutDialog()
		self.__d = QDialog(self.__mainWindow)
		self.__abt.setupUi(self.__d)
		self.__d.exec()


	def flattenButtons(self, mainWindow : QObject):
		for c in mainWindow.children():
			if isinstance(c, QToolButton):
				c.setAutoRaise(True)

	def addAction(self, actionType : int = Action.COMMAND
			   , data : str | None = None
			   , priv : bool = False
			   , comment : str | None = None):
		assert(actionType >= 0 and actionType <= 2)
		newIdx = self.actionListWidget.rowCount()
		self.actionListWidget.insertRow(newIdx)
		selected = QCheckBox()
		actionTypeComboBox = QComboBox()
		actionTypeComboBox.addItems(["Command", "File Copy", "Shell Script"])
		actionTypeComboBox.setCurrentIndex(actionType)
		dataLine = CommandWidget() if actionType == Action.COMMAND else \
				FileCopyWidget() if actionType == Action.FILE_COPY else ShellScriptWidget()
		dataLineWidget = QWidget()
		dataLine.setupUi(dataLineWidget)
		if data is not None:
			dataLine.parseData(data)
		commentLine = QLineEdit()
		needsSudo = QCheckBox()
		needsSudo.setChecked(priv)
		if comment is not None:
			commentLine.setText(comment)
		ar = ActionRow(newIdx, actionTypeComboBox, dataLine, commentLine, needsSudo, selected, self.actionListWidget)
		self.__actionList.addActionRow(ar)
		# Add to UI
		self.actionListWidget.setCellWidget(newIdx, 0, selected)
		self.actionListWidget.setCellWidget(newIdx, 1, actionTypeComboBox)
		self.actionListWidget.setCellWidget(newIdx, 2, dataLineWidget)
		self.actionListWidget.setCellWidget(newIdx, 3, commentLine)
		self.actionListWidget.setCellWidget(newIdx, 4, needsSudo)
		self.tabWidget.setCurrentIndex(1)

	def openActions(self):
		filename = QFileDialog.getOpenFileName(None
										, "Open Action List"
										, os.getcwd()
										, "Action List (*.labactions)")
		if filename[0] == "":
			return
		self.__actionList = ActionList(filename[0])
		self.tabWidget.setCurrentIndex(1)

	def saveActions(self):
		filename = QFileDialog.getSaveFileName(None
										, "Save Action List"
										, os.getcwd()
										, "Action List (*.labactions)")
		if filename[0] == "":
			return
		try:
			self.__actionList.save(filename[0])
		except Exception as e:
			QMessageBox.critical(None, "Error Saving File", str(e))

	def addLabMachine(self):
		newIdx = self.machineListWidget.rowCount()
		self.machineListWidget.insertRow(newIdx)

		selected = QCheckBox()
		unameBox = QLineEdit()
		ipBox = QLineEdit()
		hostBox = QLineEdit()
		row = LabComputerRow(selected, unameBox, ipBox, hostBox)
		self.machineListWidget.setCellWidget(newIdx, 0, selected)
		self.machineListWidget.setCellWidget(newIdx, 1, unameBox)
		self.machineListWidget.setCellWidget(newIdx, 2, ipBox)
		self.machineListWidget.setCellWidget(newIdx, 3, hostBox)
		self.__lab.addLabComputerRow(row)

	def newLab(self):
		self.__lab.selectAll()
		self.__lab.deleteSelected()

	def runMyActions(self):
		self.__workerThread = QThread()
		self.__actionList.moveToThread(self.__workerThread)
		# password, accept = QInputDialog.getText(None, "Password", "Password", QLineEdit.Password)
		executionOptions = createExecutionOptions()
		accept = executionOptions.execute
		password = executionOptions.password
		justSelectedActions = not executionOptions.allActions
		justSelectedMachines = not executionOptions.allMachines
		if not accept:
			self.statusbar.showMessage("Aborted", 10000)
			return
		elif self.__lab.empty():
			QMessageBox.critical(None, "No lab computers!", "No lab computers!")
			self.statusbar.showMessage("Aborted. No lab computers", 10000)
			return
		elif self.__actionList.empty():
			QMessageBox.critical(None, "No actions!", "No Actions!")
			self.statusbar.showMessage("Aborted. No actions", 10000)
			return
		assert(password is not None)
		self.statusbar.showMessage("Started tasks...", 10000)
		self.progressBar.setValue(0)
		self.progressBar.setVisible(True)
		self.__actionList.moveToThread(self.__workerThread)
		def start():
			try:
				if justSelectedActions:
					self.progressBar.setRange(0, self.__actionList.selectedActionCount())
					self.__actionList.executeSelected(self.__lab, password, selectedMachinesOnly=justSelectedMachines)
				else:
					self.progressBar.setRange(0, self.__actionList.actionCount())
					self.__actionList.executeAll(self.__lab, password, selectedMachinesOnly=justSelectedMachines)
			except Exception as e:
				QMessageBox.critical(None, "Could not execute actions!", str(e))
				self.__workerThread.exit(1)
				self.progressBar.setVisible(False)
				self.statusbar.showMessage("Action execution failed!", 10000)
		self.__workerThread.started.connect(start)
		self.__workerThread.start()
		# Threading is buggy
		#worker = Thread(target=run)
		#worker.start()


	def openLab(self):
		filename = QFileDialog.getOpenFileName(None
										, "Open Computer Lab List"
										, os.getcwd()
										, "Computer Lab List (*.computerlab)")
		if filename[0] == "":
			return
		self.newLab()
		self.__lab = Lab(filename[0], self.machineListWidget)
		# This one we have to append widgets
		for row in self.__lab.widgets():
			selected, unameBox, ipBox, hostBox = row
			newIdx = self.machineListWidget.rowCount()
			self.machineListWidget.insertRow(newIdx)
			self.machineListWidget.setCellWidget(newIdx, 0, selected)
			self.machineListWidget.setCellWidget(newIdx, 1, unameBox)
			self.machineListWidget.setCellWidget(newIdx, 2, ipBox)
			self.machineListWidget.setCellWidget(newIdx, 3, hostBox)
		self.statusbar.showMessage(f"Opened lab list from f{filename[0]}")
		self.tabWidget.setCurrentIndex(0)

	def saveLab(self):
		filename = QFileDialog.getSaveFileName(None
										, "Save Computer Lab List"
										, os.getcwd()
										, "Computer Lab List (*.computerlab)")
		if filename[0] == "":
			return
		self.__lab.save(filename[0])
		self.statusbar.showMessage(f"Saved lab list to f{filename[0]}")

	def saveMyLogs(self):
		foldername = QFileDialog.getExistingDirectory(None
											, "Folder to save logs to"
											, os.getcwd())
		if foldername == "":
			self.statusbar.showMessage(f"Aborted save logs")
			return

		for lt in self.__allLogs:
			lt.saveLogs(foldername)
		self.statusbar.showMessage(f"Saved results to {foldername}")

	def logSelection(self, toggle : bool = False, deselectAll : bool = False):
		def selectItem(item : QTreeWidgetItem):
			item.setSelected((not toggle or not item.isSelected()) and not deselectAll)
			for i in range(item.childCount()):
				selectItem(item.child(i))
		selectItem(self.logTree.invisibleRootItem())

	def deleteLogSelection(self):
		for w in self.logTree.selectedItems():
			if w is None:
				break
			w.parent().removeChild(w)

	def exportShellScript(self):
		filename = QFileDialog.getSaveFileName(None
										, "Save action list as shell script"
										, os.getcwd()
										, "Shell Script (*.sh)")
		if filename[0] == "":
			return
		script = self.__actionList.toShellScript()
		with open(filename[0], 'w') as f:
			f.write(script)
		self.statusbar.showMessage(f"Saved action to script as f{filename[0]}")


	def setupSlots(self):
		# My 'Action' class is different then QAction. That is what is being referred to here
		self.__actionList = ActionList(None)
		self.__lab = Lab(None, self.machineListWidget)
		self.__allLogs = []
		self.__mainThread = self.__mainWindow.thread()
		self.__possibleCommandDialog = PossibleCommandDialog()
		self.__possibleCommandDialogWidget = QWidget()
		self.__possibleCommandDialog.setParentWindowCallback(self.addAction)
		self.__possibleCommandDialog.setupUi(self.__possibleCommandDialogWidget)
		self.actionsVerticalLayout.addWidget(self.__possibleCommandDialogWidget)
		self.__possibleCommandDialogWidget.setVisible(False)

		# Other stuff
		self.actionExit.triggered.connect(lambda : sys.exit(0))

		# Action editor stuff
		self.newAction.clicked.connect(self.addAction)
		self.actionCommand_Action.triggered.connect(self.addAction)
		self.actionFile_Copy_Action.triggered.connect(lambda: self.addAction(Action.FILE_COPY))
		self.actionScript_Action.triggered.connect(lambda: self.addAction(Action.SHELL_SCRIPT))
		self.openActionList.clicked.connect(self.openActions)
		self.actionLoad_Action_List.triggered.connect(self.openActions)
		self.saveActionList.clicked.connect(self.saveActions)
		self.actionSave_Action_List.triggered.connect(self.saveActions)
		self.selectAllActions.clicked.connect(lambda : self.__actionList.selectAll())
		self.selectInvertedActions.clicked.connect(lambda : self.__actionList.toggleSelected())
		self.deselectAllActions.clicked.connect(lambda : self.__actionList.deselectAll())
		self.actionDelete_Action.triggered.connect(lambda : self.__actionList.deleteSelected())
		self.actionRun.triggered.connect(self.runMyActions)
		self.runActions.clicked.connect(self.runMyActions)
		self.deleteSelectedActions.clicked.connect(lambda : self.__actionList.deleteSelected())
		self.actionExport_Script.triggered.connect(self.exportShellScript)
		self.actionTemplate_Action.triggered.connect(lambda : self.__possibleCommandDialogWidget.setVisible(self.actionTemplate_Action.isChecked()))

		# Lab machine stuff
		self.addMachine.clicked.connect(self.addLabMachine)
		# These need to be lambdas since self.__lab may change
		self.selectAllMachines.clicked.connect(lambda : self.__lab.selectAll())
		self.invertMachineSelection.clicked.connect(lambda : self.__lab.toggleSelected())
		self.deselectAllMachines.clicked.connect(lambda : self.__lab.deselectAll())
		self.deleteMachine.clicked.connect(lambda : self.__lab.deleteSelected())
		self.actionNew_Lab_List.triggered.connect(self.newLab)
		self.actionOpen_Lab_List.triggered.connect(self.openLab)
		self.actionSave_Lab_List.triggered.connect(self.saveLab)

		# Log stuff
		self.saveLogs.clicked.connect(self.saveMyLogs)
		self.actionSave_Logs.triggered.connect(self.saveMyLogs)
		self.selectAllMachineLogs.clicked.connect(self.logSelection)
		self.invertMachineLogSelection.clicked.connect(lambda : self.logSelection(True))
		self.deselectAllMachineLogs.clicked.connect(lambda : self.logSelection(deselectAll=True))
		self.actionClear_Logs.triggered.connect(self.logTree.clear)
		self.deleteSelectedLogs.clicked.connect(self.deleteLogSelection)

		# Other
		self.actionAbout.triggered.connect(self.showAbout)
		self.actionDocumentation.triggered.connect(lambda : QDesktopServices.openUrl(QUrl("https://github.com/ifndefJOSH/labadmintools/blob/main/docs/introduction.md")))

		self.setupLabKeyEvents()
		# Running Actions
		self.__actionList.progress.connect(lambda i : self.progressBar.setValue(i))
		self.__actionList.progressMessage.connect(lambda msg : self.statusbar.showMessage(msg))
		def finished():
			self.__allLogs.append(LogTree(
				self.logTree
				, self.__actionList.allLogs()
				, self.logViewer))
			self.tabWidget.setCurrentIndex(2)
			self.progressBar.setVisible(False)
			self.__workerThread.started.disconnect()
			self.__workerThread.quit()
			self.__actionList.moveToThread(self.__mainThread)
			self.statusbar.showMessage("Finished.")
		self.__actionList.finished.connect(finished)

	def setupLabKeyEvents(self):
		self.machineListWidget.installEventFilter(
			KeyPressFilter(self.machineListWidget, labOrActionList=self.__lab))
		self.actionListWidget.installEventFilter(
			KeyPressFilter(self.actionListWidget, labOrActionList=self.__actionList))

class KeyPressFilter(QObject):
	def __init__(self, parent : QObject | None = None, labOrActionList : ActionList | Lab | None = None) -> None:
		super().__init__(parent)
		self.__labOrActionList = labOrActionList

	def eventFilter(self, obj : QObject, event : QKeyEvent):
		if not isinstance(event, QKeyEvent) or event is None:
			return False
		assert(event is not None)
		if event.key() == QtCore.Qt.Key_Delete:
			self.__labOrActionList.deleteSelected()
		elif QtCore.Qt.ControlModifier == event.modifiers() and event.key() == QtCore.Qt.Key_A:
			self.__labOrActionList.selectAll()
		return False

