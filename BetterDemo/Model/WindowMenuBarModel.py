import os
from Model.masterMemory import MasterMemory
from Model.nd2FileAccessor import ND2FileAccessor
from Model.Canvas import Canvas
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage


class WindowMenuBarModel():
    def __init__(self):
        pass

    def openImage(self, imagePath):
        #open file at image location
        file = ND2FileAccessor(imagePath) #FIXME currently frame index is just none, handle this better.
        #place file in memory
        MasterMemory.setOpenFile(file)
        #convert to QImage compatable format
        frame = file.grabcurrentFrame()
        #determine number of channels
        #FIXME grab metadata properly and judge based on that.
        height, width, channels = frame.shape #Note: this might not work, its making an assumption on array structure...
        #if 3, rgb
        if channels == 3:
            qimage = QImage(frame.data, width, height, 3 * width, QImage.Format_RGB888)
        #if 4, rgba
        elif channels == 4:
            qimage = QImage(frame.data, width, height, 4 * width, QImage.Format_RGBA8888)
        #if 1, grayscale
        elif channels == 1:
            qimage = QImage(frame.data, width, height, width, QImage.Format_Grayscale8)
        #else, error
        else:
            raise ValueError("Unsupported number of channels: {}".format(channels))

        #Return QImage to presenter where it can be sent off to the master memory and view
        return qimage
        

    def openFolder(self, directoryPath):
        '''
        FIXME returns the contents of a selected folder
        '''
        #ensure the path isnt empty
        if(directoryPath == ""):
            print("Empty path detected, no file/folder selected")
        else:
            #open folder
            files = os.listdir(directoryPath)
            #now filter out all files of incompatable types
            filteredFiles = self.filterFileList(files)
            #now update the filtered files to include the whole path
            fullPathFiles = []
            for file in filteredFiles:
                filePath = directoryPath + "/" + file
                fullPathFiles.append(filePath)
            #now return the filtered list
            return fullPathFiles

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