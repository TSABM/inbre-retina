from Presenter.AbstractPresenter import AbstractPresenter
from BetterDemo.Model.Canvases.ImageCanvas import ImageCanvas
from Model.masterMemory import MasterMemory
from BetterDemo.Model.Labels import Label

class CanvasPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
        self.model = ImageCanvas("test", 0)
        self.registerNewSubscriber("canvas", self)
        self.addSubscriber("labelData")
    
    def refresh(self):
        super().refresh()
        self.model.updatePixmap()

    def getCanvas(self):
        return self.model

    def getSelectedLabel(self):
        return self.model.selectedLabel
    
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
        selectedBox = self.model.selectBox(point)
        self.publishToSubs()
        return selectedBox 
    
    def deselectBox(self):
        self.publishToSubs()
        self.model.deselectBox()
    
    def selectResizeCorner(self, point):
        return self.model.selectResizeCorner(point)

    def deleteBox(self):
        pass

    def getAllBoxes(self):
        pass

    def deleteAllBoxes(self):
        pass

    def resizeBox(self, newPosition, cornerIndex):
        self.model.resizeBox(newPosition, cornerIndex)

    def moveBox(self, point):
        self.model.moveBox(point)
        self.publishToSubs()

