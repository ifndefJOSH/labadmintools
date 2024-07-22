# -*- coding: utf-8 -*-

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore

import resources

class AboutDialog(object):
	def setupUi(self, AboutDialog):
		if not AboutDialog.objectName():
			AboutDialog.setObjectName(u"AboutDialog")
		AboutDialog.resize(582, 412)
		self.verticalLayout = QVBoxLayout(AboutDialog)
		self.verticalLayout.setObjectName(u"verticalLayout")
		self.aboutTabs = QTabWidget(AboutDialog)
		self.aboutTabs.setObjectName(u"aboutTabs")
		self.aboutTabs.setTabPosition(QTabWidget.South)
		self.aboutTabs.setDocumentMode(False)
		self.aboutTabs.setTabsClosable(False)
		self.aboutTabs.setMovable(False)
		self.aboutTab = QWidget()
		self.aboutTab.setObjectName(u"aboutTab")
		self.verticalLayout_4 = QVBoxLayout(self.aboutTab)
		self.verticalLayout_4.setObjectName(u"verticalLayout_4")
		self.aboutBox = QTextBrowser(self.aboutTab)
		self.aboutBox.setObjectName(u"aboutBox")
		self.aboutBox.setSource(QUrl(u"qrc:/about/about.md"))

		self.verticalLayout_4.addWidget(self.aboutBox)

		self.aboutTabs.addTab(self.aboutTab, "")
		self.licenseTab = QWidget()
		self.licenseTab.setObjectName(u"licenseTab")
		self.verticalLayout_2 = QVBoxLayout(self.licenseTab)
		self.verticalLayout_2.setObjectName(u"verticalLayout_2")
		self.licenseBox = QTextBrowser(self.licenseTab)
		self.licenseBox.setObjectName(u"licenseBox")
		self.licenseBox.setSource(QUrl(u"qrc:/about/gplv3.md"))
		self.licenseBox.setOpenExternalLinks(True)

		self.verticalLayout_2.addWidget(self.licenseBox)

		self.aboutTabs.addTab(self.licenseTab, "")
		self.ackTab = QWidget()
		self.ackTab.setObjectName(u"ackTab")
		self.verticalLayout_3 = QVBoxLayout(self.ackTab)
		self.verticalLayout_3.setObjectName(u"verticalLayout_3")
		self.acknowledgementsBox = QTextBrowser(self.ackTab)
		self.acknowledgementsBox.setObjectName(u"acknowledgementsBox")
		self.acknowledgementsBox.setSource(QUrl(u"qrc:/about/acknowledgement.md"))

		self.verticalLayout_3.addWidget(self.acknowledgementsBox)

		self.aboutTabs.addTab(self.ackTab, "")

		self.verticalLayout.addWidget(self.aboutTabs)

		self.buttonBox = QDialogButtonBox(AboutDialog)
		self.buttonBox.setObjectName(u"buttonBox")
		self.buttonBox.setOrientation(Qt.Horizontal)
		self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

		self.verticalLayout.addWidget(self.buttonBox)


		self.retranslateUi(AboutDialog)
		self.buttonBox.accepted.connect(AboutDialog.accept)
		self.buttonBox.rejected.connect(AboutDialog.reject)

		self.aboutTabs.setCurrentIndex(0)


		QMetaObject.connectSlotsByName(AboutDialog)
	# setupUi

	def retranslateUi(self, AboutDialog):
		AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"About LabAdminTools", None))
		self.aboutTabs.setTabText(self.aboutTabs.indexOf(self.aboutTab), QCoreApplication.translate("AboutDialog", u"About", None))
		self.licenseBox.setDocumentTitle(QCoreApplication.translate("AboutDialog", u"License (GPLv3)", None))

		self.aboutTabs.setTabText(self.aboutTabs.indexOf(self.licenseTab), QCoreApplication.translate("AboutDialog", u"License", None))
		self.aboutTabs.setTabText(self.aboutTabs.indexOf(self.ackTab), QCoreApplication.translate("AboutDialog", u"Acknowledgements", None))
	# retranslateUi

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	abt = AboutDialog()
	d = QDialog()
	abt.setupUi(d)
	d.exec()
