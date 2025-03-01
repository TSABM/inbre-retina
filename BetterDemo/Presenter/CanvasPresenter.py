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

    def deleteBox(self, point):
        #self.model.selectAndDelete(point)
        print("FIXME deleting needs fixed")
        

    def selectBox(self, point):
        selectedBox = self.model.selectAnnotation(point)
        #self.publishToSubs()
        return selectedBox 
    
    def deselectBox(self):
        #self.publishToSubs()
        self.model.deselectBox()

    '''
    def moveBox(self, point):
        self.model.moveBox(point)
    '''
        
    def getLargestBoxID(self):
        labelData : LabelData = MasterMemory.getLabelData() # type: ignore
        return labelData.getLargestBoxIdVal()
        

