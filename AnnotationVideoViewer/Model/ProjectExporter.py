import json
import os
import re
import shutil
from Model.masterMemory import MasterMemory
from Model.LabelData import LabelData, MetaData, Frame

class ProjectExporter():
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
        fileName : str | list[str] = metadata.getSourceField() #FIXME? remnent from gif days may need to alter for folders?
        
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

    def __createProjectFolder__(self, projectPath) -> bool:
        if os.path.isdir(projectPath):  # Check if it's a folder
            print(f"Folder already exists: {projectPath}")
            return False
        self.__createFolder__(projectPath)
        return True

    def __createAnnotationFile__(self, overwrite : bool, projectDestinationPath):
        annotationPath = os.path.join(projectDestinationPath, "annotations.json")

        ##stop any overwrites if not allowed
        if os.path.exists(annotationPath):
            print(f"Warning trying to overwrite '{annotationPath}' which already exists")
            if overwrite == False:
                print("aborting file overwrite")
                return 
        ##jsonify data
        json_data = self.__convertLabelsToJson__()
        ##write annotation file
        self.__writeJsonFile__(json_data, annotationPath)

    def __createSource__(self, sourcePath, projectDestinationPath):
        #create new source folder path
        newSourceFilePath = os.path.join(projectDestinationPath, "source")
        #create a folder for the frame
        self.__createFolder__(newSourceFilePath)
        #save source image(s) to the new folder
        #FIXME
        if os.path.isfile(sourcePath):
            #only dealing with a single image/video copy it to the new source folder
            try:
                shutil.copy(sourcePath, newSourceFilePath)
            except FileNotFoundError:
                print(f"Source file not found: {sourcePath}")
            except PermissionError:
                print(f"Permission denied: Unable to copy to {newSourceFilePath}")
            except Exception as e:
                print(f"An error occurred: {e}")
        
        elif os.path.isdir(sourcePath):
            #dealing with a folder... need to verify that it keeps the folder of images format
            #ensure it has nothing but images
            #all images are the same type (jpeg, jpeg, etc)
            #possibly that they follow some naming convetions (named by frame or something)
            print("designated source is a folder not a file. Folder based graphic copying is not completed")
        pass
    
    def __updateProjectName__(self, projectPath : str):
        labelData = MasterMemory.getLabelData()
        if isinstance(labelData, LabelData):
            metadata = labelData.getMetaData()
            sourceName = os.path.basename(projectPath)
            metadata.setProjectName(sourceName)

    def export(self, projectDestinationPath : str, overwrite : bool = False): 
        """converts label data to JSON and saves that data as a new JSON file"""
        """FIXME instead of having hard dependencies on master mem and label data in this function maybe either pass in labels 
        or have it be a class instance variable ALSO let the user choose the save location instead of hard coding it """
        sourcePath : str = MasterMemory.getSourcePath()
        #check if source exists
        if self.__check_path__(sourcePath):
            self.__updateProjectName__(projectDestinationPath)

            self.__createProjectFolder__(projectDestinationPath)

            self.__createAnnotationFile__(overwrite, projectDestinationPath)

            self.__createSource__(sourcePath, projectDestinationPath)
        else:
            print("cannot export file, source image/video cannot be found with the given path: ", sourcePath)
        return

    
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
    
    def __check_path__(self, path) -> bool:
        if os.path.exists(path):  # Check if the path exists
            if os.path.isfile(path):  # Check if it's a file
                print(f"The path exists and is a file: {path}")
                return True
            elif os.path.isdir(path):  # Check if it's a folder
                print(f"The path exists and is a folder: {path}")
                return True
            else:  # Something exists, but it's neither a file nor a folder (e.g., symbolic link)
                print(f"The path exists but is not a regular file or folder: {path}")
                return False
        else:
            print(f"The path does not exist: {path}")
            return False