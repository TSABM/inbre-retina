'''
Main window structure and contents.
'''
import PyQt5.QtWidgets as qtw
from View.WindowMenuBarView import WindowMenuBarView
from View.CenterBox import CenterBox

class MainWindowView(qtw.QMainWindow):
    def __init__(self):#telling main window to init 
        super().__init__()
        self.setWindowTitle("DemoApp")
    
    def addMenuBar(self, menuBar):
        self.setMenuBar(menuBar)
    
    def addCenterBox(self, centerBox):
        self.setCentralWidget(centerBox)