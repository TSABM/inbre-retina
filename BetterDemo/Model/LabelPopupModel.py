from Model.masterMemory import MasterMemory
from Model.LabelData import LabelData, Cell, BoundingBox, Event

class LabelPopupModel():
    def __init__(self):
        super().__init__()
        pass

    def refresh(self):
        pass

    def submitNewLabelData(self, boxID : str, frameNumber : int, boxDimensions : list, cellsIncludedInBox :dict, eventsIncludedInBox : dict,  newCellTypes : set, newEventTypes : set):
        '''
        creates new types, cells, and events based on lists of new Ids. Creates a new box object, and then updates label data with all of the new data
        '''
        labelData : LabelData = MasterMemory.getLabelData()

        #add the new types
        for type in newCellTypes:
            labelData.addNewCellType(type)
        for type in newEventTypes:
            labelData.addNewEventType(type)

        #Add the new cells and new events
        existingCells : dict = labelData.getCells()
        existingEvents :dict = labelData.getEvents()
        for cellID in cellsIncludedInBox:
            if existingCells.get(cellID, None) != None:
                pass
            else:
                labelData.addNewCell(Cell(cellID, cellsIncludedInBox.get(cellID)))
        for eventID in eventsIncludedInBox:
            event : dict = existingEvents.get(eventID, None)
            boxes : dict = event.get("boxIDs")
            if event != None:
                #make sure the new box is assotiated with the existing event
                boxes.update({boxID : True})
            else:
                labelData.addNewEvent(Event(eventID, eventsIncludedInBox.get(eventID), boxID, cellsIncludedInBox))

        #add box
        labelData.updateBoundingBox(BoundingBox(boxID, frameNumber, boxDimensions[0], boxDimensions[1], 
                                                boxDimensions[2], boxDimensions[3], list(cellsIncludedInBox.keys()), 
                                                list(eventsIncludedInBox.keys())))
    
    def getCellIDs(self):
        '''
        requests the cells dictionary from label data and then returns the keys for that dict as a set
        '''
        labelData : LabelData = MasterMemory.getLabelData()
        cellsDict : dict = labelData.getCells()
        keys = set(cellsDict.keys())

        return keys
    
    def getCellTypes(self):
        '''
        requests the celltype dict from label data and then return the keys as a set
        '''
        labelData : LabelData = MasterMemory.getLabelData()
        typesDict : dict = labelData.getCellTypes()
        keys = set(typesDict.keys())
        return keys
    
    def getEventTypes(self):
        '''
        requests the event type dict from label data and then return the keys as a set
        '''
        labelData : LabelData = MasterMemory.getLabelData()
        typesDict : dict = labelData.getEventTypes()
        keys = set(typesDict.keys())
        return keys
    
    def getEventIDs(self):
        '''
        requests the events dictionary from label data and then returns the keys for that dict as a set
        '''
        labelData : LabelData = MasterMemory.getLabelData()
        eventsDict : dict = labelData.getEvents()
        keys = set(eventsDict.keys())

        return keys