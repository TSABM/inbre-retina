from Model.masterMemory import MasterMemory
from Model.LabelData import LabelData, Cell, BoundingBox, Event

class LabelPopupModel():
    def __init__(self):
        super().__init__()
        pass

    def refresh(self):
        pass

    def submitData(self, boxID, frameNumber, boxDimensions, newCellsToAdd, cellsDict :dict, eventsToUpdate : dict):
        #this function is primarily used to upload a new bounding box, this means adding the box, updating the frame, updating events
        #and adding the new cells
        labelData : LabelData = MasterMemory.getLabelDataModel()

        boundingBoxes = [] 
        box = BoundingBox(boxID, frameNumber, boxDimensions[0], boxDimensions[1], boxDimensions[2], boxDimensions[3], list(cellsDict.keys()), list(eventsToUpdate.keys()))

        #need to add new cells
        cells = []
        for cellID in cellsDict.keys():
            cells.append(Cell(cellID, cellsDict.get(cellID))) #create a cell based on the cell id and the celltype (stored in the dict and found via the key of cell Id)

        #FIXME, here you should be updating events one by one not trying to just upload right? what about events that just had a cell added?
        #but can a new box be an old event? sure an old event type but the same event? Hmm multi frame events... why not?
        events = []
        '''
        for eventIds in eventsDict.keys():
            events.append(Event(eventID, eventType, boxID, cellIds))
        '''

        #add new cells to cells list
        labelData.addNewData(boundingBoxes, cells, events)
        
        
    
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
    
        