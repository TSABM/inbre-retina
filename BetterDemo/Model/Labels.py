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

class Events(dict):
    def __init__(self):
        super().__init__()

class MetaData():
    def __init__(self):
        #defining fields
        self.fileInfo : str = None
        self.frameTotal : int = None
        self.other : list[str] = []

class BoundingBox():
    def __init__(self, boxID  = None, cellID = None, frameNumber = None, cellType = None):
        #defining fields
        self.boxID : int = boxID
        self.cellID : int = cellID
        self.frameNumber : int = frameNumber
        self.cellType : str = cellType

class Event():
    def __init__(self, eventID = None, type = None):
        self.eventID = eventID
        self.type = type