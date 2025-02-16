import os
import json
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

    #init label data
        #read outer directory
        #read metadata
        #

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
                loaded_data = json.load(file)
                #FIXME see if maybe pydantic can check if the loaded data matches the labelData spec if so we can just load it in directly
            pass
        else:
            print("could not verify the project structure")
            pass

    def extractLabels():
        pass