from Model.masterMemory import MasterMemory
from Model.LabelData import LabelData, BoundingBox, Cell, Event

class LabelPopupModel():
    def __init__(self, view):
        super().__init__(view)
        pass

    def refresh(self):
        pass

    def submitData(self, newBoxesToAdd : list[BoundingBox], newCellsToAdd : list[Cell], newEventsToAdd : list[Event]):
        labelData : LabelData = MasterMemory.getLabelDataModel()
        
        #convert id's into objects
        labelData.addNewData(newBoxesToAdd, newEventsToAdd, newCellsToAdd)
        
        
    
    def getCellIDList(self):
        #FIXME
        return[]
    
    def getEventIDList(self):
        #FIXME
        return []