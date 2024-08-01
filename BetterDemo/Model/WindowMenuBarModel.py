import os
from Model.masterMemory import MasterMemory
from Model.nd2FileAccessor import ND2FileAccessor
from BetterDemo.Model.Canvases.ImageCanvas import ImageCanvas
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage


class WindowMenuBarModel():
    def __init__(self):
        pass

    def openImage(self, imagePath, ):

        #open file at image location
        file = ND2FileAccessor(imagePath) #FIXME currently frame index is just none, handle this better.
        #place file in memory
        MasterMemory.setOpenFile(file)
        #convert to QImage compatable format
        frame = file.grabcurrentFrame()

        #Return QImage to presenter where it can be sent off to the master memory and view
        return frame
        

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