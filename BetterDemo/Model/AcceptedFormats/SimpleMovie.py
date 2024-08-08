from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QMovie
from Model.AcceptedFormats.Displayable import Displayable

class SimpleMovie(Displayable):
    '''
    canvas that accepts GIF, MNG, and APNG formats
    '''
    def __init__(self):
        super().__init__()
        #self.label = QLabel #FIXME possibly not needed?
        self.movie : QMovie = None
    
    def getPixmap(self):
        return self.movie.currentPixmap()

    def setMovie(self, moviePath):
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
