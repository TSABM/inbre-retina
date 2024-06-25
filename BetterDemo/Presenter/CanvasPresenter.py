from Presenter.AbstractPresenter import AbstractPresenter
from Model.Canvas import Canvas

class CanvasPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view, Canvas())
        pass

    def getScene(self):
        return self.model.getScene()

    def setBaseLayer():
        pass

    def addLayer():
        pass

    def removeLayer():
        pass

