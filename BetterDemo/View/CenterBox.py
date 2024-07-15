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
        self.viewWidget.setOrientation(Qt.Horizontal)
        self.viewWidget.setChildrenCollapsible(False)

        mainCntrlsView = MainControlsView()
        self.viewWidget.addWidget(mainCntrlsView.getWidget())
        imageAreaView = ImageAreaView()
        self.viewWidget.addWidget(imageAreaView.getWidget())

        print("center box initalized")
    
    def refresh(self):
        return super().refresh()