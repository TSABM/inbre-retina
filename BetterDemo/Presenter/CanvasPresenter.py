from Presenter.AbstractPresenter import AbstractPresenter
from Model.Canvas import Canvas
from Model.masterMemory import MasterMemory
from Model.Label import Label

class CanvasPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
        self.model = Canvas("test", 0)
        self.registerNewSubscriber("canvas", self)

    def getCanvas(self):
        return self.model
    
    #handle interactionMode
    def getInteractionMode(self):
        return MasterMemory.getInteractionMode()
    
    def setInteractionMode(self, mode : str):
        MasterMemory.setInteractionMode(mode)

    #Handle boxes
    def addBox(self, boxToAdd):
        #make the box into a label object
        label = Label(0, boxToAdd, "testType", "testID", "testDescription")
        #add label to the list of labels
        #add the label to the model
        frameLabels = self.model.addBox(label)
        MasterMemory.updateFrame(0, frameLabels)


    def selectBox(self, point):
        self.model.selectBox(point)
    
    def selectResizeCorner(self):
        return self.model.selectResizeCorner()

    def deleteBox(self):
        pass

    def getAllBoxes(self):
        pass

    def deleteAllBoxes(self):
        pass

    def resizeBox(self, box, point):
        self.model.resizeBox()  
        pass

    def moveBox(self, box, point):
        pass

