import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt

from View.ControlsArea.MainControlsView import MainControlsView
from View.ControlsArea.LabelDataView import LabelDataView

class ControlAreaView(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        mainControlsWidget = MainControlsView()
        labelDataWidget = LabelDataView()
        line = qtw.QFrame()
        line.setFrameShape(qtw.QFrame.HLine)
        line.setFrameShadow(qtw.QFrame.Sunken)

        self.setLayout(qtw.QVBoxLayout())

        self.layout().addWidget(mainControlsWidget)
        self.layout().addWidget(line)
        self.layout().addWidget(labelDataWidget)
        