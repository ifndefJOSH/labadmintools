from PyQt5 import *
from PyQt5 import QtCore
from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *

import resources

def createIcon(iconThemeName : str) -> QIcon:
	if QIcon.hasThemeIcon(iconThemeName):
		icon = QIcon.fromTheme(iconThemeName)
	else:
		icon = QIcon(f":/icons/{iconThemeName}.svg")
	return icon


