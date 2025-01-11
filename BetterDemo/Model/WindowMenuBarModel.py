import os
from Model.masterMemory import MasterMemory
#from Model.nd2FileAccessor import ND2FileAccessor
from Model.CanvasModel import CanvasModel
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage
from Model.AcceptedFormats.SimpleMovie import SimpleMovie
from Model.AcceptedFormats.StandardImage import StandardImage

class WindowMenuBarModel():
    def __init__(self):
        pass

    def openImage(self, imagePath, projectName : str):
        '''
        opens a single image or "simple movie" (such as a gif) and creates a data object to hold annotation info
        '''
        imageName = os.path.basename(imagePath)
        #check the file format

        #if gif or other like format
        if ".gif" in imagePath or ".mng" in imagePath or ".apng" in imagePath:
            acceptedFormat = SimpleMovie(imageName)
            if acceptedFormat.setMovie(imagePath) == True:
                #send to canvas?
                canvas : CanvasModel= MasterMemory.getCanvas() # type: ignore
                canvas.setSource(acceptedFormat, projectName, None)
            else:
                pass
            pass
        #if jpeg, png, or jpg
        elif ".jpeg" in imagePath or ".png" in imagePath or ".jpg" in imagePath or ".bmp" in imagePath or ".ppm" in imagePath or ".tiff" in imagePath:
            acceptedFormat = StandardImage(imageName)
            if acceptedFormat.setImage(imagePath) == True:
                canvas : CanvasModel = MasterMemory.getCanvas() # type: ignore
                canvas.setSource(acceptedFormat, projectName, None)
        else:
            pass
        
    def openProject(self):
        #FIXME I need to be defined!
        pass

    def filterFileList(self, fileList):
        '''
        filters a list of files and returns jpeg, jpg, and png files
        '''
        print("filtering for jpeg, jpg, and png")

        filteredList = []
        for file in fileList:
            if ".jpeg" in file or ".png" in file or ".jpg" in file:
                filteredList.append(file)
        #print(filteredList)
        return filteredList