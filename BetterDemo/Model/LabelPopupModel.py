from Model.masterMemory import MasterMemory
from Model.LabelData import LabelData, Cell, BoundingBox, Event

class LabelPopupModel():
    def __init__(self):
        super().__init__()
        pass

    def refresh(self):
        pass

    def submitData(self, boundingBoxes : list, newCellsToAdd : list, newEventsToAdd :list):
        labelData : LabelData = MasterMemory.getLabelDataModel()
        #add new cells to cells list
        labelData.addNewData(boundingBoxes, newCellsToAdd, newEventsToAdd)
        
        
    
    def getCellIDs(self):
        '''
        requests the cells dictionary from label data and then returns the keys for that dict as a set
        '''
        labelData : LabelData = MasterMemory.getLabelDataModel()
        cellsDict : dict = labelData.getCells()
        keys = set(cellsDict.keys())

        return keys
    
    def getCellTypes(self):
        '''
        requests the celltype dict from label data and then return the keys as a set
        '''
        labelData : LabelData = MasterMemory.getLabelDataModel()
        typesDict : dict = labelData.getCellTypes()
        keys = set(typesDict.keys())
        return keys
    
    def getEventTypes(self):
        '''
        requests the event type dict from label data and then return the keys as a set
        '''
        labelData : LabelData = MasterMemory.getLabelDataModel()
        typesDict : dict = labelData.getEventTypes()
        keys = set(typesDict.keys())
        return keys
    
    def getEventIDs(self):
        '''
        requests the events dictionary from label data and then returns the keys for that dict as a set
        '''
        labelData : LabelData = MasterMemory.getLabelDataModel()
        eventsDict : dict = labelData.getEvents()
        keys = set(eventsDict.keys())

        return keys