from PyQt5.QtWidgets import (
	QMainWindow, 
	QWidget, 
	QPushButton, 
	QFileDialog, 
	QLabel, 
	QVBoxLayout, 
	QHBoxLayout, 
	QGroupBox, 
)
from StorageUtils import *
from PyQt5.QtCore import pyqtSlot ,Qt
from LabelEditText import LabelEditText
from FileInfoAndSelectorBox import FileInfoAndSelectorBox
from CustomRadioButtonGroup import CustomRadioButtonGroup

from PyQt5.QtGui import QIntValidator,QDoubleValidator


class MainWidget(QMainWindow):

	saveLocation = ""

	def __init__(self):
		super().__init__()

		### window attrs
		self.setWindowTitle("Filter GUI")
		self.resize(300, 300)
		wid = QWidget(self)
		self.setCentralWidget(wid)
		layout = QVBoxLayout()
		wid.setLayout(layout)
		###

		### filter name label
		self.inputTB = LabelEditText("Filter name:")
		layout.addWidget(self.inputTB)
		###

		### brightness label
		self.filterB = LabelEditText("Brightness:", QDoubleValidator(-100.00, 100.00, 2))
		layout.addWidget(self.filterB)
		###

		### brightness label
		self.filterC = LabelEditText("Contrast:   ", QDoubleValidator(-100.00, 100.00, 2))
		layout.addWidget(self.filterC)
		###

		### brightness label
		self.filterS = LabelEditText("Saturation:", QDoubleValidator(-100.00, 100.00, 2))
		layout.addWidget(self.filterS)
		###

		### texture 
		self.filterT = FileInfoAndSelectorBox("Texture", "png", 1)
		layout.addWidget(self.filterT)
		###

		### texture use?
		self.useT = CustomRadioButtonGroup(title = "Use Texture ?", options = ["Yes", "No"])
		layout.addWidget(self.useT)
		###

		### out-file dir select
		self.outputDir = QPushButton('Select output dir', self)
		self.outputDir.clicked.connect(self.on_click_dir)
		layout.addWidget(self.outputDir)
		###

		### horizontal layout (Output)
		horizontalGroupBox = QGroupBox()
		h_layout = QHBoxLayout()

		#### textview says "outupt Dir"
		self.labelOutx = QLabel('', self)
		self.labelOutx.setText("Output directory:")
		self.labelOutx.setAlignment(Qt.AlignCenter)
		h_layout.addWidget(self.labelOutx)
		####

		#### out-file dir textview
		self.labelOut = QLabel('This is label', self)
		self.labelOut.setText("No output directory selected")
		self.labelOut.setAlignment(Qt.AlignCenter)
		h_layout.addWidget(self.labelOut)
		####

		horizontalGroupBox.setLayout(h_layout)
		layout.addWidget(horizontalGroupBox)
		###

		### load save file or create
		try:
			with open( getLocationsFile() ,'r' ) as F:
				self.updateSaveLocation( json.load(F)['last'] )
		except:
			with open( getLocationsFile() ,'w' ) as F:
				json.dump({'last' : getDefaultStorageLocation()} ,F)
			self.updateSaveLocation( getDefaultStorageLocation() )
		###

		### run button
		self.button_run = QPushButton('Create', self)
		self.button_run.setToolTip('Run Script')
		self.button_run.setStyleSheet("QPushButton {background-color:#48A14D; border-radius: 4px; min-height: 22px;}")
		self.button_run.clicked.connect(self.run_script)
		layout.addWidget(self.button_run)
		###

	# download location onClick
	@pyqtSlot()
	def on_click_dir(self):
		dir = self.saveLocation

		dirName = QFileDialog().getExistingDirectory(self, 'Select an directory to save files' ,dir)
		if dirName:
			print(dirName)
			self.updateSaveLocation(dirName)
	
	@pyqtSlot()
	def run_script(self):
		oDir = self.saveLocation

		with open( getLocationsFile() ,'w' ) as F:
			json.dump({'last' : oDir} ,F)

		sf = self.filterT.selectedFiles
		hasTex = self.useT.selected == "Yes"
		t = None
		if( hasTex and len(sf) > 0 ):
			# hasTex = True
			t = sf[0] # cp: None: No such file or directory

		name = self.inputTB.getText()
		b = self.filterB.getText()
		c = self.filterC.getText()
		s = self.filterS.getText()
		transformAndSave(name, b, c, s, hasTex, t, oDir)

	def updateSaveLocation(self, loc):
		self.labelOut.setText(loc)
		self.saveLocation = loc

