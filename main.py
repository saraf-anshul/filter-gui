#!/usr/bin/env python
from PyQt5.QtWidgets import QApplication
from MainWidget import MainWidget
import sys

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ui = MainWidget()
	ui.show()
	sys.exit(app.exec_())