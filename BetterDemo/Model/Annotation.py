class Annotation(dict):
    def __init__(self, projectID : int, annotationID : int , annotationType : str, frameNumber : int, cellID : int, 
                 cellType : str, mask : list | None = None, eventID : int = -1, prevAnnoId : int = -1, nextAnnoId : int = -1,
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
                "previousAnnotationID" : prevAnnoId,
                "nextAnnotationID" : nextAnnoId,
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
    
    def get_prev_anno_id(self) -> int:
        return self["previousAnnotationID"]
    
    def set_prev_anno_id(self, newPrevID : int):
        self["previousAnnotationID"] = newPrevID

    def get_next_anno_id(self) -> int:
        return self["nextAnnotationID"]
    
    def set_next_anno_id(self, nextID : int):
        self["nextAnnotationID"] = nextID

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

