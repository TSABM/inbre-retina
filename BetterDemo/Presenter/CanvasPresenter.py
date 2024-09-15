from Presenter.AbstractPresenter import AbstractPresenter
from Model.CanvasModel import CanvasModel
from Model.masterMemory import MasterMemory
from Model.LabelData import LabelData

class CanvasPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
        self.model = CanvasModel()
        MasterMemory.setCanvas(self)
        #subs? label data? control view?
    
    def setFile(self, file):
        self.model.setfile(file)
        print("image file set, attempting to refresh")
        self.model.updatePixmap()
    
    def refresh(self):
        super().refresh()
        self.model.updatePixmap()

    def getCanvas(self):
        return self.model

    def getSelectedLabel(self):
        return self.model.selectedItem
    
    #handle interactionMode
    def getInteractionMode(self):
        return MasterMemory.getInteractionMode()
    
    def setInteractionMode(self, mode : str):
        MasterMemory.setInteractionMode(mode)

    #Handle boxes
    def addBox(self, boxToAdd): #FIXME
        #make the box into a label object
        #boxID
        #cellID
        #frame num
        #cell type
        #x, y, width, height
        #events
        cell = BoundingBox()
        #label = Label(0, boxToAdd, "testType", "testID", "testDescription") #FIXME
        #add label to the list of labels
        #add the label to the model
        frameLabels = self.model.addBox(key, label)
        MasterMemory.updateFrame(0, frameLabels)


    def selectBox(self, point):
        selectedBox = self.model.selectBox(point)
        self.publishToSubs()
        return selectedBox 
    
    def deselectBox(self):
        #self.publishToSubs()
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
        MasterMemory.labelData.re
    
    def generateNewBoundingBox(self, rect):
        pass

    def getLargestBoxID(self):
        labelData : LabelData = MasterMemory.getLabelDataModel()
        return labelData.getLargestBoxIdVal()
        

