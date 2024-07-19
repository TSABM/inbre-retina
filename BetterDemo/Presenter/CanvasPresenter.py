from Presenter.AbstractPresenter import AbstractPresenter
from Model.Canvas import Canvas
from Model.masterMemory import MasterMemory

class CanvasPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
        self.registerNewSubscriber("canvas", Canvas())

    def getCanvas(self):
        return MasterMemory.getSubscriberByKey("canvas")
    
    def addBox(self):
        pass

    def getBox(self):
        pass

    def deleteBox(self):
        pass

    def getAllBoxes(self):
        pass

    def deleteAllBoxes(self):
        pass

