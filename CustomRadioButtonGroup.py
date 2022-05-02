from PyQt5.QtWidgets import (
	QWidget,
	QHBoxLayout,
	QLabel,
	QGroupBox,
	QVBoxLayout,
	QRadioButton
)
from PyQt5.QtCore import pyqtSlot, Qt
from StorageUtils import *

class CustomRadioButtonGroup(QWidget):
	onChange = None
	def __init__(self, title : str, options : list[str]):
		super().__init__()

		self.opts = options
		self.selected = ""
		
		layout = QHBoxLayout(self)

		label = QLabel(title)
		layout.addWidget(label)

		vBox = QGroupBox()
		vLayout = QVBoxLayout()

		self.rBtns = [ QRadioButton(i) for i in options ]
		for i in self.rBtns :
			i.toggled.connect( self.on_click_r_btn )
			vLayout.addWidget( i )
		self.rBtns[0].setChecked(True)

		vBox.setLayout(vLayout)
		layout.addWidget(vBox)
		###

	@pyqtSlot()
	def on_click_r_btn(self):
		radioBtn = self.sender()
		self.selected = radioBtn.text()
		if(self.onChange):
			self.onChange( self.selected )
		print( f"selected : {self.selected}" )