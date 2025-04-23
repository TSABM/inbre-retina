from Model.Annotation import Annotation
class Frame(dict):
    def __init__(self, frameNumber : int, frameID : int,imageSource : str, annotations : dict | None = None):
        if annotations is None: #note this is important, if you just have the class line = {} when not specified it creates a global dict shared by all frames
            annotations = {}  # Create a new dictionary for each instance
        super().__init__({
            #using dictionaries instead of lists so adding and searching is more efficient.
            #"projectID" : projectID,
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
    def getFrameNumber(self) -> int:
        return self["frameNumber"]
    def getFrameAnnotations(self) -> dict[int, "Annotation"]:
        return self["annotations"]
    def getAnnotationKeys(self):
        boundingBoxes : dict = self["annotations"]
        if boundingBoxes == None:
            return None
        return boundingBoxes.keys()
    #def getProjectId(self):
    #    return self.get("projectID")
    def getImageSource(self)->str:
        return self["imageSource"]
    
    def setFrameID(self, newID):
        self["frameID"] = newID
    #def setProjectId (self, newID):
    #    self["projectID"] = newID
    
    @classmethod
    def from_dict(cls, data: dict) -> "Frame":
        annotations = {
            int(anno_id): Annotation.from_dict(anno_data)
            for anno_id, anno_data in data.get("annotations", {}).items()
        }

        return cls(
            frameNumber=data["frameNumber"],
            frameID=data["frameID"],
            #projectID=data["projectID"],
            imageSource=data["imageSource"],
            annotations=annotations
        )
