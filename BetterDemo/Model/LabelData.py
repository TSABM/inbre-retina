from PyQt5.QtCore import QRect



class LabelData(dict):
    '''
    dictionary containing the bounding boxes events and metadata for the file
    '''
    def __init__(self):
        self.update({"Frames" : dict()})
        self.update({"BoundingBoxes": dict()})
        self.update({"Cells": dict()})
        self.update({"CellTypes" : dict()})
        self.update({"Events": dict()})
        self.update({"EventTypes" : dict()})
        self.update({"MetaData": MetaData()})
    
    def addNewData(self, boundingBoxes, cells, events):
        for box in boundingBoxes:
            self.addNewBoundingBox(box)
        for cell in cells:
            self.addNewCell(cell)
        for event in events:
            self.addNewEvent(event)

    def addNewBoundingBox(self, box : "BoundingBox"):
        boundingBoxes : dict = self.get("BoundingBoxes")
        frames : dict = self.get("Frames")
        #verify type
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
            #grab id and record box in frame
            boxID = box.get_boxID()
            frame.addBoxId(boxID)
            #grab box event(s) and record in the frame
            eventIDs = box.get_eventIDs()
            for event in eventIDs:
                frame.addEventId(event)
            #store updated frame (in case it only updated locally)
            frames.update({frameNum : frame})
            #add the bounding box
            boundingBoxes.update({box.get_boxID() : box})

    def addNewCellType(self, type : str):
        '''
        adds new cell type to the dict of existing cell types. the key is the Type (which is a string), a boolean "True" is stored as the value
        '''
        cellTypes : dict = self.get("CellTypes")
        cellTypes.update({type : True})
    
    def addNewEventType(self, type : str):
        '''
        adds new event type to dict. The key is the type (a string) and the value is a boolean
        '''
        eventTypes : dict = self.get("EventTypes")
        eventTypes.update({type : True})

    def addNewCell(self, cell : "Cell"):
        cells: dict = self.get("Cells")
        cells.update({cell.get("cellID"): cell})

    def addNewEvent(self, event : "Event"):
        events: dict = self.get("Events")
        events.update({event.get("eventID"): event})

    def updateMetaData(self):
        print("UPDATEMETADATA UNIMPLEMENTED")
        pass
    
    def getFrames(self):
        '''
        returns a dictionary of frame objects (also dictionaries) where the key is the frame number and the val is the frame
        '''
        return self.get("Frames")

    def getBoundingBoxes(self):
        '''
        returns a dictionary of bounding box objects (also dictionaries) where the key is the boxID and the val is the box itself
        '''
        return self.get("BoundingBoxes")

    def getCells(self):
        '''
        returns a dictionary of Cell objects (also dictionaries) where the key is the cellID and the val is the cell
        '''
        return self.get("Cells")

    def getCellTypes(self):
        return self.get("CellTypes")

    def getEvents(self):
        '''
        returns a dictionary of Event objects (also dictionaries) where the key is the eventID and the val is the event
        '''
        return self.get("Events")
    
    def getEventTypes(self):
        return self.get("EventTypes")

    def getMetaData(self):
        return self.get("MetaData")

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
        if boxId in boxIds: #if the boxID is already stored just return
            return
        boxIds[boxId] = True
    
    def addEventId(self, eventId):
        eventIds: dict = self.get("eventIDs")
        if eventId in eventIds:
            return
        eventIds[eventId] = True

class BoundingBox(dict):
    def __init__(self, boxID : str = None, frameNumber : int = None,xCoord: int = None, yCoord: int = None, width: int = None, height: int = None, cellIDs : dict = None, eventIDs : dict = None):
        if cellIDs is None:
            cellIDs = {}
        if eventIDs is None:
            eventIDs = {}
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
    
    def get_boxID(self):
        return self.get("boxID")

    def get_frameNumber(self):
        return self.get("frameNumber")
    
    def getDims(self):
        return self.get("dimensions")
    
    def get_cellIDs(self):
        return self.get("cellIds")

    def get_eventIDs(self):
        return self.get("eventIDs")
    
    def updateBox(self, frameNumber : int = None, xCoord: int = None, yCoord: int = None, 
               width: int = None, height: int = None, cellIDsToAdd : dict = None, eventIdsToAdd : dict = None):
        '''
        update the box info
        '''
        #if a frame number is provided update the stored frame number
        if frameNumber is not None:
            self["frameNumber"] = frameNumber
        #if dimensions are provided update them (but only update the provided dims)
        if xCoord is not None or yCoord is not None or width is not None or height is not None:
            dimensions = self["dimensions"]
            self["dimensions"] = [
                xCoord if xCoord is not None else dimensions[0],
                yCoord if yCoord is not None else dimensions[1],
                width if width is not None else dimensions[2],
                height if height is not None else dimensions[3]
            ]
        #if cellIds are provided update the dict. Note this method will technically override duplicate entries
        if cellIDsToAdd is not None:
            self["cellIDs"].update(cellIDsToAdd)
        #if an event is provided update the dict. Note this will technically override events with duplicate event keys
        if eventIdsToAdd:
            self["eventIDs"].update(eventIdsToAdd)
    
    def addCell(self, cellID):
        self["cellIDs"].update({cellID : True})

    def addEvent(self, eventID):
        self["eventIDs"].update({eventID : True})

class Cell(dict):
    def __init__(self, cellID : str, cellType : str):
        super().__init__({
            "cellID" : cellID,
            "cellType" : cellType
        })

class Event(dict):
    def __init__(self, eventID : str, eventType : str, boxIDs : dict):
        # defining fields
        super().__init__({
            "eventID": eventID,
            "eventType": eventType,
            "boxIDs" : boxIDs
            #"cellIDs": cellIds #cellIDs was a dict, but maybe redundant since boxes store the cell list too
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