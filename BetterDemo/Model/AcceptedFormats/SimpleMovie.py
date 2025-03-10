# pylint: disable = no-name-in-module
#from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QMovie, QPixmap
from Model.AcceptedFormats.Displayable import Displayable

class SimpleMovie(Displayable):
    '''
    class that accepts GIF, MNG, and APNG formats
    '''
    def __init__(self, fileName : str):
        super().__init__(fileName)
        #self.label = QLabel #FIXME possibly not needed?
        self.movie : QMovie |None = None
    
    def setFrame(self, frame : int):
        '''set current frame'''
        if self.movie == None:
            print("cannot set frame no movie is loaded")
            return
        self.movie.jumpToFrame(frame)
        
    def getPixmap(self) -> QPixmap | None:
        '''returns a pixmap or none'''
        #verify there is a movie
        if self.movie == None:
            print("movie was not set")
            return
        if not self.movie.isValid():
            print("warning current movie is invalid")
            return
        #if current frame isnt set jump to the requested frame first
        if(self.movie.currentFrameNumber()) == -1:
            self.movie.jumpToFrame(0)
        #return pixmap
        return self.movie.currentPixmap()
    
    def getTotalFrames(self) -> int:
        super().getTotalFrames()
        if self.movie == None:
            return 0
        return self.movie.frameCount()

    def setMovie(self, moviePath : str) -> bool: #FIXME movie path and file name are not linked and could in theory be different...make sure its not a problem
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
        if self.movie == None:
            print("cannot jump to next frame no movie is loaded")
            return
        self.movie.jumpToNextFrame()

    def stepFrameBackward(self):
        pass
