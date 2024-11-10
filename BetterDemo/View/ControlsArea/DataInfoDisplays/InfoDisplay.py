from PyQt5.QtGui import QColor, QPalette
import PyQt5.QtWidgets as qtw
from Presenter.InfoDisplayPresenter import InfoDisplayPresenter

class InfoDisplay(qtw.QWidget):
    def __init__(self, view, addDisplayContentMethod):
        super().__init__()
        self.layout = qtw.QVBoxLayout()
        self.presenter = InfoDisplayPresenter(view)
        
        #set a grey background
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("grey"))
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        
        addDisplayContentMethod()
        
        self.setLayout(self.layout)