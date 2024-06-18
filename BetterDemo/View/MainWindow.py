'''
Main window structure and contents. Defer rendering though to a view
'''
import PyQt5.QtWidgets as qtw
from View.WindowMenuBar import WindowMenuBar
from View.CenterBox import CenterBox

class MainWindow(qtw.QMainWindow):
    def __init__(self):#telling main window to init 
        super().__init__()
        self.setWindowTitle("DemoApp")

        self.windowMenuBar = WindowMenuBar(self) #initalize menubar and pass main window

        self.centerBox = CenterBox(self)

        self.show()