import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt

from View.ControlsArea.MainControlsView import MainControlsView
#from View.ControlsArea.LabelDataView import LabelDataView

class ControlAreaView(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())
        
        self.layout().addWidget(MainControlsView())
        #self.layout().addWidget(LabelDataView())
        