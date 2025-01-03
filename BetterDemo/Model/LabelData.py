from PyQt5.QtCore import QRect



class LabelData(dict):
    '''
    dictionary containing the bounding boxes events and metadata for the file
    '''
    def __init__(self, mediaSourceName : str, maxFrames : int):
        self.update({"MetaData": MetaData(mediaSourceName, maxFrames)})
        #self.update({"BoundingBoxes": dict()})
        self.update({"Cells": dict()})
        self.update({"CellTypes" : dict()})
        self.update({"Events": dict()})
        self.update({"EventTypes" : dict()})
        self.update({"Frames" : dict()})

        self.initFrames(maxFrames)
    
    def addNewData(self, boundingBoxes, cells, events):
        '''
        add or update box, cell, and event data
        '''
        for box in boundingBoxes:
            self.updateBoundingBox(box)
        for cell in cells:
            self.addNewCell(cell)
        for event in events:
            self.addNewEvent(event)

    def getNewBoxID(self):
        largestId = self.getLargestBoxIdVal()
        idNum = largestId + 1
        boxID = "box_" + str(idNum)
        return boxID
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
    def updateBoundingBox(self, box : "BoundingBox"):
        '''
        give a bounding box you want to update, then update the frame and bounding box containers with that box
        '''
        '''
        print("attempting to update frame and boxes with new bounding box")
        #grab the bounding box and frame fields so we can update them
        #boundingBoxes : dict = self.get("BoundingBoxes")
        frames : dict = self.get("Frames")

        #grab the frame the box belongs in
        frame : Frame = frames.get(box.get_frameNumber())
        #verify frame is set
        if frame == None:
            print("Error, couldnt add box: frame number  ", box.get_frameNumber(), " was invalid")
            return
        #add boxid to frame, and update the bounding box dictionary
        frame.addBoxId(box.get_boxID())
        #frames.update({box.get_frameNumber() : frame}) #redunant
        boundingBoxes.update({box.get_boxID() : box})
        '''
        #ok this all needs redone:
        #for a box
        #find its frame
        #place it in the frame
        frames : dict = self.get("Frames")
        currFrameNum = box.get_frameNumber()
        if isinstance(currFrameNum, int):
            currFrame : "Frame" = frames.get(currFrameNum)
            if currFrame == None:
                print("couldnt find frame: ", currFrameNum)
                return
            else:
                print("Frame found, updating box")
                currFrame.updateBoundingBox(box)
        else:
            print("error: box being added did not have a valid frame number: ", currFrameNum)

    def deleteBoundingBox(self, boxID : str):
        #grab the bounding box in question
        boxes : dict = self.getBoundingBoxes()
        box : BoundingBox = boxes.get(boxID)
        
        #verify it still exists
        if box == None: 
            print("Cannot delete box. Box not found in data object")
            return
        
        #remove its reference from the frame
        frames : dict = self.getFrames()
        frame : Frame = frames.get(box.get_frameNumber())
        frameBoxIDs : dict = frame.getBoxIds(boxID)
        del frameBoxIDs[boxID]
        
        #for each event assotiated with it
        events : dict = self.getEvents()
        for eventID in box.get_eventIDs():
            event : Event = events.get(eventID)
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

    def updateMetaData(self, sourceName, frameTotal):
        metadata : "MetaData" = self.get("MetaData")
        metadata.setsourceName(sourceName)
        metadata.setFrameTotal(frameTotal)
        
    def initFrames(self, maxFrames):
        '''
        fill Frames with maxFrames amount of new empty frames
        '''
        #grab a reference to frames data pool
        frames : dict = self.get("Frames")
        #for the range of maxframes define a new frame obejct for each framnumber
        for i in range(maxFrames):
            frames[i] = Frame(i)

    def getFrames(self):
        '''
        returns a dictionary of frame objects (also dictionaries) where the key is the frame number and the val is the frame
        '''
        return self.get("Frames")

    def getFrame(self, frameNum : int):
        frames : dict = self.get("Frames")
        frame = frames.get(frameNum)
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

    def getEvents(self):
        '''
        returns a dictionary of Event objects (also dictionaries) where the key is the eventID and the val is the event
        '''
        return self.get("Events")
    
    def getEventTypes(self):
        return self.get("EventTypes")

    def getMetaData(self):
        return self.get("MetaData")

    def getLargestBoxIdVal(self): #This will need changed, there is no global box storage
        largestValue = 0
        #FIXME
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
    def __init__(self, frameNumber : int, frameID : int = -1, projectName : str = "", projectID : str = "", boundingBoxes : dict = None, maskAnnotations : dict = None):
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
        #FIXME might want to add some checks to be sure I'm ot overriding something I shouldnt be...
        boxes: dict = self.get("boundingBoxes")
        boxID = boundingBox.get_boxID()
        boxes[boxID] = boundingBox
    def getFrameNumber(self):
        return self.get("frameNumber")
    def getBoundingBoxes(self):
        return self.get("boundingBoxes")
    def getProjectId(self):
        return self.get("projectID")
    def setProjectId (self, newID):
        self["projectID"] = newID
    def getProjectName(self):
        return self["projectName"]
    def setProjectName(self, newName):
        self["projectName"] = newName

    
    
class BoundingBox(dict):
    def __init__(self, projectID : int, frameID : int, boxID : str = None, frameNumber : int = None,xCoord: int = None, yCoord: int = None, width: int = None, height: int = None, cellIDs : dict = None, eventIDs : dict = None):
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
    
    def get_boxID(self):
        return self.get("boxID")

    def get_frameNumber(self):
        return self.get("frameNumber")
    
    def getDimensions(self):
        return self.get("dimensions")
    
    def setDimensions(self, x, y, width, height):
        self.update({"dimensions": [x, y, width, height]})
    
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
    def __init__(self, eventID : str, eventType : str, boxIDs : dict):
        # defining fields
        super().__init__({
            "eventID": eventID,
            "eventType": eventType,
            "boxIDs" : boxIDs
            #"cellIDs": cellIds #cellIDs was a dict, but maybe redundant since boxes store the cell list too
        })
    def getEventID(self):
        return self.get("eventID")
    def getEventType(self):
        return self.get("eventType")
    def getBoxIDs(self):
        return self.get("boxIDs")
        
class MetaData(dict): #FIXME need to 
    def __init__(self, sourceName: str, frameTotal: int, maxWidth : int = 0, maxHeight : int = 0, other: list[str] = None, projectName : str = ""):
        # Ensure other is a list if not provided
        if other is None: #May need fixing as it may be unneeded and unreachable
            other = []
        
        # defining fields
        super().__init__({
            "sourceName": sourceName,
            "projectName" : projectName,
            "frameTotal": frameTotal,
            "maxWidth" : maxWidth,
            "maxHeight" : maxHeight,
            "other": other,
        })
    
    def setSourceName(self, sourceName: str) -> None:
        """Set the sourceName in the metadata."""
        self["sourceName"] = sourceName
    
    def setFrameTotal(self, frameTotal: int) -> None:
        """Set the frameTotal in the metadata."""
        self["frameTotal"] = frameTotal
    
    def getSourceName(self):
        """Get the stored sourceName as a string or NONE"""
        return self.get("sourceName")
    
    def getFrameTotal(self):
        return self.get("frameTotal")
    
    def getProjectName(self):
        return self.get("projectName")
    
    def getMaxDimensions(self):
        '''returns [width, height] values will be integer or None'''
        return [self.get("maxWidth"), self.get("maxHeight")]
