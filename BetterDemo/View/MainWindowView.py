'''
Main window structure and contents.
'''
import PyQt5.QtWidgets as qtw

#from Presenter.MainWindowPresenter import MainWindowPresenter

from View.WindowMenuBarView import WindowMenuBarView
from View.CenterBox import CenterBox

class MainWindowView(qtw.QMainWindow):
    def __init__(self):#telling main window to init 
        super().__init__()
        #self.presenter = MainWindowPresenter(self)
        self.setWindowTitle("DemoApp")
        self.setMenuBar(WindowMenuBarView())
        self.setCentralWidget(CenterBox())
        print("main window initalized")