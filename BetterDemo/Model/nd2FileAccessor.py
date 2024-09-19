import nd2
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage
import numpy as np


class ND2FileAccessor():
    
    def __init__(self, filePath, currentFrameIndex = 0):
        self.filePath = filePath
        self.currentFrameIndex = currentFrameIndex
        with nd2.ND2File(filePath) as myfile:
            self.attributes = myfile.attributes
            self.componentsPerChannel = myfile.components_per_channel

    def grabFrameByIndex(self, index):
        #returns the data for a frame of an nd2 files video as a numpy array
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
    
    def __normalize(self, imageToNormalize):
        #ensure image is 16 bit
        #normalize to 8 bit
        print("normalizing")
        normalizedArray = (imageToNormalize/256).astype(np.uint8)
        return normalizedArray

    def __handleTwoChannelGrayscale(self, grayscaleImage):
        #convert to a grey rgba image. This will allow display    
        pass

    def __convertFrameToQImage(self, frame):
        print("shape metadata: ", self.attributes)
        channels = self.attributes.channelCount
        width = self.attributes.widthPx
        height = self.attributes.heightPx
        #normalize the 16 bit image to 8 for display
        normalizedFrame = self.__normalize(frame)
        #FIXME
        #if grayscale
        if channels == 1:
            qimage = QImage(normalizedFrame.data, width, height, width, QImage.Format_Grayscale8)
            pass
        #if grayscale and alpha
        #elif channels == 2:
        #    print("unimplemented")
            #qimage = QImage(normalizedFrame.data, width, height, width, QImage.Format_Grayscale16)
        #RGB
        elif channels == 3: 
            qimage = QImage(normalizedFrame.data, width, height, 3 * width, QImage.Format_RGB888)
        #if 4, rgba
        elif channels == 4:
            qimage = QImage(normalizedFrame.data, width, height, 4 * width, QImage.Format_RGBA8888)
        #else, error
        else:
            raise ValueError("Unsupported number of channels: {}".format(channels))
        print("frame formatted for display")
        return qimage
    
    def getFilePath(self):
        return self.filePath
    
    def incrementFrameIndex(self):
        self.currentFrameIndex += 1
        return self.currentFrameIndex
    
    def decrementFrameIndex(self):
        self.currentFrameIndex -= 1
        return self.currentFrameIndex
