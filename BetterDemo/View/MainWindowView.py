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
        self.viewWidget.setWindowTitle("DemoApp")
        menuBar = WindowMenuBarView()
        self.viewWidget.setMenuBar(menuBar.getWidget())
        centerBox = CenterBox()
        self.viewWidget.setCentralWidget(centerBox.getWidget())
        print("main window initalized")
    
    def refresh(self):
        super().refresh()
        pass