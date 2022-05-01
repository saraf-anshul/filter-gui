from PyQt5.QtWidgets import (
	QWidget,
	QPushButton,
	QVBoxLayout,
	QLabel,
	QFileDialog
)
from PyQt5.QtCore import pyqtSlot, Qt
from StorageUtils import *

class FileInfoAndSelectorBox(QWidget):
	def __init__(self, type, extension = "", maxSelect = 100):
		super().__init__()

		self.selectedFiles = []
		self.maxSelect = maxSelect
		self.fileType = type
		self.ext = extension

		self.setAcceptDrops(True)

		#### V-box for column
		vBoxLayout0 = QVBoxLayout(self)

		##### button select
		self.button = QPushButton(f'Select {type} file(s)', self)
		self.button.setToolTip(f'Select {type} file for conversion')
		self.button.clicked.connect(self.on_click_select)
		vBoxLayout0.addWidget(self.button)
		#####

		##### textview says "selected Dir"
		self.labelSelect = QLabel('', self)
		self.labelSelect.setText(f"Selected {type} Files:")
		self.labelSelect.setAlignment(Qt.AlignCenter)
		vBoxLayout0.addWidget(self.labelSelect)
		#####

		##### filename textview
		self.twFlies = QLabel(f'Selected {type} files', self)
		self.twFlies.setText(f"No {type} files selected")
		self.twFlies.setAlignment(Qt.AlignCenter)
		vBoxLayout0.addWidget(self.twFlies)	
		#####


	# select file onClick
	@pyqtSlot()
	def on_click_select(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		open_loc = getDefaultStorageLocation()

		fileName, _ = QFileDialog.getOpenFileNames(self,"Select input files", open_loc,f"All Files (*);;{self.fileType} Files (*.{self.ext})", options=options)
		if fileName:
			print(fileName)
			self.updateFilenames(fileName)
			self.setFilename(self.twFlies , self.selectedFiles)

	def dragEnterEvent(self, event):
		if event.mimeData().hasUrls():
			event.accept()
		else:
			event.ignore()

	def dropEvent(self, event):
		files = [u.toLocalFile() for u in event.mimeData().urls()]
		for f in files:
			print(f)
		self.updateFilenames(files)
		self.setFilename(self.twFlies , self.selectedFiles)

	def setFilename(self ,view, names):
		text = "\n".join([i.split('/')[-1] for i in names])
		view.setText(text)
		view.adjustSize()
	
	def updateFilenames(self, names):
		self.selectedFiles = names[:self.maxSelect]

