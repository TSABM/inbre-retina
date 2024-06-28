from Presenter.AbstractPresenter import AbstractPresenter
from Model.Canvas import Canvas
from Model.masterMemory import MasterMemory

class CanvasPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
        self.subscribers.append("canvas")
        self.subscribers.append()
        pass

    def getCanvas(self):

        pass

