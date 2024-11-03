from PyQt5.QtGui import QColor, QPalette
import PyQt5.QtWidgets as qtw

class InfoDisplay(qtw.QWidget):
    def __init__(self, addDisplayContentFunction):
        self.layout = qtw.QVBoxLayout()
        
        #set a grey background
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("grey"))
        self.setPalette(palette)
        
        addDisplayContentFunction()
        
        self.setLayout(self.layout)