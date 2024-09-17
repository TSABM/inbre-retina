from Presenter.AbstractPresenter import AbstractPresenter
from Model.LabelPopupModel import LabelPopupModel
from Model.LabelData import LabelData, Cell, BoundingBox, Event

class LabelPopupPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
        self.model = LabelPopupModel()
        pass

    def refresh(self):
        pass

    def submitData(self, boxID, boxDimensions, newCellIdsToAdd, otherCellIDs, newEventsToAdd, otherEventIDs):
        #convert data to appropriate data types stored in iterable
        boundingBoxes = []
        cellsToAdd = []
        eventsToAdd = []

        for cell in newCellIdsToAdd:
            cellsToAdd.append(Cell(newCellIdsToAdd))

        x = boxDimensions[0]
        y = boxDimensions[1]
        width = boxDimensions[2]
        height = boxDimensions[3]
        frameNumber = 0 #FIXME frame number not set properly
        BoundingBox(boxID, frameNumber, x, y, width, height, cellIDs, eventIDs)

        #submit the appropriate data
        self.model.submitData()
    
    def getCellIDs(self):
        # Retrieve the list of cell IDs
        return list(self.model.data["Cells"].keys())
    
    def getEventIDs(self):
        # Retrieve the list of event IDs
        return list(self.model.data["Events"].keys())

    def getBoundingBoxes(self):
        # Retrieve the bounding boxes
        return self.model.data["BoundingBoxes"]
    
    def getFrames(self):
        # Retrieve the frames
        return self.model.data["Frames"]

    def getMetaData(self):
        # Retrieve the metadata
        return self.model.data["MetaData"]