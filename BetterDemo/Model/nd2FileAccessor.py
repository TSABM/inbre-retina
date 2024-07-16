import nd2
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage


class ND2FileAccessor():
    
    def __init__(self, filePath, currentFrameIndex = 0):
        self.filePath = filePath
        self.currentFrameIndex = currentFrameIndex
        with nd2.ND2File(filePath) as myfile:
            self.metadataShape = myfile.shape

    def grabFrameByIndex(self, index):
        '''
        returns the data for a frame of an nd2 files video as a numpy array
        '''
        with nd2.ND2File(self.getFilePath()) as nd2_file:
            frame = nd2_file.read_frame(index)
        convertedFrame = self.__convertFrameToQImage(frame)
        return convertedFrame
    
    def grabcurrentFrame(self):
        return self.grabFrameByIndex(self.currentFrameIndex)
    
    def grabNextFrame(self):
        #FIXME check if it can be incremented
        return self.grabFrameByIndex(self.incrementFrameIndex())

    def grabPrevFrame(self):
        #FIXME check if it can be decremented
        return self.grabFrameByIndex(self.decrementFrameIndex())
    
    def __convertFrameToQImage(self, frame):
        #determine number of channels
        #FIXME grab metadata properly and judge based on that.
        print("shape metadata: ", self.metadataShape)
        T, channels, height, width = self.metadataShape
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
        return qimage
    
    def getFilePath(self):
        return self.filePath
    
    def incrementFrameIndex(self):
        self.currentFrameIndex += 1
        return self.currentFrameIndex
    
    def decrementFrameIndex(self):
        self.currentFrameIndex -= 1
        return self.currentFrameIndex
