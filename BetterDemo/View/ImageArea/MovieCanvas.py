from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QMovie

class MovieCanvas(QLabel):
    def __init__(self):
        super().__init__()
        self.movie : QMovie = None
        pass

    def setMovie(self, moviePath):
        if moviePath != None:
            self.movie = QMovie(moviePath)
            if self.movie.isValid() == False:
                print("invalid movie attempted to load")
                return False
            else:
                print("Movie set")
                #FIXME

    def startMovie(self):
        pass

    def stopMovie(self):
        pass
    
    def stepFrameForward(self):
        pass

    def stepFrameBackward(self):
        pass
