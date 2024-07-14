import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt

from Presenter.CenterBoxPresenter import CenterBoxPresenter
from View.MainControlsView import MainControlsView
from View.ImageArea.ImageAreaView import ImageAreaView
from View.AbstractView import AbstractView

class CenterBox(AbstractView):
    '''
    A container for the main windows items, in this implementation a splitter to allow some resizing
    '''
    def __init__(self):
        super().__init__(qtw.QSplitter())
        self.presenter = CenterBoxPresenter(self)
        self.view.setOrientation(Qt.Horizontal)
        self.view.setChildrenCollapsible(False)

        mainCntrlsView = MainControlsView()
        self.view.addWidget(mainCntrlsView.getWidget())
        imageAreaView = ImageAreaView()
        self.view.addWidget(imageAreaView.getWidget())

        print("center box initalized")
    
    def refresh(self):
        return super().refresh()