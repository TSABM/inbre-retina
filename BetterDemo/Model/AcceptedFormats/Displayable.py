from abc import ABC, abstractmethod

class Displayable(ABC):
    '''
    an abstract class. Any other class that inherits or extends this abstract ought to be able to be displayed in the app
    '''
    fileName : str = None

    @abstractmethod
    def __init__(self, fileName):
        self.fileName = fileName
        pass

    @abstractmethod
    def getPixmap():
        pass

    def getFileName(self):
        return self.fileName

    @abstractmethod
    def getTotalFrames():
        pass