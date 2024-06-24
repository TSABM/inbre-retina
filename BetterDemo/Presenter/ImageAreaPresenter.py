from Presenter.AbstractPresenter import AbstractPresenter
from Presenter.CurrentlyOpenFilesMenuPresenter import CurrentlyOpenFilesMenuPresenter
from Presenter.CanvasPresenter import CanvasPresenter

from View.ImageArea.ImageAreaView import ImageAreaView

class ImageAreaPresenter(AbstractPresenter):
    def __init__(self):
        super().__init__(ImageAreaView(), None)

    def addFileMenu(self):
        #A file "menu" for the currently open files in a folder
        self.fileMenu = CurrentlyOpenFilesMenuPresenter()
        self.view.setMenuBar(self.fileMenu.getView)

    def addCanvas(self):
        #rendering the canvas
        self.canvas = CanvasPresenter()
        self.view.addWidget(CanvasPresenter.getView())