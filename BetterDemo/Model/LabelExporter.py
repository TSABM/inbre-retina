import json
import os
from Model.masterMemory import MasterMemory
from LabelData import LabelData, MetaData

class LabelExporter():
    """Converts label data to JSON and then exports it as a new JSON file"""
    def __init__():
        #get all labels
        pass

    def __convertLabelsToJson__():
        labelData = MasterMemory.getAllLabels()
        json_data = json.dumps(labelData, indent = 4)
        return json_data
    
    def __getFileName__():
        labelData : LabelData = MasterMemory.getLabelData()
        metadata : MetaData = labelData.getMetaData()
        fileName : str | None = metadata.getFileName()
        
        return fileName


    def export(self): 
        """converts label data to JSON and saves that data as a new JSON file"""
        """FIXME instead of having hard dependencies on master mem and label data in this function maybe either pass in labels 
        or have it be a class instance variable ALSO let the user choose the save location instead of hard coding it """
        json_data = self.__convertLabelsToJson__()
        fileName : str | None = self.__getFileName__()
        
        #if name is not a string
        if not isinstance(fileName, str):
            print("Export error: open file has no filename")
            return
        
        #just in case remove any existing file extension
        name, extension = os.path.splitext(fileName)
        #add on the new file extension
        newFileName = name + "_exportedViewerData.json"
        
        #check if file already exists
        if os.path.exists(newFileName):
            print(f"Warning: overwriting '{newFileName}' which already exists")
            #return
        
        #write to a file
        try:
            with open(newFileName, 'w') as json_file:
                json_file.write(json_data)
            print("Data exported successfully")
        except IOError as e:
            print(f"Export error: failed to write to file. {e}")