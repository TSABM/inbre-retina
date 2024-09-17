from PyQt5.QtCore import QRect



class LabelData(dict):
    '''
    dictionary containing the bounding boxes events and metadata for the file
    '''
    def __init__(self):
        self.update("BoundingBoxes", dict())
        self.update("Events", dict())
        self.update("MetaData", MetaData())
    
<<<<<<< HEAD
    @classmethod
    def from_dict(cls, data):
        #FIXME need to extract data and convert to subclasses...
=======
    def addNewBoxLabel(self, BoundingBoxes, Cells, Events):
        for box in BoundingBoxes:
            self.addNewBoundingBox()

    def addNewBoundingBox(self, box):
        boundingBoxes : dict = self.get("BoundingBoxes")
        frames : dict = self.get("Frames")
        #verify type
        if type(box) is not BoundingBox:
            print("Error, cannot add bounding box of type: " + type(box).__name__)
        else:
            frameNum : int = box.get("frameNumber")
            frame : Frame = frames.get(frameNum)
            #verify frameNum is a valid number
            if frameNum is not None:
                try:
                    frameNum = int(frameNum)
                except ValueError:
                    print("Error: frameNumber is not a valid integer")
                    return
            #verify frame is set
            if frame == None:
                print("Error, couldnt add box: frame number %d was invalid", frameNum)
            else:
                #update the frames box list
                frame.get("")
                frames.update({frameNum : })
                #add the bounding box
                boundingBoxes.update({box.get("boxID") : box})
            
        
    
    def addNewCell(self, cell):
        cells: dict = self.get("Cells")
        if not isinstance(cell, Cell):
            print("Error, cannot add cell of type: " + type(cell).__name__)
        else:
            cells.update({cell.get("cellID"): cell})

    def addNewEvent(self, event):
        events: dict = self.get("Events")
        if not isinstance(event, Event):
            print("Error, cannot add event of type: " + type(event).__name__)
        else:
            events.update({event.get("eventID"): event})

    def updateMetaData(self):
>>>>>>> parent of a85f780 (updated id storage, now fixing circular import)
        pass

<<<<<<< HEAD
=======
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
            #using dictionaries instead of lists so adding and searching is more efficient. 
            "boxIDs": {},  # Initialize as an empty dictionary
            "eventIDs": {}  # Initialize as an empty dictionary
        })
    
    def addBoxId(self, boxId):
        boxIds: dict = self.get("boxIDs")
        if boxId in boxIds:
            return
        boxIds[boxId] = True
    
    def addEventId(self, eventId):
        eventIds: dict = self.get("eventIDs")
        if eventId in eventIds:
            return
        eventIds[eventId] = True



class BoundingBox(dict):
    def __init__(self, boxID : str = None, frameNumber : int = None,xCoord: int = None, yCoord: int = None, width: int = None, height: int = None, cellIDs : list = None, eventIDs : list = None):
        if cellIDs is None:
            cellIDs = []
        if eventIDs is None:
            eventIDs = []
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
    
    def updateBox(self, frameNumber : int = None, xCoord: int = None, yCoord: int = None, 
               width: int = None, height: int = None, cellIDsToAdd : list = [], eventIdsToAdd : list = []):
        if frameNumber is not None:
            self["frameNumber"] = frameNumber
        if xCoord is not None or yCoord is not None or width is not None or height is not None:
            # Only update the dimensions that are provided
            dimensions = self["dimensions"]
            self["dimensions"] = [
                xCoord if xCoord is not None else dimensions[0],
                yCoord if yCoord is not None else dimensions[1],
                width if width is not None else dimensions[2],
                height if height is not None else dimensions[3]
            ]
        if cellIDsToAdd:
            self["cellIDs"].extend(cellIDsToAdd)
        if eventIdsToAdd:
            self["eventIDs"].extend(eventIdsToAdd)
    
    def addCell(self, cellID):
        self["cellIDs"].append(cellID)

    def addEvent(self, eventID):
        self["eventIDs"].append(eventID)

class Cell(dict):
    def __init__(self, cellID : str, cellType : str):
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
>>>>>>> parent of a85f780 (updated id storage, now fixing circular import)
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