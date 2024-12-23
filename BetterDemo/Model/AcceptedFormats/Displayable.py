from abc import ABC, abstractmethod

class Displayable(ABC):
    '''
    an abstract class. Any other class that inherits or extends this abstract ought to be able to be displayed in the app
    '''
    sourceName : str = None

    @abstractmethod
    def __init__(self, sourceName):
        self.sourceName = sourceName
        pass

    @abstractmethod
    def getPixmap():
        pass

    def getSourceName(self):
        return self.sourceName

    @abstractmethod
    def getTotalFrames():
        pass