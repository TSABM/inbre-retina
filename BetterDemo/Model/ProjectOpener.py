import os
import json
from Model.masterMemory import MasterMemory
from Model.LabelData import LabelData
from Model.MetaData import MetaData
#from pydantic import BaseModel
class ProjectOpener():
    def __init__(self, projectPath):
        self.projectPath = projectPath
        pass
    
    def __verifyProject__(self) -> bool:
        verified : bool = True
        #take project folder
        #inside should be a file named annotation(s)? verify this
        annotationPath = self.projectPath + "/annotations.json"
        if not os.path.isfile(annotationPath):
            print("annotations.json does not exist on path: ", annotationPath)
            verified = False
        #inside should be a folder named source verify this
        sourcePath = self.projectPath + "/source"
        if not os.path.isdir(sourcePath):
            print("source directory does not exist on path: ", sourcePath)
            verified = False
            #inside that folder should be 1 or more images of an accepted format. for now only one image is supported.
            if not os.listdir(sourcePath):
                print("The source directory is empty the project cannot load without a supported image or video")
                verified = False
        return verified

    def validateData(self, data):
        if not isinstance(data, dict):
            print("json data is not a dictionary, cannot parse")
            return
        metaData = data.get("MetaData")
        if metaData == None: print("metaData could not be found"); return
        if not MetaData.validate_structure(metaData): print("imported metaData did not match expected structure"); return
        #verify dict
        #for cell in cells: Cell.validate_structure(cell)
        #verify dict
        #for cellType in cellTypes: validate is string
        #verify dict
        #for event in events: Event.validate_structure(event)
        #verify dict
        #for eventType in eventTypes: validate is string
        #verify dict
        #for frame in Frames: Frame.validate_structure(frame)

    def openProject(self):
        '''
        take a potential folder, verify it meets format and open
        '''
        #verify the project
        if self.__verifyProject__():
            #init label data
            #set current image
            #open annotations into label data
            annotationPath = self.projectPath + "/annotations.json"
            with open(annotationPath, "r") as file:
                loaded_data : dict = json.load(file)
        #FIXME validate data integrity. ideally in a LabelData class so changes made there arent lost
        self.val
        #FIXME read the data into a label data object
        #FIXME set master mems label data as this label data possibly through the canvas?
        else:
            print("could not verify the project structure")
            pass

    def extractLabels():
        pass