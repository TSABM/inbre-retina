from PyQt5.QtCore import QRect



class Label(dict):
    '''
    A rectangular box which "labels" or indicates the presence of something. Also contains data about what the object being labelled is.
    '''
    def __init__(self, frameNumber: int, rectangle : QRect, type: str, itemID: str, description: str = ""):
        self.frameNumber : int = frameNumber
        self.rectangle : QRect = rectangle
        self.itemId : str = itemID
        self.type : str = type
        self.description : str = description

class BoundingBox(dict):
    def __init__(self):
        super().__init__()

        #defining fields
        boxID : list[int] = []
        cellID : list[int] = []
        frameNumber : list[int] = []
        cellType : list[str] = []

        #adding to dict
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
    def __init__():
        super().__init__()

        #defining fields

        #adding to dict
