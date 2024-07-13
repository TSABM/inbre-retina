'''
Main window structure and contents.
'''
import PyQt5.QtWidgets as qtw

from Presenter.MainWindowPresenter import MainWindowPresenter

from View.WindowMenuBarView import WindowMenuBarView
from View.CenterBox import CenterBox
from View.AbstractView import AbstractView

class MainWindowView(AbstractView):
    def __init__(self):#telling main window to init 
        super().__init__(qtw.QMainWindow())
        self.presenter = MainWindowPresenter(self)
        self.view.setWindowTitle("DemoApp")
        self.view.setMenuBar(WindowMenuBarView())
        self.view.setCentralWidget(CenterBox())
        print("main window initalized")
    
    def refresh(self):
        super().refresh()
        pass