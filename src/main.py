#!/usr/bin/env python3

import sys

from PyQt5 import *
from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore

import ui.MainWindow

if __name__ == "__main__":
	app = QApplication(sys.argv)
	mww = QMainWindow()
	mw = ui.MainWindow.MainWindow()
	mw.setupUi(mww)

	mww.show()
	sys.exit(app.exec())
