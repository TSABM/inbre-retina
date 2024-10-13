from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QMovie
from Model.AcceptedFormats.Displayable import Displayable

class SimpleMovie(Displayable):
    '''
    canvas that accepts GIF, MNG, and APNG formats
    '''
    def __init__(self, fileName : str):
        super().__init__(fileName)
        #self.label = QLabel #FIXME possibly not needed?
        self.movie : QMovie = None
    
    def getPixmap(self, frame : int):
        if(self.movie.currentFrameNumber()) == -1:
            self.movie.jumpToFrame(frame)
        return self.movie.currentPixmap()
    
    def getTotalFrames(self):
        #super().getTotalFrames()
        return self.movie.frameCount()

    def setMovie(self, moviePath): #FIXME movie path and file name are not linked and could in theory be different...make sure its not a problem
        if moviePath != None:
            self.movie = QMovie(moviePath)
            if self.movie.isValid() == False:
                print("invalid movie format attempted to load")
                return False
            else:
                print("Movie set")
                #FIXME
                return True

    def startMovie(self):
        pass

    def stopMovie(self):
        pass
    
    def stepFrameForward(self):
        pass

    def stepFrameBackward(self):
        pass
