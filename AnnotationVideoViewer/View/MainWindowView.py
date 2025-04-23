'''
Main window structure and contents.
'''
import PyQt5.QtWidgets as qtw

from View.WindowMenuBarView import WindowMenuBarView
from View.CenterBox import CenterBox

class MainWindowView(qtw.QMainWindow):
    def __init__(self):#telling main window to init 
        super().__init__()

        windowMenu = WindowMenuBarView()
        centerBoxWidget = CenterBox()

        self.setWindowTitle("Inbre Retina Footage Viewer")
        self.setMenuBar(windowMenu)
        self.setCentralWidget(centerBoxWidget)
        print("main window initalized")