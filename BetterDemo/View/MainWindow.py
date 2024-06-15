'''
Main window structure and contents. Defer rendering though to a view
'''
import PyQt5.QtWidgets as qtw
import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPen
from Presenter import MenuBarPresenter, CenterBoxPresenter

class MainWindow(qtw.QMainWindow):
    def __init__(self):#telling main window to init 
        super().__init__()
        self.setWindowTitle("DemoApp")

        menuBar = MenuBarPresenter(self) #initalize menubar and pass main window

        centerBox = CenterBoxPresenter(self)

        self.show()
    
    def __del__(self): #FIXME
        #try to close all subprocesses
        #(something like presenter.subpresenter.close())
        
        #Then close this window
        sys.exit()