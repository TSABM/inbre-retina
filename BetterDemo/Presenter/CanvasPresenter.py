from Presenter.AbstractPresenter import AbstractPresenter
from Model.CanvasModel import CanvasModel
from Model.masterMemory import MasterMemory
from Model.LabelData import LabelData

class CanvasPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
        self.model : CanvasModel = CanvasModel()
        MasterMemory.setCanvas(self.model)
        #subs? label data? control view?
    
    #def setFile(self, file : str, projectName : str, projectID : int):
    #    self.model.setSource(file, projectName, projectID)
    
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
    def addAnnotation(self, maskPoints : list, cellType : str, cellId : int):
        addedBoxID = self.model.addAnnotation(maskPoints, cellType, cellId)
        return addedBoxID
        

    def selectBox(self, point):
        selectedBox = self.model.selectAnnotation(point)
        #self.publishToSubs()
        return selectedBox 
    
    def deselectBox(self):
        #self.publishToSubs()
        self.model.deselectBox()

    def playMovie(self):
        self.model.playMovie()

    def pauseMovie(self):
        self.model.pauseMovie()
        

