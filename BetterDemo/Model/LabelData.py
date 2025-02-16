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
    
    def initFrames(self, maxFrames):
        '''
        fill Frames with maxFrames amount of new empty frames
        '''
        metadata : MetaData = self.getMetaData()
        if metadata == None:
            print("metadata was uninitalized when frames were being initalized")
        #projectName : str = metadata.getProjectName()
        projectID : int = metadata.getProjectID()
        #grab a reference to frames data pool
        frames : dict = self["Frames"]
        imageSource : str | list[str] = metadata.getSourceField()
        if isinstance(imageSource, str):
            #for the range of maxframes define a new frame obejct for each framnumber
            for i in range(maxFrames):
                frames[i] = Frame(i, i, projectID, imageSource) #for now te frameID will also just be the frame number. This may need to be changed later
            
        elif isinstance(imageSource, list):
            #verify you get a string 
            if all(isinstance(item, str) for item in imageSource):
                print("verified source contents")
            #if not throw an error
            else:
                print("image source has contents other than the accepted types, ")
            for i in range(maxFrames):
                frameSource = ""
                if isinstance(imageSource[i], str):
                    frameSource = imageSource[i]
                else:
                    print("WARNING somehow a frame source of type: ", type(imageSource[i]), " has been loaded into metadata.")
                    raise(TypeError("Cannot set frames source to a type other than string"))
                frames[i] = Frame(i, i, projectID, frameSource) #for now te frameID will also just be the frame number. This may need to be changed later    
        else:
            #something went wrong
            print("tried to assign image source to the frame but the image source was of an unknown type")
            print("imageSource type: ", type(imageSource))

    def generateNewProjectId(self) -> int:
        '''returns a 1-4 digit project ID'''
        random_number = random.randint(0, 5000)
        return random_number

    def getNewBoxID(self) -> int:
        metadata : MetaData = self["MetaData"]
        largestID : int = metadata.getLargestID()
        if largestID == -1:
            largestId = self.getLargestBoxIdVal()
        newID = largestId + 1
        return newID

    def addNewData(self, annotations : Iterable["Annotation"], cells, events, imageSource):
        '''
        add or update box, cell, and event data
        '''
        for annotation in annotations:
            id = annotation.get_annotationID()
            frameNum = annotation.get_frameNumber()
            cellID = annotation.get_cellID()
            cellType = annotation.get_cellType()
            maskPoints = annotation.getMask()
            annotationType = annotation.getAnnotationType()
            self.updateFrameWithAnnotation(id, annotationType, frameNum, cellID, cellType, maskPoints, imageSource)
        for cell in cells:
            self.addNewCell(cell)
        for event in events:
            self.addNewEvent(event)
    
    def updateFrameWithAnnotation(self, annotationID : int, annotationType : str,  frameNumber : int, cellID : int, cellType : str, maskPoints : list, imageSource : str):
        metadata : MetaData = self.getMetaData()
        frames : dict = self.getFrames()
        #currFrameNum = box.get_frameNumber()
        projectID = metadata.getProjectID()
        
        if isinstance(frameNumber, int):
            if frameNumber in frames:
                currFrame : "Frame" = frames[frameNumber]
                if not isinstance(currFrame, Frame):
                    print("error tried to update a box in frame but given frame number is type: ", type(currFrame))
                    return
                else:
                    print("Frame found, updating box")
                    frameID : int = currFrame.getFrameID()
                    box : Annotation = Annotation(projectID, annotationID, annotationType, frameNumber, cellID, cellType, maskPoints)
                    currFrame.updateAnnotation(box)
            else:
                print("Tried to update frame with box data, couldnt find frame: ", frameNumber)
                return
        else:
            print("error: box being added did not have a valid frame number: ", frameNumber)

    def deleteAnnotation(self, boxID : int, frameKey : int):
        #grab the bounding box in question
        #boxes : dict = self.getBoundingBoxes()
        #box : BoundingBox = boxes.get(boxID)
        frames : dict = self.getFrames()
        frame : Frame = frames[frameKey]
        annotations : dict = frame.getFrameAnnotations()
        annotationToDelete : Annotation = annotations[boxID]
        
        #verify it still exists
        if annotationToDelete == None: 
            print("Cannot delete annotation. Annotation not found in data object")
            return
        
        #for each event assotiated with it
        events : dict[int, Event] = self.getEvents()
        del events[annotationToDelete.get_eventID()]
            
        #delete the annotation
        del annotations[boxID]
        print("deleted bounding box")

    def addNewCellType(self, type : str):
        '''
        adds new cell type to the dict of existing cell types. the key is the Type (which is a string), a boolean "True" is stored as the value
        '''
        cellTypes : dict = self["CellTypes"]
        cellTypes.update({type : type})
    
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
        metadata.setSourceField(sourceName)
        metadata.setFrameTotal(frameTotal)
           
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
            boxKeys = frame.getAnnotationKeys()
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
    def __init__(self, frameNumber : int, frameID : int, projectID : int,imageSource : str, annotations : dict | None = None):
        if annotations is None: #note this is important, if you just have the class line = {} when not specified it creates a global dict shared by all frames
            annotations = {}  # Create a new dictionary for each instance
        super().__init__({
            #using dictionaries instead of lists so adding and searching is more efficient.
            "projectID" : projectID,
            "imageSource" : imageSource,
            "frameID" : frameID,
            "frameNumber" : frameNumber,
            "annotations": annotations,  # Initialize as an empty dictionary
        })
    
    def updateAnnotation(self, annotations : "Annotation"):
        #FIXME this is no longer valid way of getting bounding boxes. It must be frame based
        boxes: dict = self["annotations"]
        boxID = annotations.get_annotationID()
        boxes[boxID] = annotations
    def getFrameID(self) -> int:
        return self["frameID"]
    def getFrameNumber(self):
        return self.get("frameNumber")
    def getFrameAnnotations(self) -> dict[int, "Annotation"]:
        return self["annotations"]
    def getAnnotationKeys(self):
        boundingBoxes : dict = self["annotations"]
        if boundingBoxes == None:
            return None
        return boundingBoxes.keys()
    def getProjectId(self):
        return self.get("projectID")
    
    def setFrameID(self, newID):
        self["frameID"] = newID
    def setProjectId (self, newID):
        self["projectID"] = newID

    
class Annotation(dict):
    def __init__(self, projectID : int, annotationID : int , annotationType : str, frameNumber : int, cellID : int, 
                 cellType : str, mask : list | None = None, eventID : int = -1, 
                 created_by : str | None = None, creationTimestamp : str |None = None, approved : bool = False ):
        #defining fields
        super().__init__({
                "projectID" : projectID,
                #"frameID" : frameID,
                "annotationID" : annotationID,
                "frameNumber" : frameNumber,
                "annotationType" : annotationType, #current types "Box", or "Contour" FIXME make this better than strings
                "mask": mask,
                "cellId" : cellID,
                "cellType" : cellType,
                "eventID" : eventID,
                "created_by": created_by,
                "creationTimestamp": creationTimestamp,
                "approved": approved,
                })
    
    def get_annotationID(self) -> int:
        return self["annotationID"]

    def get_frameNumber(self) -> int:
        return self["frameNumber"]
    
    def getMask(self) -> list:
        return self["mask"]
    
    def setMask(self, newMask):
        self.update({"mask": newMask})
    
    def get_cellID(self) -> int:
        return self["cellId"]
    
    def get_cellType(self) -> str:
        return self["cellType"]

    def get_eventID(self) -> int:
        return self["eventID"]
    
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
    
    def getAnnotationType(self) -> str:
        return self["annotationType"]
class Cell(dict):
    def __init__(self, cellID : str, cellType : str):
        super().__init__({
            "cellID" : cellID,
            "cellType" : cellType
        })

class Event(dict):
    def __init__(self, eventID : int, eventType : str, annotationIDs : list):
        # defining fields
        super().__init__({
            "eventID": eventID,
            "eventType": eventType,
            "annotationIDs" : annotationIDs
        })
    def getEventID(self) -> int:
        return self["eventID"]
    def getEventType(self):
        return self.get("eventType")
    def getAnnotationIDs(self) -> list:
        return self["annotationIDs"]
        
class MetaData(dict): #FIXME need to 
    def __init__(self, source: list[str] | str, frameTotal: int, projectID : int, projectName : str, maxWidth : int = 0, maxHeight : int = 0, other: list[str] | None = None):
        # Ensure other is a list if not provided
        if other is None:
            other = []
        
        # defining fields
        super().__init__({
            "projectName" : projectName,
            "projectID" : projectID,
            "source": source, #sometimes there should be multiple source files... change this maybe to a list in that case? Or default to some other value? 
            "frameTotal": frameTotal,
            "maxWidth" : maxWidth,
            "maxHeight" : maxHeight,
            "largestID" : -1,
            "other": other,
        })
    
    def setSourceField(self, source: str | list[str]) -> None:
        """Set the source in the metadata."""
        self["source"] = source

    def setProjectID(self, projectID : int) -> None:
        self["projectID"] = projectID
    
    def setFrameTotal(self, frameTotal: int) -> None:
        """Set the frameTotal in the metadata."""
        self["frameTotal"] = frameTotal
    
    def setLargestID(self, largestID : int):
        self["largestID"] = largestID
    
    def getSourceField(self) -> str | list[str]:
        """Get the stored source as a string or list[str]"""
        return self["source"]
    
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
    
    @classmethod
    def from_dict(cls, data: dict) -> "MetaData":
        """
        Convert a dictionary into a MetaData object.
        
        Args:
            data (dict): The dictionary containing the metadata fields.
        
        Returns:
            MetaData: An instance of MetaData.
        """
        # Extract the required fields from the dictionary and set default values if missing
        source = data.get("source", [])
        frameTotal = data.get("frameTotal", 0)
        projectID = data.get("projectID", 0)
        projectName = data.get("projectName", "")
        maxWidth = data.get("maxWidth", 0)
        maxHeight = data.get("maxHeight", 0)
        other = data.get("other", [])
        
        # Return an instance of MetaData
        return cls(source, frameTotal, projectID, projectName, maxWidth, maxHeight, other)
