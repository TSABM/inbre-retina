import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt

#from Presenter.CenterBoxPresenter import CenterBoxPresenter
from View.ControlsArea.ControlAreaView import ControlAreaView
from View.ImageArea.MediaAreaView import MediaAreaView

class CenterBox(qtw.QSplitter):
    '''
    A container for the main windows items, in this implementation a splitter to allow some resizing
    '''
    def __init__(self):
        super().__init__()
        #self.presenter = CenterBoxPresenter(self)
        self.setOrientation(Qt.Horizontal)
        self.setChildrenCollapsible(False)

        #adding widgets
        self.addWidget(ControlAreaView())
        self.addWidget(MediaAreaView())

        #setting stretch preferences
        self.setStretchFactor(0,0) #Dont auto stretch first widget
        self.setStretchFactor(1,1) #Auto stretch 2nd widget to fill space

        print("center box initalized")