import nd2

class ND2FileAccessor():
    
    def __init__(self, fileName, filePath, currentFrameIndex = None):
        self.fileName = fileName
        self.filePath = filePath
        self.currentFrameIndex = currentFrameIndex

    def grabFrameByIndex(self, index):
        '''
        returns the data for a frame of an nd2 files video as a numpy array
        '''
        with nd2.ND2File(self.getFilePath()) as nd2_file:
            frame = nd2_file.read_frame(index)
        return frame
    
    def grabNextFrame(self):
        #FIXME check if it can be incremented
        with nd2.ND2File(self.getFilePath()) as nd2_file:
            frame = nd2_file.read_frame(self.incrementFrameIndex())
        return frame

    def grabPrevFrame(self):
        #FIXME check if it can be decremented
        with nd2.ND2File(self.getFilePath()) as nd2_file:
            frame = nd2_file.read_frame(self.decrementFrameIndex())
        return frame
    
    def getFileName(self):
        return self.fileName
    
    def getFilePath(self):
        return self.filePath
    
    def incrementFrameIndex(self):
        self.currentFrameIndex += 1
        return self.currentFrameIndex
    
    def decrementFrameIndex(self):
        self.currentFrameIndex -= 1
        return self.currentFrameIndex
