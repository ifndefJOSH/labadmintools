# -*- coding: utf-8 -*-

from types import FunctionType
from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore

import sys

class Command:
	def __init__(self, cmd : str, priv : bool = False):
		self.commandString = cmd
		self.privileged = priv

templateCommands = {
	"Package Updates":{
		"Update Packages (Debian, Ubuntu...)":Command("apt update && apt -y upgrade", True)
		, "Update Packages (CentOS >7, RHEL, Fedora...)":Command("dnf -y update --skip-broken", True)
		, "Update Packages (CentOS <=7, older RHEL...)":Command("yum -y update --skip-broken", True)
		, "Update Packages (Arch, Manjaro, Endeavor...)":Command("pacman -Syu", True)
	}
	, "Performance Commands":{
		"Current Memory Usage":Command("free -m")
		, "Current Disk Usage":Command("df -h")
		, "Running processes":Command("ps aux")
		, "All system logs":Command("journalctl --no-pager")
		, "Uptime":Command("uptime")
	}
	, "User Management Commands":{
		"Message All Users":Command("wall \"Message\"")
		, "Message Specific User":Command("echo \"Message\" | write USERNAME")
		, "Currently Logged-in Users":Command("who")
		, "Add User":Command("useradd USERNAME", True)
		, "Delete User":Command("userdel -fr USERNAME", True)
	}
	, "Firewall Controls":{
		"Start Firewall Service":Command("systemctl start firewalld", True)
		, "Enable Firewall Service":Command("systemctl enable firewalld", True)
		, "Enable HTTP":Command("firewall-cmd --zone=public --add-service=http --permanent", True)
		, "Enable HTTPS":Command("firewall-cmd --zone=public --add-service=https --permanent", True)
		, "Apply Firewall Changes":Command("firewall-cmd --reload", True)
		, "Block IPv4 Address":Command("firewall-cmd --zone=public --add-rich-rule='rule family=\"ipv4\" source address=\"x.x.x.x\" reject'", True)
		, "Block IPv6 Address":Command("firewall-cmd --zone=public --add-rich-rule='rule family=\"ipv6\" source address=\"ffff::ffff:ffff:ffff:ffff\" reject'", True)
		, "Open a Port":Command("firewall-cmd --zone=public --add-port=PORT_NUMBER/tcp --permanent", True)
		, "Close a Port":Command("firewall-cmd --zone=public --remove-port=PORT_NUMBER/tcp --permanent", True)
	}

}

class PossibleCommandDialog(object):
	commandMap = {}
	def __init__(self) -> None:
		self.parentWindowCallback = None

	def setParentWindowCallback(self, parentWindowCallback):
		self.parentWindowCallback = parentWindowCallback

	def setupUi(self, Dialog):
		if not Dialog.objectName():
			Dialog.setObjectName(u"PossibleCommandDialog")
		Dialog.resize(400, 300)
		self.verticalLayout = QVBoxLayout(Dialog)
		self.verticalLayout.setObjectName(u"verticalLayout")
		self.commandsTree = QTreeWidget(Dialog)
		self.commandsTree.setObjectName(u"commandsTree")

		self.verticalLayout.addWidget(self.commandsTree)
		self.verticalLayout.addWidget(QLabel("Template Commands: Double Click on a command to add it"))

		self.retranslateUi(Dialog)

		QMetaObject.connectSlotsByName(Dialog)
	# setupUi

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QCoreApplication.translate("Template Commands", u"Template Commands", None))
		commandsHeaderItem = self.commandsTree.headerItem()
		commandsHeaderItem.setText(2, QCoreApplication.translate("Template Commands", u"Privileged?", None));
		commandsHeaderItem.setText(1, QCoreApplication.translate("Template Commands", u"Command", None));
		commandsHeaderItem.setText(0, QCoreApplication.translate("Template Commands", u"Description", None));
		self.addTemplateCommands()
	# retranslateUi

	def addTemplateCommands(self):
		def callback(widget : QTreeWidget, idx : int):
			if id(widget) in PossibleCommandDialog.commandMap:
				description, command = PossibleCommandDialog.commandMap[id(widget)]
				print(f"Adding command `{command.commandString}`")
				if self.parentWindowCallback is not None:
					self.parentWindowCallback(data=command.commandString, priv=command.privileged, comment=description)
				# PossibleCommandDialog.commandMap[id(widget)]()
		self.commandsTree.itemDoubleClicked.connect(callback)
		for category, commands in templateCommands.items():
			catItem = QTreeWidgetItem(self.commandsTree)
			catItem.setText(0, category)
			self.commandsTree.addTopLevelItem(catItem)
			for description, command in commands.items():
				cmdItem = QTreeWidgetItem(catItem)
				cmdItem.setText(0, description)
				cmdItem.setText(1, command.commandString)
				cmdItem.setText(2, f"{'Yes' if command.privileged else 'No'}")
				catItem.addChild(cmdItem)
				PossibleCommandDialog.commandMap[id(cmdItem)] = (description, command)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	d = QDialog()
	pcd = PossibleCommandDialog()
	pcd.setupUi(d)
	d.exec()
