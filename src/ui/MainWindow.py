# -*- coding: utf-8 -*-

from PyQt5 import *
from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore

from Actions import *
from LabList import *

class MainWindow(object):
	def setupUi(self, mainWindow):
		if not mainWindow.objectName():
			mainWindow.setObjectName(u"mainWindow")
		mainWindow.resize(800, 639)
		self.actionNew_Lab_List = QAction(mainWindow)
		self.actionNew_Lab_List.setObjectName(u"actionNew_Lab_List")
		icon = QIcon()
		iconThemeName = u"document-new"
		if QIcon.hasThemeIcon(iconThemeName):
			icon = QIcon.fromTheme(iconThemeName)
		else:
			icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

		self.actionNew_Lab_List.setIcon(icon)
		self.actionOpen_Lab_List = QAction(mainWindow)
		self.actionOpen_Lab_List.setObjectName(u"actionOpen_Lab_List")
		icon1 = QIcon()
		iconThemeName = u"document-open"
		if QIcon.hasThemeIcon(iconThemeName):
			icon1 = QIcon.fromTheme(iconThemeName)
		else:
			icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

		self.actionOpen_Lab_List.setIcon(icon1)
		self.actionSave_Lab_List = QAction(mainWindow)
		self.actionSave_Lab_List.setObjectName(u"actionSave_Lab_List")
		icon2 = QIcon()
		iconThemeName = u"document-save"
		if QIcon.hasThemeIcon(iconThemeName):
			icon2 = QIcon.fromTheme(iconThemeName)
		else:
			icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

		self.actionSave_Lab_List.setIcon(icon2)
		self.actionExit = QAction(mainWindow)
		self.actionExit.setObjectName(u"actionExit")
		icon3 = QIcon()
		iconThemeName = u"exit"
		if QIcon.hasThemeIcon(iconThemeName):
			icon3 = QIcon.fromTheme(iconThemeName)
		else:
			icon3.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

		self.actionExit.setIcon(icon3)
		self.actionDelete_Action = QAction(mainWindow)
		self.actionDelete_Action.setObjectName(u"actionDelete_Action")
		icon4 = QIcon()
		iconThemeName = u"delete"
		if QIcon.hasThemeIcon(iconThemeName):
			icon4 = QIcon.fromTheme(iconThemeName)
		else:
			icon4.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

		self.actionDelete_Action.setIcon(icon4)
		self.actionstdout_Logs = QAction(mainWindow)
		self.actionstdout_Logs.setObjectName(u"actionstdout_Logs")
		self.actionstdout_Logs.setCheckable(True)
		self.actionstdout_Logs.setChecked(True)
		self.actionstderr_Logs = QAction(mainWindow)
		self.actionstderr_Logs.setObjectName(u"actionstderr_Logs")
		self.actionstderr_Logs.setCheckable(True)
		self.actionstderr_Logs.setChecked(True)
		self.actionScript_Action = QAction(mainWindow)
		self.actionScript_Action.setObjectName(u"actionScript_Action")
		self.actionCommand_Action = QAction(mainWindow)
		self.actionCommand_Action.setObjectName(u"actionCommand_Action")
		self.actionFile_Copy_Action = QAction(mainWindow)
		self.actionFile_Copy_Action.setObjectName(u"actionFile_Copy_Action")
		self.actionRun = QAction(mainWindow)
		self.actionRun.setObjectName(u"actionRun")
		icon5 = QIcon()
		iconThemeName = u"media-playback-start"
		if QIcon.hasThemeIcon(iconThemeName):
			icon5 = QIcon.fromTheme(iconThemeName)
		else:
			icon5.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

		self.actionRun.setIcon(icon5)
		self.actionSave_Action_List = QAction(mainWindow)
		self.actionSave_Action_List.setObjectName(u"actionSave_Action_List")
		self.actionSave_Action_List.setIcon(icon2)
		self.actionLoad_Action_List = QAction(mainWindow)
		self.actionLoad_Action_List.setObjectName(u"actionLoad_Action_List")
		self.actionLoad_Action_List.setIcon(icon1)
		self.actionSave_Logs = QAction(mainWindow)
		self.actionSave_Logs.setObjectName(u"actionSave_Logs")
		self.actionSave_Logs.setIcon(icon2)
		self.actionClear_Logs = QAction(mainWindow)
		self.actionClear_Logs.setObjectName(u"actionClear_Logs")
		self.actionClear_Logs.setIcon(icon4)
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
		icon6 = QIcon()
		iconThemeName = u"edit-add"
		if QIcon.hasThemeIcon(iconThemeName):
			icon6 = QIcon.fromTheme(iconThemeName)
		else:
			icon6.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

		self.addMachine.setIcon(icon6)

		self.horizontalLayout.addWidget(self.addMachine)

		self.deleteMachine = QToolButton(self.tab)
		self.deleteMachine.setObjectName(u"deleteMachine")
		self.deleteMachine.setIcon(icon4)

		self.horizontalLayout.addWidget(self.deleteMachine)

		self.line_3 = QFrame(self.tab)
		self.line_3.setObjectName(u"line_3")
		self.line_3.setFrameShape(QFrame.VLine)
		self.line_3.setFrameShadow(QFrame.Sunken)

		self.horizontalLayout.addWidget(self.line_3)

		self.selectAllMachines = QToolButton(self.tab)
		self.selectAllMachines.setObjectName(u"selectAllMachines")
		icon7 = QIcon()
		iconThemeName = u"edit-select-all"
		if QIcon.hasThemeIcon(iconThemeName):
			icon7 = QIcon.fromTheme(iconThemeName)
		else:
			icon7.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

		self.selectAllMachines.setIcon(icon7)

		self.horizontalLayout.addWidget(self.selectAllMachines)

		self.invertMachineSelection = QToolButton(self.tab)
		self.invertMachineSelection.setObjectName(u"invertMachineSelection")
		icon8 = QIcon()
		iconThemeName = u"edit-select-invert"
		if QIcon.hasThemeIcon(iconThemeName):
			icon8 = QIcon.fromTheme(iconThemeName)
		else:
			icon8.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

		self.invertMachineSelection.setIcon(icon8)

		self.horizontalLayout.addWidget(self.invertMachineSelection)

		self.deselectAllMachines = QToolButton(self.tab)
		self.deselectAllMachines.setObjectName(u"deselectAllMachines")
		icon9 = QIcon()
		iconThemeName = u"edit-select-none"
		if QIcon.hasThemeIcon(iconThemeName):
			icon9 = QIcon.fromTheme(iconThemeName)
		else:
			icon9.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

		self.deselectAllMachines.setIcon(icon9)

		self.horizontalLayout.addWidget(self.deselectAllMachines)

		self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout.addItem(self.horizontalSpacer)


		self.verticalLayout_2.addLayout(self.horizontalLayout)

		self.tabWidget.addTab(self.tab, "")
		self.tab_2 = QWidget()
		self.tab_2.setObjectName(u"tab_2")
		self.verticalLayout_3 = QVBoxLayout(self.tab_2)
		self.verticalLayout_3.setObjectName(u"verticalLayout_3")
		self.actionListWidget = QTableWidget(self.tab_2)
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

		self.verticalLayout_3.addWidget(self.actionListWidget)

		self.horizontalLayout_4 = QHBoxLayout()
		self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
		self.newAction = QToolButton(self.tab_2)
		self.newAction.setObjectName(u"newAction")
		self.newAction.setIcon(icon)

		self.horizontalLayout_4.addWidget(self.newAction)

		self.openActionList = QToolButton(self.tab_2)
		self.openActionList.setObjectName(u"openActionList")
		self.openActionList.setIcon(icon1)

		self.horizontalLayout_4.addWidget(self.openActionList)

		self.saveActionList = QToolButton(self.tab_2)
		self.saveActionList.setObjectName(u"saveActionList")
		self.saveActionList.setIcon(icon2)

		self.horizontalLayout_4.addWidget(self.saveActionList)

		self.line_2 = QFrame(self.tab_2)
		self.line_2.setObjectName(u"line_2")
		self.line_2.setFrameShape(QFrame.VLine)
		self.line_2.setFrameShadow(QFrame.Sunken)

		self.horizontalLayout_4.addWidget(self.line_2)

		self.selectAllActions = QToolButton(self.tab_2)
		self.selectAllActions.setObjectName(u"selectAllActions")
		self.selectAllActions.setIcon(icon7)

		self.horizontalLayout_4.addWidget(self.selectAllActions)

		self.selectInvertedActions = QToolButton(self.tab_2)
		self.selectInvertedActions.setObjectName(u"selectInvertedActions")
		self.selectInvertedActions.setIcon(icon8)

		self.horizontalLayout_4.addWidget(self.selectInvertedActions)

		self.deselectAllActions = QToolButton(self.tab_2)
		self.deselectAllActions.setObjectName(u"deselectAllActions")
		self.deselectAllActions.setIcon(icon9)

		self.horizontalLayout_4.addWidget(self.deselectAllActions)

		self.line_4 = QFrame(self.tab_2)
		self.line_4.setObjectName(u"line_4")
		self.line_4.setFrameShape(QFrame.VLine)
		self.line_4.setFrameShadow(QFrame.Sunken)

		self.horizontalLayout_4.addWidget(self.line_4)

		self.runActions = QToolButton(self.tab_2)
		self.runActions.setObjectName(u"runActions")
		self.runActions.setIcon(icon5)
		self.runActions.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

		self.horizontalLayout_4.addWidget(self.runActions)

		self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


		self.verticalLayout_3.addLayout(self.horizontalLayout_4)

		self.tabWidget.addTab(self.tab_2, "")
		self.tab_3 = QWidget()
		self.tab_3.setObjectName(u"tab_3")
		self.horizontalLayout_3 = QHBoxLayout(self.tab_3)
		self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
		self.verticalLayout_4 = QVBoxLayout()
		self.verticalLayout_4.setObjectName(u"verticalLayout_4")
		self.logTree = QTreeWidget(self.tab_3)
		self.logTree.setObjectName(u"logTree")

		self.verticalLayout_4.addWidget(self.logTree)

		self.horizontalLayout_2 = QHBoxLayout()
		self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
		self.selectAllMachineLogs = QToolButton(self.tab_3)
		self.selectAllMachineLogs.setObjectName(u"selectAllMachineLogs")
		self.selectAllMachineLogs.setIcon(icon7)

		self.horizontalLayout_2.addWidget(self.selectAllMachineLogs)

		self.invertMachineLogSelection = QToolButton(self.tab_3)
		self.invertMachineLogSelection.setObjectName(u"invertMachineLogSelection")
		self.invertMachineLogSelection.setIcon(icon8)

		self.horizontalLayout_2.addWidget(self.invertMachineLogSelection)

		self.deselectAllMachineLogs = QToolButton(self.tab_3)
		self.deselectAllMachineLogs.setObjectName(u"deselectAllMachineLogs")
		self.deselectAllMachineLogs.setIcon(icon9)

		self.horizontalLayout_2.addWidget(self.deselectAllMachineLogs)

		self.line = QFrame(self.tab_3)
		self.line.setObjectName(u"line")
		self.line.setFrameShape(QFrame.VLine)
		self.line.setFrameShadow(QFrame.Sunken)

		self.horizontalLayout_2.addWidget(self.line)

		self.saveLogs = QToolButton(self.tab_3)
		self.saveLogs.setObjectName(u"saveLogs")
		self.saveLogs.setIcon(icon2)

		self.horizontalLayout_2.addWidget(self.saveLogs)

		self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


		self.verticalLayout_4.addLayout(self.horizontalLayout_2)


		self.horizontalLayout_3.addLayout(self.verticalLayout_4)

		self.logViewer = QTextEdit(self.tab_3)
		self.logViewer.setObjectName(u"logViewer")
		self.logViewer.setReadOnly(True)

		self.horizontalLayout_3.addWidget(self.logViewer)

		self.tabWidget.addTab(self.tab_3, "")

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
		icon10 = QIcon()
		iconThemeName = u"add"
		if QIcon.hasThemeIcon(iconThemeName):
			icon10 = QIcon.fromTheme(iconThemeName)
		else:
			icon10.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

		self.menuAdd_Action.setIcon(icon10)
		self.menuLogs = QMenu(self.menubar)
		self.menuLogs.setObjectName(u"menuLogs")
		self.menuShow_Logs = QMenu(self.menuLogs)
		self.menuShow_Logs.setObjectName(u"menuShow_Logs")
		mainWindow.setMenuBar(self.menubar)
		self.statusbar = QStatusBar(mainWindow)
		self.statusbar.setObjectName(u"statusbar")
		mainWindow.setStatusBar(self.statusbar)

		self.menubar.addAction(self.menuLab.menuAction())
		self.menubar.addAction(self.menuScript.menuAction())
		self.menubar.addAction(self.menuLogs.menuAction())
		self.menuLab.addAction(self.actionNew_Lab_List)
		self.menuLab.addAction(self.actionOpen_Lab_List)
		self.menuLab.addAction(self.actionSave_Lab_List)
		self.menuLab.addSeparator()
		self.menuLab.addAction(self.actionExit)
		self.menuScript.addAction(self.menuAdd_Action.menuAction())
		self.menuScript.addAction(self.actionDelete_Action)
		self.menuScript.addSeparator()
		self.menuScript.addAction(self.actionRun)
		self.menuScript.addSeparator()
		self.menuScript.addAction(self.actionSave_Action_List)
		self.menuScript.addAction(self.actionLoad_Action_List)
		self.menuAdd_Action.addAction(self.actionCommand_Action)
		self.menuAdd_Action.addAction(self.actionFile_Copy_Action)
		self.menuAdd_Action.addAction(self.actionScript_Action)
		self.menuLogs.addAction(self.menuShow_Logs.menuAction())
		self.menuLogs.addAction(self.actionSave_Logs)
		self.menuLogs.addAction(self.actionClear_Logs)
		self.menuShow_Logs.addAction(self.actionstdout_Logs)
		self.menuShow_Logs.addAction(self.actionstderr_Logs)

		self.retranslateUi(mainWindow)

		self.tabWidget.setCurrentIndex(1)


		QMetaObject.connectSlotsByName(mainWindow)
	# setupUi

	def retranslateUi(self, mainWindow):
		mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Lab Admin Tools", None))
		self.actionNew_Lab_List.setText(QCoreApplication.translate("mainWindow", u"New Lab List", None))
		self.actionOpen_Lab_List.setText(QCoreApplication.translate("mainWindow", u"Open Lab List", None))
		self.actionSave_Lab_List.setText(QCoreApplication.translate("mainWindow", u"Save Lab List", None))
		self.actionExit.setText(QCoreApplication.translate("mainWindow", u"Exit", None))
		self.actionDelete_Action.setText(QCoreApplication.translate("mainWindow", u"Delete Action", None))
		self.actionstdout_Logs.setText(QCoreApplication.translate("mainWindow", u"stdout Logs", None))
		self.actionstderr_Logs.setText(QCoreApplication.translate("mainWindow", u"stderr Logs", None))
		self.actionScript_Action.setText(QCoreApplication.translate("mainWindow", u"Script Action", None))
		self.actionCommand_Action.setText(QCoreApplication.translate("mainWindow", u"Command Action", None))
		self.actionFile_Copy_Action.setText(QCoreApplication.translate("mainWindow", u"File Copy Action", None))
		self.actionRun.setText(QCoreApplication.translate("mainWindow", u"Run", None))
		self.actionSave_Action_List.setText(QCoreApplication.translate("mainWindow", u"Save Action List", None))
		self.actionLoad_Action_List.setText(QCoreApplication.translate("mainWindow", u"Load Action List", None))
		self.actionSave_Logs.setText(QCoreApplication.translate("mainWindow", u"Save Logs", None))
		self.actionClear_Logs.setText(QCoreApplication.translate("mainWindow", u"Clear Logs", None))
		___qtablewidgetitem8 = self.machineListWidget.horizontalHeaderItem(0)
		___qtablewidgetitem8.setText(QCoreApplication.translate("mainWindow", u"Selected", None));
		___qtablewidgetitem = self.machineListWidget.horizontalHeaderItem(1)
		___qtablewidgetitem.setText(QCoreApplication.translate("mainWindow", u"Username", None));
		___qtablewidgetitem1 = self.machineListWidget.horizontalHeaderItem(2)
		___qtablewidgetitem1.setText(QCoreApplication.translate("mainWindow", u"IP Address", None));
		___qtablewidgetitem2 = self.machineListWidget.horizontalHeaderItem(3)
		___qtablewidgetitem2.setText(QCoreApplication.translate("mainWindow", u"Hostname", None));
		self.addMachine.setText(QCoreApplication.translate("mainWindow", u"+", None))
		self.deleteMachine.setText(QCoreApplication.translate("mainWindow", u"-", None))
		self.selectAllMachines.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.invertMachineSelection.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.deselectAllMachines.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("mainWindow", u"Lab Machines", None))
		___qtablewidgetitem7 = self.actionListWidget.horizontalHeaderItem(0)
		___qtablewidgetitem7.setText(QCoreApplication.translate("mainWindow", u"Selected", None));
		___qtablewidgetitem3 = self.actionListWidget.horizontalHeaderItem(1)
		___qtablewidgetitem3.setText(QCoreApplication.translate("mainWindow", u"Type", None));
		___qtablewidgetitem4 = self.actionListWidget.horizontalHeaderItem(2)
		___qtablewidgetitem4.setText(QCoreApplication.translate("mainWindow", u"Data", None));
		___qtablewidgetitem5 = self.actionListWidget.horizontalHeaderItem(3)
		___qtablewidgetitem5.setText(QCoreApplication.translate("mainWindow", u"Comment", None));
		___qtablewidgetitem6 = self.actionListWidget.horizontalHeaderItem(4)
		___qtablewidgetitem6.setText(QCoreApplication.translate("mainWindow", u"Privileged", None));
		self.newAction.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.openActionList.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.saveActionList.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.selectAllActions.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.selectInvertedActions.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.deselectAllActions.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.runActions.setText(QCoreApplication.translate("mainWindow", u"Run Action List", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("mainWindow", u"Actions", None))
		___qtreewidgetitem = self.logTree.headerItem()
		___qtreewidgetitem.setText(2, QCoreApplication.translate("mainWindow", u"stdout Logs", None));
		___qtreewidgetitem.setText(1, QCoreApplication.translate("mainWindow", u"stderr Logs", None));
		___qtreewidgetitem.setText(0, QCoreApplication.translate("mainWindow", u"Computer and Actions", None));
		self.selectAllMachineLogs.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.invertMachineLogSelection.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.deselectAllMachineLogs.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.saveLogs.setText(QCoreApplication.translate("mainWindow", u"...", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("mainWindow", u"Logs", None))
		self.menuLab.setTitle(QCoreApplication.translate("mainWindow", u"Lab", None))
		self.menuScript.setTitle(QCoreApplication.translate("mainWindow", u"Actions", None))
		self.menuAdd_Action.setTitle(QCoreApplication.translate("mainWindow", u"Add Action", None))
		self.menuLogs.setTitle(QCoreApplication.translate("mainWindow", u"Logs", None))
		self.menuShow_Logs.setTitle(QCoreApplication.translate("mainWindow", u"Show Logs", None))
		self.setupSlots()
	# retranslateUi

	def addAction(self, actionType : int = Action.COMMAND):
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
		commentLine = QLineEdit()
		needsSudo = QCheckBox()
		ar = ActionRow(newIdx, actionTypeComboBox, dataLine, commentLine, needsSudo, selected, self.actionListWidget)
		self.__actionList.addActionRow(ar)
		# Add to UI
		self.actionListWidget.setCellWidget(newIdx, 0, selected)
		self.actionListWidget.setCellWidget(newIdx, 1, actionTypeComboBox)
		self.actionListWidget.setCellWidget(newIdx, 2, dataLineWidget)
		self.actionListWidget.setCellWidget(newIdx, 3, commentLine)
		self.actionListWidget.setCellWidget(newIdx, 4, needsSudo)

	def openActions(self):
		filename = QFileDialog.getOpenFileName(None
										, "Open Action List"
										, os.getcwd()
										, "Action List (*.labactions)")
		if filename[0] == "":
			return
		self.__actionList = ActionList(filename[0])

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
		row.setDelCallback(lambda : self.machineListWidget.removeRow(newIdx))
		self.__lab.addLabComputerRow(row)

	def newLab(self):
		self.__lab.selectAll()
		self.__lab.deleteSelected()

	def runMyActions(self, justSelected : bool = False):
		password, accept = QInputDialog.getText(None, "Password", "Password", QLineEdit.Password)
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
		self.statusbar.showMessage("Started tasks...", 10000)
		try:
			if justSelected:
				self.__actionList.executeSelected(self.__lab, password)
			else:
				self.__actionList.executeAll(self.__lab, password)
		except Exception as e:
			QMessageBox.critical(None, "Could not execute actions!", str(e))

	def openLab(self):
		filename = QFileDialog.getOpenFileName(None
										, "Open Computer Lab List"
										, os.getcwd()
										, "Computer Lab List (*.computerlab)")
		if filename[0] == "":
			return
		self.__lab = Lab(filename[0])
		self.__lab.setupCallbacks(self.machineListWidget)
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

	def saveLab(self):
		filename = QFileDialog.getSaveFileName(None
										, "Open Computer Lab List"
										, os.getcwd()
										, "Computer Lab List (*.computerlab)")
		if filename[0] == "":
			return
		self.__lab.save(filename[0])
		self.statusbar.showMessage(f"Saved lab list to f{filename[0]}")


	def setupSlots(self):
		# My 'Action' class is different then QAction. That is what is being referred to here
		self.__actionList = ActionList()
		self.__lab = Lab()

		# Action editor stuff
		self.newAction.clicked.connect(self.addAction)
		self.actionCommand_Action.triggered.connect(self.addAction)
		self.actionFile_Copy_Action.triggered.connect(lambda: self.addAction(Action.FILE_COPY))
		self.actionScript_Action.triggered.connect(lambda: self.addAction(Action.SHELL_SCRIPT))
		self.openActionList.clicked.connect(self.openActions)
		self.actionLoad_Action_List.triggered.connect(self.openActions)
		self.saveActionList.clicked.connect(self.saveActions)
		self.actionSave_Action_List.triggered.connect(self.saveActions)
		self.selectAllActions.clicked.connect(self.__actionList.selectAll)
		self.selectInvertedActions.clicked.connect(self.__actionList.toggleSelected)
		self.deselectAllActions.clicked.connect(self.__actionList.deselectAll)
		self.actionDelete_Action.triggered.connect(self.__actionList.deleteSelected)
		self.actionRun.triggered.connect(self.runMyActions)

		# Lab machine stuff
		self.addMachine.clicked.connect(self.addLabMachine)
		self.selectAllMachines.clicked.connect(self.__lab.selectAll)
		self.invertMachineSelection.clicked.connect(self.__lab.toggleSelected)
		self.deselectAllMachines.clicked.connect(self.__lab.deselectAll)
		self.deleteMachine.clicked.connect(lambda : (self.__lab.deleteSelected(), self.__lab.setupCallbacks(self.machineListWidget)))
		self.actionNew_Lab_List.triggered.connect(self.newLab)
		self.actionOpen_Lab_List.triggered.connect(self.openLab)
		self.actionSave_Lab_List.triggered.connect(self.saveLab)
