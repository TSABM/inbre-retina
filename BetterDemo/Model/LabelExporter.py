import json
from Model.masterMemory import MasterMemory

class LabelExporter():
    def __init__():
        #get all labels
        pass

    def __convertLabelsToJson__():
        labelData = MasterMemory.getAllLabels()
        json_data = json.dumps(labelData, indent = 4)
        return json_data
    
    def __getFileName__():
        #get the origional files name
        #add _labels.json
        fileName = "test1.json"
        return fileName

    def export(self):
        json_data = self.__convertLabelsToJson__()
        fileName : str = self.__getFileName__()
        #write to a file
        with open(fileName, 'w') as json_file: #FIXME check for already saved file
            json_file.write(json_data)
        print("data exported")