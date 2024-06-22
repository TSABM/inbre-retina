'''
Main window structure and contents.
'''
import PyQt5.QtWidgets as qtw
from View.WindowMenuBarView import WindowMenuBarView
from View.CenterBox import CenterBox

class MainWindowView(qtw.QMainWindow):
    def __init__(self, windowMenuBar, centerBox):#telling main window to init 
        super().__init__()
        self.setWindowTitle("DemoApp")

        self.windowMenuBar = WindowMenuBarView(self) #initalize menubar and pass main window

        self.centerBox = CenterBox(self)