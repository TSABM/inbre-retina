from Presenter.AbstractPresenter import AbstractPresenter
from Model.Canvas import Canvas

class CanvasPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view, Canvas())
        pass

    def getScene(self):
        #check first to see if there is an open scene to turn to

        #if no open scene send a default scene
        return 

    def setBaseLayer():
        pass

    def addLayer():
        pass

    def removeLayer():
        pass

