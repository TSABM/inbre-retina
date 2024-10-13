import os
from Model.masterMemory import MasterMemory
#from Model.nd2FileAccessor import ND2FileAccessor
from Model.CanvasModel import CanvasModel
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage
from Model.AcceptedFormats.SimpleMovie import SimpleMovie

class WindowMenuBarModel():
    def __init__(self):
        pass

    def openImage(self, imagePath):
        imageName = os.path.basename(imagePath)
        #check the file format

        #if gif or other like format
        if ".gif" in imagePath or ".mng" in imagePath or ".apng" in imagePath:
            acceptedFormat = SimpleMovie(imageName)
            if acceptedFormat.setMovie(imagePath) == True:
                #send to canvas?
                canvas = MasterMemory.getCanvas()
                canvas.setFile(acceptedFormat)
                pass
            else:
                pass
            pass
        #if jpeg, png, or jpg
        elif ".jpeg" in imagePath or ".png" in imagePath or ".jpg" in imagePath:
            print("jpeg, png, and jpg opening is unimplemented")
            pass

        else:
            pass
        '''
        #open file at image location
        file =  
        #place file in memory
        MasterMemory.setOpenFile(file)
        #convert to QImage compatable format
        frame = file.grabcurrentFrame()

        #Return QImage to presenter where it can be sent off to the master memory and view
        return frame
        '''
        

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