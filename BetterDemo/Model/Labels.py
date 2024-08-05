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

class MetaData(dict):
    def __init__(self, fileInfo: str = None, frameTotal: int = None, other: list[str] = None):
        # Ensure other is a list if not provided
        if other is None: #May need fixing as it may be unneeded and unreachable
            other = []
        
        # defining fields
        super().__init__({
            "fileInfo": fileInfo,
            "frameTotal": frameTotal,
            "other": other,
        })

class BoundingBox(dict):
    def __init__(self, boxID : int = None, cellID : int = None, frameNumber : int = None, cellType : str = None, xCoord : int = None, yCoord : int = None, width : int = None, height : int = None, events : list = None):
        #defining fields
        super().__init__({
                "boxID" : boxID, 
                "cellID" : cellID,
                "frameNumber" : frameNumber,
                "cellType" : cellType,
                #coordinate and size data for the bounding box
                "coordsAndDims" : [xCoord, yCoord, width, height],
                "associatedEvents" : []
                })

class Event(dict):
    def __init__(self, eventID : int, eventType : str, boxID : int,):
        # defining fields
        super().__init__({
            "eventID": eventID,
            "eventType": eventType,
            "associatedBoxID" : boxID
        })