'''
Main window structure and contents. Defer rendering though to a view
'''
import PyQt5.QtWidgets as qtw
import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPen

class MainWindow(qtw.QMainWindow):
    def __init__(self):#telling main window to init 
        super().__init__()
        self.setWindowTitle("DemoApp")

        #self.menuBar() #FIXME remove this
        #presenter.presenter.drawMenuBar(windowLayout)?


        #mainBox = qtw.QSplitter(Qt.Horizontal)
        #mainBox.setChildrenCollapsible(False)
        #self.setCentralWidget(mainBox) #initalize the mainbox
        #centerBox = Presenter.centerBoxpresenter()
        #self.setCentralWidget(centerBoxPresenter.getCenterBox)


        self.show()
    
    def __del__(self):
        #try to close all subprocesses
        #(something like presenter.subpresenter.close())
        
        #Then close this window
        sys.exit()