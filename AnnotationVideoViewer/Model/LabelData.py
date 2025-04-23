from PyQt5.QtCore import QRect
from collections.abc import Iterable
import random
from Model.MetaData import MetaData
from Model.Frame import Frame
from Model.Event import Event
from Model.Cell import Cell
from Model.Annotation import Annotation


class LabelData(dict):
    '''
    dictionary containing the bounding boxes events and metadata for the file
    '''
    def __init__(self, mediaSourceName : str | None = None, maxFrames : int | None = None, projectName : str | None = None, projectID : int | None = None, rawData : dict | None = None): #FIXME right now this class is incompatable with opening existing label datas
        if rawData != None:
            self.readInData(rawData)
        else:    
            if mediaSourceName == None or maxFrames ==None or projectName == None:
                print("tried to init label data but somethign want initalized")
                return
            if projectID == None:
                projectID = self.generateNewProjectId()
            self.update({"MetaData": MetaData(mediaSourceName, maxFrames, projectID, projectName)})
            self.update({"Cells": dict()})
            self.update({"CellTypes" : dict()})
            self.update({"Events": dict()})
            self.update({"EventTypes" : dict()})
            self.update({"Frames" : dict()})

            #if maxFrames == None: #deprocated, pretty sure this needs removing
            #    maxFrames = len(self["Frames"])
            self.initFrames(maxFrames) #FIXME
    
    def readInData(self, rawData : dict):
        '''takes data in generic formats and turns into LabelData'''
        #metadata
        rawMetadata = rawData["MetaData"]
        metaData = MetaData.from_dict(rawMetadata)
        
        #cells
        rawCells : dict[int, dict] = rawData["Cells"]
        cells = {}
        for cellID, rawCell in rawCells.items():
            cell : Cell = Cell.from_dict(rawCell)
            cells.update({cellID : cell})
        
        # Cell Types
        rawCellTypes : dict = rawData["CellTypes"]
        cellTypes = {}
        for rawCellType in rawCellTypes.keys():
            cellTypes[rawCellType] = rawCellType

        # Events
        rawEvents : dict = rawData["Events"]
        events = {}
        for eventID, rawEvent in rawEvents.items():
            event: Event = Event.from_dict(rawEvent)
            events[eventID] = event

        # Event Types
        rawEventTypes : dict = rawData["EventTypes"]
        eventTypes = {}
        for rawEventType in rawEventTypes.keys():
            eventTypes[rawEventType] = rawEventType

        # Frames
        rawFrames = rawData["Frames"]
        frames = {}
        for frameID in rawFrames.keys():
            convertedFrame = Frame.from_dict(rawFrames[frameID])
            frames[int(frameID)] = convertedFrame
            #check if frame cell  details are loaded in cells, if not fix this
            annotations = convertedFrame.getFrameAnnotations()
            for annotationKey in annotations:
                cellID = annotations[annotationKey].get_cellID()
                cellType = annotations[annotationKey].get_cellType()
                if cellID != None and cellType != None:
                    if cells.get(cellID) == None:
                        cells[cellID] = Cell(cellID, cellType)
                    if cellTypes.get(cellType) == None:
                        cellTypes[cellType] = cellType

        # Update the dictionary with the parsed data
        self.update({
            "MetaData": metaData,
            "Cells": cells,
            "CellTypes": cellTypes,
            "Events": events,
            "EventTypes": eventTypes,
            "Frames": frames
        })

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
                frames[i] = Frame(i, i, imageSource) #for now te frameID will also just be the frame number. This may need to be changed later
            
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
                frames[i] = Frame(i, i, frameSource) #for now te frameID will also just be the frame number. This may need to be changed later    
        else:
            #something went wrong
            print("tried to assign image source to the frame but the image source was of an unknown type")
            print("imageSource type: ", type(imageSource))

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

    def generateNewProjectId(self) -> int:
        '''returns a 1-4 digit project ID'''
        random_number = random.randint(0, 5000)
        return random_number

    def getNewAnnotationID(self) -> int:
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
            #annotationType = annotation.getAnnotationType()
            self.updateFrameWithAnnotation(id, frameNum, cellID, cellType, maskPoints)
        for cell in cells:
            self.addNewCell(cell)
        for event in events:
            self.addNewEvent(event)
    
    def updateFrameWithAnnotation(self, annotationID : int,  frameNumber : int, cellID : int, cellType : str, maskPoints : list):
        #metadata : MetaData = self.getMetaData()
        frames : dict = self.getFrames()
        #currFrameNum = box.get_frameNumber()
        #projectID = metadata.getProjectID()
        
        if isinstance(frameNumber, int):
            if frameNumber in frames:
                currFrame : "Frame" = frames[frameNumber]
                if not isinstance(currFrame, Frame):
                    print("error tried to update a box in frame but given frame number is type: ", type(currFrame))
                    return
                else:
                    print("Frame found, updating box")
                    #frameID : int = currFrame.getFrameID()
                    box : Annotation = Annotation(annotationID, frameNumber, cellID, cellType, maskPoints)
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
        
        #check the events dir and delete the one that relates to the deleted annotation
        events : dict[int, Event] = self.getEvents()
        toDeleteID = annotationToDelete.get_eventID()
        if isinstance(toDeleteID, int):
            del events[toDeleteID]
            
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
           
    def getLargestBoxIdVal(self) -> int: #FIXME change this no longer should those ID's worry about collisions
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

    @classmethod
    def validate_structure(cls, data: dict) -> bool:
        """
        Validates if a dictionary matches the expected structure of LabelData.

        Args:
            data (dict): The dictionary to validate.

        Returns:
            bool: True if the structure matches, False otherwise.
        """
        # Define the required top-level keys
        required_keys = {"MetaData", "Cells", "CellTypes", "Events", "EventTypes", "Frames"}
        
        # Check if all required keys exist in the data
        for key in required_keys:
            if key not in data:
                print(f"Missing key: {key}")
                return False

        # Check if there are extra keys in the dictionary
        extra_keys = set(data.keys()) - required_keys
        if extra_keys:
            print(f"Extra keys found: {extra_keys}")
            return False

        # Validate MetaData structure if MetaData is a dict
        if isinstance(data.get("MetaData"), dict):
            if not MetaData.validate_structure(data["MetaData"]):
                print("MetaData structure is invalid.")
                return False
        else:
            print("MetaData is not a dictionary.")
            return False

        # Ensure other keys are dictionaries
        for key in ["Cells", "CellTypes", "Events", "EventTypes", "Frames"]:
            if not isinstance(data.get(key), dict):
                print(f"{key} is not a dictionary.")
                return False

        return True

    

