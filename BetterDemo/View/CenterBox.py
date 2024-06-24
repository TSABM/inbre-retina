import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt

class CenterBox(qtw.QSplitter):
    '''
    A container for the main windows items, in this implementation a splitter to allow some resizing
    '''
    def __init__(self):
        super().__init__()
        self.setOrientation(Qt.Horizontal)
        self.setChildrenCollapsible(False)

    def addMainControlsArea(self, mainControlsView):
        self.addWidget(mainControlsView)
    
    def addImageArea(self, imageArea):
        self.addWidget = imageArea