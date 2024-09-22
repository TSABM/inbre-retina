from Model.masterMemory import MasterMemory
from Model.LabelData import LabelData, Cell, BoundingBox, Event

class LabelPopupModel():
    def __init__(self):
        super().__init__()
        pass

    def refresh(self):
        pass

    def submitData(self, boxID, frameNumber, boxDimensions, newCellsToAdd, cellIDs, newEventsToAdd, eventIDs):
        #ok so I need to 1) update existing cells so they know they are assotiated with a new bounding box as well as update
        #the given frame because this cell will need to be assotiated with it
        #then I also need to turn the new cells into Cell objects and store them in Label Data (also assotiating them with the frame and such)
        #the same idea needs to also be done with events
        labelData : LabelData = MasterMemory.getLabelDataModel()

        boundingBoxes = [] 
        box = BoundingBox(boxID, frameNumber, boxDimensions[0], boxDimensions[1], boxDimensions[2], boxDimensions[3], cellIDs, eventIDs)

        cells = []
        for cell in newCellsToAdd:
            cells.append(Cell(cellIDs))

        events = []

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
    
        