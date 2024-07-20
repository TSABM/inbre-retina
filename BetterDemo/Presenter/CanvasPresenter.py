from Presenter.AbstractPresenter import AbstractPresenter
from Model.Canvas import Canvas
from Model.masterMemory import MasterMemory

class CanvasPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
        self.model = Canvas()
        self.registerNewSubscriber("canvas", self)

    def getCanvas(self):
        return self.model
    
    def addBox(self, boxToAdd):
        #make the box into a label object
        #add label to the list of labels
        #add the label to the model
        self.model.addBox(boxToAdd)


    def getBox(self):
        pass

    def deleteBox(self):
        pass

    def getAllBoxes(self):
        pass

    def deleteAllBoxes(self):
        pass

