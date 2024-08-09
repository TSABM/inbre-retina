from PyQt5.QtCore import QRect



class LabelData(dict):
    '''
    dictionary containing the bounding boxes events and metadata for the file
    '''
    def __init__(self):
        self.update({"Cells": dict()})
        self.update({"Events": dict()})
        self.update({"MetaData": MetaData()})

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

class Cell(dict):
    def __init__(self, boxID : str = None, cellID : str = None, frameNumber : int = None, cellType : str = None, xCoord: int = None, yCoord: int = None, width: int = None, height: int = None, events : list = []):
        #defining fields
        super().__init__({
                "boxID" : boxID, 
                "cellID" : cellID,
                "frameNumber" : frameNumber,
                "cellType" : cellType,
                #coordinate and size data for the bounding box
                "boundingBox": [xCoord, yCoord, width, height],
                "associatedEvents" : events #make events able to store multiple cells
                })

    def get_boundingBox_as_rect(self):
        boundingBox = self.get("boundingBox")
        if boundingBox[0] is None:
            return None
        return QRect(boundingBox[0], boundingBox[1], boundingBox[2], boundingBox[3])

class Event(dict):
    def __init__(self, eventID : str, eventType : str, boxIDs : list,):
        # defining fields
        super().__init__({
            "eventID": eventID,
            "eventType": eventType,
            "associatedBoxIDs" : boxIDs
        })