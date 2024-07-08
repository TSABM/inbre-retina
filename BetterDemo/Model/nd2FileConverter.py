
import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import QImage
import nd2
from Model.frameReader import FrameReader

class nd2FileConverter():
    def __init__(self):
        self.frameReader = FrameReader()
        pass
    
    def convertND2ToWidget(self, fileToConvert):
        pass

    def openNd2(self, fileToOpen):
        #nd2Array = nd2.imread(fileToOpen, xarray= True, dask= True)
        #nd2Array = nd2.imread(fileToOpen)
        #print("file opened")

        #get metadata (especially height, and width)
        

        #grab single frame
        frame = self.frameReader.readOneFrame(fileToOpen, 0) #FIXME using 0 as a temp value.    
        #convert to a QImage
        imageToShow = QImage(frame.data, width, height, )

        #attach QImage to the canvas

        ''' This code may be useful, review it and see if any can be salvaged.
        with nd2.ND2File(fileToOpen) as myfile:
            print(myfile.metadata)
            
            tempFrame = myfile.read_frame(0)

            print("Frame shape: %f", tempFrame.shape)
            
            
            #if grayscale
            if tempFrame.ndim == 2:
                height, width = tempFrame.shape
                bytesPerLine = width
                qImage = QImage(tempFrame.data, width, height, bytesPerLine, QImage.Format_Grayscale8)

            elif tempFrame.ndim == 3:
                #check here for 
                height, width, channels = tempFrame.shape
                if channels == 3:
                    imageFormat = QImage.Format_RGB888
                elif channels == 4:
                    imageFormat = QImage.Format_RGBA8888
                else:
                    raise ValueError("Unsupported channel number")
                bytes_per_line = width * channels
                qImage =  QImage(tempFrame.data, width, height, bytes_per_line, imageFormat)
            else:
                raise ValueError("unsupported array shape")
            #if not grayscale
                #if RGB
                #if RGBA
                #else
        print("returning a qimage")
        return qImage
        '''