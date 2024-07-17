import nd2
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage


class ND2FileAccessor():
    
    def __init__(self, filePath, currentFrameIndex = 0):
        self.filePath = filePath
        self.currentFrameIndex = currentFrameIndex
        with nd2.ND2File(filePath) as myfile:
            self.attributes = myfile.attributes
            self.componentsPerChannel = myfile.components_per_channel

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
    
    def __normalize(self):
        #ensure image is 16 bit
        #normalize to 8 bit
        #

    def __convertFrameToQImage(self, frame):
        print("shape metadata: ", self.attributes)
        channels = self.attributes.channelCount
        width = self.attributes.widthPx
        height = self.attributes.heightPx
        #normalize the 16 bit image to 8 for display
        #FIXME
        #if grayscale
        if channels == 1:
            qimage = QImage(frame.data, width, height, width, QImage.Format_Grayscale8)
            pass
        #if grayscale and alpha
        elif channels == 2:
            #FIXME
            pass
        #RGB
        if channels == 3:
            qimage = QImage(frame.data, width, height, 3 * width, QImage.Format_RGB888)
        #if 4, rgba
        elif channels == 4:
            qimage = QImage(frame.data, width, height, 4 * width, QImage.Format_RGBA8888)
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
