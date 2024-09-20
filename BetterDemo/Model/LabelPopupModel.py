from Model.masterMemory import MasterMemory
from Model.LabelData import LabelData, Cell, BoundingBox, Event

class LabelPopupModel():
    def __init__(self):
        super().__init__()
        pass

    def refresh(self):
        pass

    def submitData(self, newCellsToAdd, newEventsToAdd, boxID):
        labelData : LabelData = MasterMemory.getLabelDataModel()
        #add new cells to cells list
        for cell in newCellsToAdd:
                #add them to cells list
            labelData.addNewCell()

            pass
        #add new events to events list
        for event in newEventsToAdd:
            #make sure all relevent cellIDs are included
            labelData.addNewEvent()
            pass
        #add new box to boxes
            #make sure frame is updated to include the new box
        #if boxID != None
        if boxID != None:
            #add box
            labelData.addNewBoundingBox()
            
            pass
        
        
    
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