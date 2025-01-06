import json
import os
import re
from Model.masterMemory import MasterMemory
from Model.LabelData import LabelData, MetaData

class LabelExporter():
    """Converts label data to JSON and then exports it as a new JSON file"""
    def __init__(self):
        #get all labels
        pass

    def __convertLabelsToJson__(self):
        labelData = MasterMemory.getLabelData()
        json_data = json.dumps(labelData, indent = 4)
        return json_data
    
    def __getFileName__(self):
        labelData : LabelData = MasterMemory.getLabelData()
        metadata : MetaData = labelData.getMetaData()
        fileName : str | None = metadata.getSourceName() #FIXME? remnent from gif days may need to alter for folders?
        
        return fileName


    def export(self, exportFileName : str, destinationPath : str, overwrite : bool = False): 
        """converts label data to JSON and saves that data as a new JSON file"""
        """FIXME instead of having hard dependencies on master mem and label data in this function maybe either pass in labels 
        or have it be a class instance variable ALSO let the user choose the save location instead of hard coding it """
        json_data = self.__convertLabelsToJson__()
        #fileName : str | None = self.__getFileName__()
        
        #if name is not a string
        if not self.__is_valid_filename(exportFileName):
            print("Export error: proposed export filename, " + exportFileName + ",is not valid")
            return
        
        #add on the new file extension
        newFileName = exportFileName + ".json"
        #turn into a full path
        newFilePath = os.path.join(destinationPath, newFileName)
        
        #check if file already exists and then stop the overwrite if not allowed
        if os.path.exists(newFilePath):
            print(f"Warning trying to overwrite '{newFilePath}' which already exists")
            if overwrite == False:
                print("aborting file overwrite")
                return
        
        #write to a file
        try:
            with open(newFilePath, 'w') as json_file:
                json_file.write(json_data)
            print("Data exported successfully")
        except IOError as e:
            print(f"Export error: failed to write to file. {e}")
    
    def __is_valid_filename(self, filename: str) -> bool:
        
        if not isinstance(filename, str):
            print("Given filename is not a string")
            return False
        
        if len(filename) > 200:
            print("filename is too long, limit is 200 chars")
            return False
        
        if not filename or filename in {".", ".."}:
            print("filename is invalid string")
            return False  # Invalid names
    
        # Check for forbidden characters based on the OS
        if os.name == 'nt':  # Windows
            forbidden_chars = r'[<>:"/\\|?*]'
            if re.search(forbidden_chars, filename):
                print("filename contains forbidden character(s)")
                return False
            # Check for reserved names in Windows
            reserved_names = {"CON", "PRN", "AUX", "NUL"} | {f"COM{i}" for i in range(1, 10)} | {f"LPT{i}" for i in range(1, 10)}
            if filename.split('.')[0].upper() in reserved_names:  # Ignore extensions for reserved names
                print("filename is a reserved file name on windows systems")
                return False
            
        elif "/" in filename:  # POSIX (Linux/macOS)
            return False
    
        return True