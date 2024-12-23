from Presenter.AbstractPresenter import AbstractPresenter
from Model.CanvasModel import CanvasModel
from Model.masterMemory import MasterMemory
from Model.LabelData import LabelData

class CanvasPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
        self.model = CanvasModel()
        MasterMemory.setCanvas(self.model)
        #subs? label data? control view?
    
    def setFile(self, file):
        self.model.setfile(file)
    
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
    def addBox(self, rectToAdd):
        addedBoxID = self.model.addBox(rectToAdd)
        return addedBoxID

    def deleteBox(self, point):
        self.model.selectAndDelete(point)
        

    def selectBox(self, point):
        selectedBox = self.model.selectBox(point)
        #self.publishToSubs()
        return selectedBox 
    
    def deselectBox(self):
        #self.publishToSubs()
        self.model.deselectBox()
    
    def selectResizeCorner(self, point):
        return self.model.selectResizeCorner(point)

    def resizeBox(self, newPosition, cornerIndex):
        self.model.resizeBox(newPosition, cornerIndex)

    def moveBox(self, point):
        self.model.moveBox(point)

    def getLargestBoxID(self):
        labelData : LabelData = MasterMemory.getLabelData()
        return labelData.getLargestBoxIdVal()
        

