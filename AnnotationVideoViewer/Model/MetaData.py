class MetaData(dict): #FIXME need to 
    def __init__(self, source: list[str] | str, frameTotal: int, projectID : int, projectName : str, width : int = 0, height : int = 0):
        
        # defining fields
        super().__init__({
            "projectName" : projectName,
            "projectID" : projectID,
            "source": source, #sometimes there should be multiple source files... change this maybe to a list in that case? Or default to some other value? 
            "frameTotal": frameTotal,
            "width" : width,
            "height" : height,
            "largestID" : -1
        })
    
    def setProjectName(self, name : str):
        self["projectName"] = name

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
        return [self.get("width"), self.get("height")]
    
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
        
        # Return an instance of MetaData
        return cls(source, frameTotal, projectID, projectName, maxWidth, maxHeight)
    
    @classmethod
    def validate_structure(cls, data: dict) -> bool:
        """
        Validate if the given dictionary matches the structure of MetaData.

        Args:
            data (dict): The dictionary to validate.

        Returns:
            bool: True if the structure matches, False otherwise.
        """
        # Define the expected structure and types
        expected_structure = {
            "projectName": str,
            "projectID": int,
            "source": (str, list),  # Accept string or list of strings
            "frameTotal": int,
            "width": int,
            "height": int,
            "largestID": int,
        }

        # Check if all required keys are present
        for key, expected_type in expected_structure.items():
            if key not in data:
                print(f"Missing key: {key}")
                return False
            if not isinstance(data[key], expected_type):
                print(f"Incorrect type for key '{key}': Expected {expected_type}, got {type(data[key])}")
                return False

        return True