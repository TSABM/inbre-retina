from PyQt5.QtCore import QRect



class Labels(dict):
    '''
    dictionary containing the bounding boxes events and metadata for the file
    '''
    def __init__(self):
        self.update("BoundingBoxes", BoundingBoxes())
        self.update("Events", Events())
        self.update("MetaData", MetaData())

class BoundingBoxes(dict):
    def __init__(self):
        super().__init__()

        #key boxID, cellID, frameNumber
        frames : dict[int] = dict()
        
        #defining fields
        boxIDs : list[int] = []
        cellIDs : list[int] = []
        frameNumbers : list[int] = []
        cellTypes : list[str] = []

        #adding to dict
        #fix this below. If order is not guranteed storing boxid cellid frame number and celltype all seperately would result in a jumble
        self.update("boxIDs", boxIDs)
        self.update("cellIDs", cellIDs)
        self.update("frameNumbers", frameNumbers)
        self.update("cellTypes", cellTypes)

class Events(dict):
    def __init__(self):
        super().__init__()

        #defining fields
        eventIDs : list[int] = []
        types : list[str] = []

        #adding to dict
        self.update("eventID", eventIDs)
        self.update("type", types)

class MetaData(dict):
    def __init__(self):
        super().__init__()

        #defining fields
        fileInfo : str = None
        frameTotal : int = None
        other : list[str] = []

        #adding to dict
        self.update("fileInfo", fileInfo)
        self.update("frameTotal", frameTotal)
        self.update("other", other)
