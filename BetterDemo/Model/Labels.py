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

        #defining fields
        boxID : list[int] = []
        cellID : list[int] = []
        frameNumber : list[int] = []
        cellType : list[str] = []

        #adding to dict
        #fix this below. If order is not guranteed storing boxid cellid frame number and celltype all seperately would result in a jumble
        self.update("boxID", boxID)
        self.update("cellID", cellID)
        self.update("frameNumber", frameNumber)
        self.update("cellType", cellType)

class Events(dict):
    def __init__(self):
        super().__init__()

        #defining fields
        eventID : list[int] = []
        type : list[str] = []

        #adding to dict
        self.update("eventID", eventID)
        self.update("type", type)

class MetaData(dict):
    def __init__(self):
        super().__init__()

        #defining fields
        fileInfo : list[str] = []
        frameTotal : int = None
        other : list[str] = []

        #adding to dict
        self.update("fileInfo", fileInfo)
        self.update("frameTotal", frameTotal)
        self.update("other", other)
