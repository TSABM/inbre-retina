from Presenter.AbstractPresenter import AbstractPresenter
from Model.Canvas import Canvas
from View.ImageArea.CanvasView import CanvasView

class CanvasPresenter(AbstractPresenter):
    def __init__(self):
        super().__init__(CanvasView(), Canvas())
        pass
    
    def setScene(self):
        self.view.setScene(self.getScene())

    def getScene(self):
        return self.model

    def setBaseLayer():
        pass

    def addLayer():
        pass

    def removeLayer():
        pass

