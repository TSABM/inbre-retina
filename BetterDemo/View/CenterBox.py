import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt

import MainControls
import View.ImageArea.ImageArea as ImageArea

class CenterBox():
    '''
    A container for the main windows items, in this implementation a splitter to allow some resizing
    '''
    def __init__(self, parentLayout):
        self.mainBox = qtw.QSplitter(Qt.Horizontal)
        self.mainBox.setChildrenCollapsible(False)
        parentLayout.setCentralWidget(self.mainBox)

        mainControlsArea = MainControls.MainControls(self.mainBox)
        imageArea = ImageArea.ImageArea(self.mainBox)