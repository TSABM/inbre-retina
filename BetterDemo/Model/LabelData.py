from PyQt5.QtCore import QRect



class LabelData(dict):
    '''
    dictionary containing the bounding boxes events and metadata for the file
    '''
    def __init__(self):
        self.update("BoundingBoxes", dict())
        self.update("Events", dict())
        self.update("MetaData", MetaData())
    
    @classmethod
    def from_dict(cls, data):
        #FIXME need to extract data and convert to subclasses...
        pass

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
    def __init__(self, boxID : str = None, cellID : str = None, frameNumber : int = None, cellType : str = None, rectangle : QRect = None, events : list = None):
        #defining fields
        super().__init__({
                "boxID" : boxID, 
                "cellID" : cellID,
                "frameNumber" : frameNumber,
                "cellType" : cellType,
                #coordinate and size data for the bounding box
                "rectangle" : rectangle,
                "associatedEvents" : []
                })

class Event(dict):
    def __init__(self, eventID : str, eventType : str, boxID : str,):
        # defining fields
        super().__init__({
            "eventID": eventID,
            "eventType": eventType,
            "associatedBoxID" : boxID
        })