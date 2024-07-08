import nd2


class FrameReader():
    '''
    Receives a nd2 file location and returns the frame data
    '''
    def __init__(self):
        pass
    
    def getMetadata(self, file):
        

    def readOneFrame(self, file, frameIndex):
        #check if file is valid
        #check if frameIndex is valid
        #grab valid frame at index
        with nd2.ND2File(file) as nd2_file:
            frame = nd2_file.read_frame(frameIndex)
        #return the frame as a numpy array
            #nd2Array = nd2.imread(self.file)
        return frame

    def readFramesFromAToB(self, file, indexA, indexB):
        #check if file is valid
        #check if start frame is valid
        #check if end frame is valid
        #grab frames between the two points
        pass

    def readAllFrames():
        #read all frame data
        pass