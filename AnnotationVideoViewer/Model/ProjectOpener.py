import os
import json
from Model.masterMemory import MasterMemory
from Model.LabelData import LabelData
from Model.MetaData import MetaData
from Model.AcceptedFormats.SimpleMovie import SimpleMovie
from Model.AcceptedFormats.SimpleVideo import SimpleVideo
from Model.AcceptedFormats.StandardImage import StandardImage
from Model.CanvasModel import CanvasModel

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

    def __validateData__(self, data):
        if not isinstance(data, dict):
            print("json data is not a dictionary, cannot parse")
            return
        if LabelData.validate_structure(data):
            print("validated dictionary against label data structure")
            return True
        else:
            print("could not validate data against LabelData structure")
            return False

    def convertLabelData(self, data : dict) -> LabelData:
        labelData = LabelData(None, None, None, None, data)
        return labelData

    def openProject(self):
        '''
        take a potential folder, verify it meets format and open
        '''
        #verify the project
        if self.__verifyProject__():
            print("project structure verified checking annotation data")
            #init label data
            #set current image
            #open annotations into label data
            annotationPath = self.projectPath + "/annotations.json"

            with open(annotationPath, "r") as file:
                loaded_data : dict = json.load(file)
            #validate data integrity. ideally in a LabelData class so changes made there arent lost
            if self.__validateData__(loaded_data):
                #read the data into a label data object and load into master mem
                readInData : LabelData = self.convertLabelData(loaded_data)
                MasterMemory.setLabelData(readInData)
                
                #load source video/image into accepted source object, then set in master memory
                metaData = readInData.getMetaData()
                graphicSource : str | list[str] = metaData.getSourceField()
                if isinstance(graphicSource, str):
                    print("attempting to bind single file source")
                    fullSourcePath = self.projectPath + "/source/" + graphicSource
                    acceptedFormat = self.bindSourceFormat(fullSourcePath)
                    if (acceptedFormat == None):
                        print("couldnt bind source to accepted format")
                        return
                    MasterMemory.setSourcePath(fullSourcePath) #stores the full source path so the exporter does not have to re-create it if grabbing image from foreign folder to project structure
                    canvas : CanvasModel | None = MasterMemory.getCanvas()
                    if isinstance(canvas, CanvasModel):
                        canvas.primeCanvas(acceptedFormat)
                    else:
                        print("error canvas isnt set properly so I cant open the project")
                else:
                    print("trying to bind multi image source from existing project")
                    print("FIXME this feature isnt ready yet")
            else:
                print("annotation data did not match aborting")
        else:
            print("could not verify the project structure")
            pass

    def bindSourceFormat(self, path):
        imageName = os.path.basename(path)
        if ".gif" in path or ".mng" in path or ".apng" in path:
            acceptedFormat = SimpleMovie(imageName)
            if acceptedFormat.setMovie(path) == True:
                return acceptedFormat
        elif ".jpeg" in path or ".png" in path or ".jpg" in path or ".bmp" in path or ".ppm" in path or ".tiff" in path:
            acceptedFormat = StandardImage(imageName)
            if acceptedFormat.setImage(path) == True:
                return acceptedFormat
        elif ".mp4":
            acceptedFormat = SimpleVideo(imageName)
            if acceptedFormat.setMovie(path) == True:
                return acceptedFormat
        return None