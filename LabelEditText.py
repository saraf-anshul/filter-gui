from PyQt5.QtWidgets import (
	QWidget,
	QLineEdit,
	QHBoxLayout,
	QLabel
)
from PyQt5.QtCore import Qt

class LabelEditText(QWidget):
	def __init__(self, displayString, validator = None):
		super().__init__()

		self.input = ""

		### horizontal layout (Input)
		h_layout = QHBoxLayout(self)

		#### textview says "Sticer name"
		labelInx = QLabel(displayString, self)
		labelInx.setAlignment(Qt.AlignCenter)
		h_layout.addWidget(labelInx)
		####

		#### name dir textview
		labelIn = QLineEdit()
		labelIn.textEdited.connect(self.textNameChanged)
		labelIn.setAlignment(Qt.AlignCenter)
		if( validator ):
			labelIn.setValidator(validator)
		h_layout.addWidget(labelIn)
		####
	
	def textNameChanged(self, text):
		self.input = text
		print(self.input)
	
	def getText(self) -> str:
		return self.input
