import json
import os
import re
import shutil
from Model.masterMemory import MasterMemory
from Model.LabelData import LabelData, MetaData, Frame

class LabelExporter():
    """Converts label data to JSON and then exports it as a new JSON file"""
    def __init__(self):
        #get all labels
        pass

    def __convertLabelsToJson__(self):
        labelData = MasterMemory.getLabelData()
        json_data = json.dumps(labelData, indent = 4)
        return json_data
    
    def __extractFrameJson__(self, frameData) -> None | str:
        if frameData == None:
            print("tried to convert an invalid frame to json")
            return None
        else:
            json_frame_data = json.dumps(frameData, indent = 4)
            return json_frame_data

    def __getFileName__(self):
        labelData : LabelData = MasterMemory.getLabelData() # type: ignore
        metadata : MetaData = labelData.getMetaData()
        fileName : str | None = metadata.getSourceName() #FIXME? remnent from gif days may need to alter for folders?
        
        return fileName

    def __writeJsonFile__(self, jsonData : str, filePath : str):
        try:
            with open(filePath, 'w') as json_file:
                json_file.write(jsonData)
            print("Data exported successfully")
        except IOError as e:
            print(f"Export error: failed to write to file. {e}")

    def __createFolder__(self, folderDestinationPath):
        # Create the folder
        os.makedirs(folderDestinationPath, exist_ok=True)

    def export(self, annotationsFileName : str, projectDestinationPath : str, sourceImagePath : str, overwrite : bool = False): 
        """converts label data to JSON and saves that data as a new JSON file"""
        """FIXME instead of having hard dependencies on master mem and label data in this function maybe either pass in labels 
        or have it be a class instance variable ALSO let the user choose the save location instead of hard coding it """
        
        ##validate new file and path name
        if not self.__is_valid_projectname(annotationsFileName):
            print("Export error: proposed annotations filename, " + annotationsFileName + ",is not valid")
            return
        
        ##add on the new file extension
        newFileName = annotationsFileName + ".json"
        #turn into a full path
        newFilePath = os.path.join(projectDestinationPath, newFileName)

        ##create folder
        self.__createFolder__(projectDestinationPath)
        
        ##save frame data (hmm how to do this...)
            #save main annotations
            #save frame folders
            #in frame folders save image and frame annotations

        ##jsonify data
        json_data = self.__convertLabelsToJson__()
        
        ##stop any overwrites if not allowed
        if os.path.exists(newFilePath):
            print(f"Warning trying to overwrite '{newFilePath}' which already exists")
            if overwrite == False:
                print("aborting file overwrite")
                return
        
        ##write annotation file
        self.__writeJsonFile__(json_data, newFilePath)

        ## copy over image data
        labelData : LabelData = MasterMemory.getLabelData() # type: ignore
        frameData :dict[int, Frame] = labelData.getFrames()
        for frame in frameData.values():
            #create new framefolder path
            frameFilePath = os.path.join(newFilePath, str(frame.getFrameNumber()))
            #create a folder for the frame
            self.__createFolder__(frameFilePath)
            #extract framejson
            frameJson = self.__extractFrameJson__(frame)
            if frameJson == None:
                pass
            else:
                #verify image exists
                    #if it exists use shutil to copy the image to the new directory
                #save both to a frame subfolder in project
                self.__writeJsonFile__(frameJson, frameFilePath)

    
    def __is_valid_projectname(self, projectname: str) -> bool:
        
        if not isinstance(projectname, str):
            print("Given projectname is not a string")
            return False
        
        if len(projectname) > 200:
            print("projectname is too long, limit is 200 chars")
            return False
        
        if not projectname or projectname in {".", ".."}:
            print("projectname is invalid string")
            return False  # Invalid names
    
        # Check for forbidden characters based on the OS
        if os.name == 'nt':  # Windows
            forbidden_chars = r'[<>:"/\\|?*]'
            if re.search(forbidden_chars, projectname):
                print("projectname contains forbidden character(s)")
                return False
            # Check for reserved names in Windows
            reserved_names = {"CON", "PRN", "AUX", "NUL"} | {f"COM{i}" for i in range(1, 10)} | {f"LPT{i}" for i in range(1, 10)}
            if projectname.split('.')[0].upper() in reserved_names:  # Ignore extensions for reserved names
                print("projectname is a reserved file name on windows systems")
                return False
            
        elif "/" in projectname:  # POSIX (Linux/macOS)
            return False
    
        return True