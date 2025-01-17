from PyQt5.QtCore import QRect
from collections.abc import Iterable
import random


class LabelData(dict):
    '''
    dictionary containing the bounding boxes events and metadata for the file
    '''
    def __init__(self, mediaSourceName : str, maxFrames : int, projectName : str, projectID : int | None = None): #FIXME right now this class is incompatable with opening existing label datas
        if projectID == None:
            projectID = self.generateNewProjectId()
        self.update({"MetaData": MetaData(mediaSourceName, maxFrames, projectID, projectName)})
        self.update({"Cells": dict()})
        self.update({"CellTypes" : dict()})
        self.update({"Events": dict()})
        self.update({"EventTypes" : dict()})
        self.update({"Frames" : dict()})

        self.initFrames(maxFrames) #FIXME
    
    def generateNewProjectId(self) -> int:
        '''returns a 1-4 digit project ID'''
        random_number = random.randint(0, 5000)
        return random_number

    def addNewData(self, boundingBoxes : Iterable["BoundingBox"], cells, events):
        '''
        add or update box, cell, and event data
        '''
        for box in boundingBoxes:
            id = box.get_boxID()
            frameNum = box.get_frameNumber()
            [x, y, w, h] = box.getDimensions()
            self.updateFrameWithBox(id, frameNum, x, y, w, h)
        for cell in cells:
            self.addNewCell(cell)
        for event in events:
            self.addNewEvent(event)

    def getNewBoxID(self) -> int:
        metadata : MetaData = self["MetaData"]
        largestID : int = metadata.getLargestID()
        if largestID == -1:
            largestId = self.getLargestBoxIdVal()
        newID = largestId + 1
        return newID
    '''
    def addNewBoundingBox(self, boxID : str, frameNumber : int, dims : QRect, cellIDs : dict = None, eventIDs : dict = {}):
        boundingBoxes : dict = self.get("BoundingBoxes")
        frames : dict = self.get("Frames")
        rect = dims.getRect()

        frame : Frame = frames.get(frameNumber)
        #verify frame is set
        if frame == None:
            print("Error, couldnt add box: frame number  ", frameNumber, " was invalid")
            return
        
        frame.addBoxId(boxID)
        for event in eventIDs.keys():
            frame.addEventId(event)
        frames.update({frameNumber : frame})
        boundingBoxes.update({boxID : BoundingBox(boxID, frameNumber, rect[0], rect[1], rect[2], rect[3], cellIDs, eventIDs)})
    '''
    def updateFrameWithBox(self, boxId : int, frameNumber : int, x : int, y : int, w : int, h : int):
        metadata : MetaData = self.getMetaData()
        frames : dict = self.getFrames()
        #currFrameNum = box.get_frameNumber()
        projectID = metadata.getProjectID()
        
        if isinstance(frameNumber, int):
            currFrame : "Frame" = frames[frameNumber]
            if currFrame == None:
                print("couldnt find frame: ", frameNumber)
                return
            else:
                print("Frame found, updating box")
                frameID : int = currFrame.getFrameID()
                box : BoundingBox = BoundingBox(projectID, frameID, boxId, frameNumber, x, y, w, h)
                currFrame.updateBoundingBox(box)
        else:
            print("error: box being added did not have a valid frame number: ", frameNumber)

    def deleteBoundingBox(self, boxID : int, frameKey : int):
        #grab the bounding box in question
        #boxes : dict = self.getBoundingBoxes()
        #box : BoundingBox = boxes.get(boxID)
        frames : dict = self.getFrames()
        frame : Frame = frames[frameKey]
        boxes : dict = frame.getBoundingBoxes()
        boxToDelete : BoundingBox = boxes[boxID]
        
        #verify it still exists
        if boxToDelete == None: 
            print("Cannot delete box. Box not found in data object")
            return
        
        #remove its reference from the frame
        #frames : dict = self.getFrames()
        #frame : Frame = frames.get(boxToDelete.get_frameNumber())
        #frameBoxIDs : dict = frame.getBoxIds(boxID)
        #del frameBoxIDs[boxID]
        
        #for each event assotiated with it
        events : dict[int, Event] = self.getEvents()
        for eventID in boxToDelete.get_eventIDs():
            event : Event = events[eventID]
            if event == None:
                print("tried to find an event in events to remove it but could not find it")
                return
            #remove the assotiation with the box being deleted
            eventBoxIds : dict = event.getBoxIDs()
            del eventBoxIds[eventID]
            #if the event has no box assotiated then delete it
            if len(eventBoxIds) == 0:
                del events[eventID]
            
        #delete the bounding box
        del boxes[boxID]
        print("deleted bounding box")

    def addNewCellType(self, type : str):
        '''
        adds new cell type to the dict of existing cell types. the key is the Type (which is a string), a boolean "True" is stored as the value
        '''
        cellTypes : dict = self["CellTypes"]
        cellTypes.update({type : True})
    
    def addNewEventType(self, type : str):
        '''
        adds new event type to dict. The key is the type (a string) and the value is a boolean
        '''
        eventTypes : dict = self["EventTypes"]
        eventTypes.update({type : True})

    def addNewCell(self, cell : "Cell"):
        cells: dict = self["Cells"]
        cells.update({cell.get("cellID"): cell})

    def addNewEvent(self, event : "Event"):
        events: dict = self["Events"]
        events.update({event.get("eventID"): event})

    def updateMetaData(self, sourceName, frameTotal):
        metadata : "MetaData" = self["MetaData"]
        metadata.setSourceName(sourceName)
        metadata.setFrameTotal(frameTotal)
        
    def initFrames(self, maxFrames):
        '''
        fill Frames with maxFrames amount of new empty frames
        '''
        metadata : MetaData = self.getMetaData()
        if metadata == None:
            print("metadata was uninitalized when frames were being initalized")
        projectName : str = metadata.getProjectName()
        projectID : int = metadata.getProjectID()
        #grab a reference to frames data pool
        frames : dict = self["Frames"]
        #for the range of maxframes define a new frame obejct for each framnumber
        for i in range(maxFrames):
            frames[i] = Frame(i, i, projectID, projectName) #for now te frameID will also just be the frame number. This may need to be changed later

    def getFrames(self) -> dict:
        '''
        returns a dictionary of frame objects (also dictionaries) where the key is the frame number and the val is the frame
        '''
        return self["Frames"]

    def getFrame(self, frameNum : int) -> "Frame | None":
        frames : dict = self["Frames"]
        frame : Frame | None = frames.get(frameNum)
        if frame == None:
            print("Tried to grab frame (",frameNum, ") that does not exist")
        return frame

    
    #def getBoundingBoxes(self):
    #    '''
    #    returns a dictionary of bounding box objects (also dictionaries) where the key is the boxID and the val is the box itself
    #    '''
    #    return self.get("BoundingBoxes")
    

    def getCells(self):
        '''
        returns a dictionary of Cell objects (also dictionaries) where the key is the cellID and the val is the cell
        '''
        return self.get("Cells")

    def getCellTypes(self):
        return self.get("CellTypes")

    def getEvents(self) -> dict:
        '''
        returns a dictionary of Event objects (also dictionaries) where the key is the eventID and the val is the event
        '''
        return self["Events"]
    
    def getEventTypes(self):
        return self.get("EventTypes")

    def getMetaData(self) -> "MetaData":
        return self["MetaData"]

    def getLargestBoxIdVal(self) -> int:
        '''
        checks the project ID, frameIDs, and boxIDs and returns the largest of them
        '''
        metadata : MetaData = self["MetaData"]
        frames : dict[int, Frame] = self["Frames"]
        largestID : int = metadata.getLargestID()
        #check projectID
        projID : int = metadata.getProjectID()
        if projID > largestID:
            largestID = projID
        #check each frames id and boxIDs
        for frame in frames.values():
            frameLargest = 0
            #check frameID's
            frameID = frame.getFrameID()
            if frameID > frameLargest: frameLargest = frameID
            #check boxKeys
            boxKeys = frame.getBoxKeys()
            if isinstance(boxKeys, Iterable):
                if not boxKeys: #aka if empty
                    pass
                else:
                    largestBoxKey = max(boxKeys)
                    if largestBoxKey > frameLargest: frameLargest = largestBoxKey
            else:
                if boxKeys == None: print("Could not get boxIds from a frame got None instead from frame: ", frame.getFrameNumber())
                else: print("unknown error occured when grabbing box keys for frame number: ", frame.getFrameNumber())
                break
            #compare frame largest to global largest
            if frameLargest > largestID: largestID = frameLargest
        
        return largestID

class Frame(dict):
    def __init__(self, frameNumber : int, frameID : int, projectID : int, projectName : str = "", boundingBoxes : dict | None = None, maskAnnotations : dict | None = None):
        if boundingBoxes is None: #note this is important, if you just have the class line = {} when not specified it creates a global dict shared by all frames
            boundingBoxes = {}  # Create a new dictionary for each instance
        super().__init__({
            #using dictionaries instead of lists so adding and searching is more efficient.
            "projectID" : projectID,
            "frameID" : frameID,
            "frameNumber" : frameNumber,
            "projectName" : projectName,
            "boundingBoxes": boundingBoxes,  # Initialize as an empty dictionary
            "maskAnnotations" : maskAnnotations
        })
    
    def updateBoundingBox(self, boundingBox : "BoundingBox"):
        #FIXME this is no longer valid way of getting bounding boxes. It must be frame based
        boxes: dict = self["boundingBoxes"]
        boxID = boundingBox.get_boxID()
        boxes[boxID] = boundingBox
    def getFrameID(self) -> int:
        return self["frameID"]
    def getFrameNumber(self):
        return self.get("frameNumber")
    def getBoundingBoxes(self) -> dict[int, "BoundingBox"]:
        return self["boundingBoxes"]
    def getBoxKeys(self):
        boundingBoxes : dict = self["boundingBoxes"]
        if boundingBoxes == None:
            return None
        return boundingBoxes.keys()
    def getProjectId(self):
        return self.get("projectID")
    def getProjectName(self):
        return self["projectName"]
    
    def setFrameID(self, newID):
        self["frameID"] = newID
    def setProjectId (self, newID):
        self["projectID"] = newID
    def setProjectName(self, newName):
        self["projectName"] = newName

    
    
class BoundingBox(dict):
    def __init__(self, projectID : int, frameID : int, boxID : int , frameNumber : int | None = None, xCoord: int | None = None, yCoord: int | None = None, width: int | None = None, height: int | None = None, cellIDs : dict | None = None, eventIDs : dict | None = None):
        if cellIDs is None:
            cellIDs = {}
        if eventIDs is None:
            eventIDs = {}
        #defining fields
        super().__init__({
                "projectID" : projectID,
                "frameID" : frameID,
                "boxID" : boxID, 
                "frameNumber" : frameNumber,
                "dimensions": [xCoord, yCoord, width, height],
                "cellIds" : cellIDs,
                "eventIDs" : eventIDs
                })

    def get_boundingBox_as_qrect(self):
        dimensions = self.get("dimensions")
        if dimensions is None:
            return None
        return QRect(dimensions[0], dimensions[1], dimensions[2], dimensions[3])
    
    def get_boxID(self) -> int:
        return self["boxID"]

    def get_frameNumber(self) -> int:
        return self["frameNumber"]
    
    def getDimensions(self) -> list:
        return self["dimensions"]
    
    def setDimensions(self, x, y, width, height):
        self.update({"dimensions": [x, y, width, height]})
    
    def get_cellIDs(self) -> dict:
        return self["cellIds"]

    def get_eventIDs(self) -> dict:
        return self["eventIDs"]
    
    def updateBox(self, frameNumber : int | None = None, xCoord: int | None = None, yCoord: int | None = None, 
               width: int | None = None, height: int | None = None, cellIDsToAdd : dict | None = None, eventIdsToAdd : dict | None = None):
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

class MaskAnnotation(dict):
    def __init__(self, projectID: int, frameID: int, created_by: str, creationTimestamp: str, approved: bool, values: dict):
        super().__init__({
            "projectID": projectID,
            "frameID": frameID,
            "created_by": created_by,
            "creationTimestamp": creationTimestamp,
            "approved": approved,
            "values": values
        })

    # Getter and setter for projectID
    def get_projectID(self) -> int:
        return self["projectID"]

    def set_projectID(self, projectID: int) -> None:
        self["projectID"] = projectID

    # Getter and setter for frameID
    def get_frameID(self) -> int:
        return self["frameID"]

    def set_frameID(self, frameID: int) -> None:
        self["frameID"] = frameID

    # Getter and setter for created_by
    def get_created_by(self) -> str:
        return self["created_by"]

    def set_created_by(self, created_by: str) -> None:
        self["created_by"] = created_by

    # Getter and setter for creationTimestamp
    def get_creationTimestamp(self) -> str:
        return self["creationTimestamp"]

    def set_creationTimestamp(self, creationTimestamp: str) -> None:
        self["creationTimestamp"] = creationTimestamp

    # Getter and setter for approved
    def get_approved(self) -> bool:
        return self["approved"]

    def set_approved(self, approved: bool) -> None:
        self["approved"] = approved

    # Getter and setter for values
    def get_values(self) -> dict:
        return self["values"]

    def set_values(self, values: dict) -> None:
        self["values"] = values

class Cell(dict):
    def __init__(self, cellID : str, cellType : str):
        super().__init__({
            "cellID" : cellID,
            "cellType" : cellType
        })

class Event(dict):
    def __init__(self, eventID : int, eventType : str, boxIDs : dict):
        # defining fields
        super().__init__({
            "eventID": eventID,
            "eventType": eventType,
            "boxIDs" : boxIDs
            #"cellIDs": cellIds #cellIDs was a dict, but maybe redundant since boxes store the cell list too
        })
    def getEventID(self) -> int:
        return self["eventID"]
    def getEventType(self):
        return self.get("eventType")
    def getBoxIDs(self) -> dict:
        return self["boxIDs"]
        
class MetaData(dict): #FIXME need to 
    def __init__(self, sourceName: str, frameTotal: int, projectID : int, projectName : str, maxWidth : int = 0, maxHeight : int = 0, other: list[str] | None = None):
        # Ensure other is a list if not provided
        if other is None:
            other = []
        
        # defining fields
        super().__init__({
            "sourceName": sourceName,
            "projectName" : projectName,
            "projectID" : projectID,
            "frameTotal": frameTotal,
            "maxWidth" : maxWidth,
            "maxHeight" : maxHeight,
            "largestID" : -1,
            "other": other,
        })
    
    def setSourceName(self, sourceName: str) -> None:
        """Set the sourceName in the metadata."""
        self["sourceName"] = sourceName
    
    def setProjectID(self, projectID : int) -> None:
        self["projectID"] = projectID
    
    def setFrameTotal(self, frameTotal: int) -> None:
        """Set the frameTotal in the metadata."""
        self["frameTotal"] = frameTotal
    
    def setLargestID(self, largestID : int):
        self["largestID"] = largestID
    
    def getSourceName(self):
        """Get the stored sourceName as a string or NONE"""
        return self.get("sourceName")
    
    def getFrameTotal(self) -> int:
        return self["frameTotal"]
    
    def getProjectID(self) -> int:
        return self["projectID"]
    
    def getProjectName(self) -> str:
        return self["projectName"]
    
    def getMaxDimensions(self):
        '''returns [width, height] values will be integer or None'''
        return [self.get("maxWidth"), self.get("maxHeight")]
    
    def getLargestID(self):
        return self["largestID"]
