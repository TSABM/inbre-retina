from PyQt5.QtCore import QObject

class Displayable(QObject):
    '''
    an abstract class. Any other class that inherits or extends this abstract ought to be able to be displayed in the app
    '''
    sourceName : str | None = None

    def __init__(self, sourceName):
        super().__init__()
        self.sourceName = sourceName

    def getPixmap(self):
        pass
    
    def getTotalFrames(self):
        pass

    def getSourceName(self):
        return self.sourceName