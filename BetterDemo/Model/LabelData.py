from PyQt5.QtCore import QRect



class LabelData(dict):
    '''
    dictionary containing the bounding boxes events and metadata for the file
    '''
    def __init__(self):
        self.update({"Frames" : dict()})
        self.update({"BoundingBoxes": dict()})
        self.update({"Cells": dict()})
        self.update({"Events": dict()})
        self.update({"MetaData": MetaData()})
    
    def generateNewLabel(self, ):
        #generate bounding box
        #cells
        #events
        #metadata
        pass

    def getLargestBoxIdVal(self):
        largestValue = 0
        boxes : dict = self.get("BoundingBoxes")
        for key in boxes.keys():
            if not isinstance(key, str):
                print("error bounding box key is not a string")
                return None
            else:
                x = key.split('_')[1]
                x = int(x)
                if x > largestValue:
                    largestValue = x
        return largestValue

class Frame(dict):
    def __init__(self):
        super().__init__({
            "boxIDs" : []
        })


class BoundingBox(dict):
    def __init__(self, boxID : str = None, frameNumber : int = None,xCoord: int = None, yCoord: int = None, width: int = None, height: int = None, cellIDs : list = [], eventIDs : list = []):
        #defining fields
        super().__init__({
                "boxID" : boxID, 
                "frameNumber" : frameNumber,
                "dimensions": [xCoord, yCoord, width, height],
                "cellIds" : cellIDs,
                "eventIDs" : eventIDs
                })

    def get_boundingBox_as_rect(self):
        boundingBox = self.get("boundingBox")
        if boundingBox[0] is None:
            return None
        return QRect(boundingBox[0], boundingBox[1], boundingBox[2], boundingBox[3])

class Cell(dict):
    def __init__(cellID : str, cellType : str):
        super().__init__({
            "cellID" : cellID,
            "cellType" : cellType
        })

class Event(dict):
    def __init__(self, eventID : str, eventType : str, boxID : str, cellIds : list):
        # defining fields
        super().__init__({
            "eventID": eventID,
            "eventType": eventType,
            "boxID" : boxID,
            "cellIDs": cellIds
        })
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