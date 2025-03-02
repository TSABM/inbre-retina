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
    
    @classmethod
    def from_dict(cls, data: dict) -> "Event":
        return cls(
            eventID=data["eventID"],
            eventType=data["eventType"],
            annotationIDs=data.get("annotationIDs", [])  # Default to empty list if missing
        )
        

