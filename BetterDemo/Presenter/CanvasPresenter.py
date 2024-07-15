from Presenter.AbstractPresenter import AbstractPresenter
from Model.Canvas import Canvas
from masterMemory import MasterMemory

class CanvasPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
        self.addSubscriber("canvas", Canvas())

    def getCanvas(self):
        return MasterMemory.getSubscriberByKey("canvas")

