from Model.masterMemory import MasterMemory
from Model.LabelData import LabelData

class LabelPopupModel():
    def __init__(self, view):
        super().__init__(view)
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
        
        
    
    def getCellIDList(self):
        #FIXME
        return[]
    
    def getEventIDList(self):
        #FIXME
        return []