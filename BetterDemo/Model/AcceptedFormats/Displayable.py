from abc import ABC, abstractmethod

class Displayable(ABC):
    '''
    an abstract class. Any other class that inherits or extends this abstract ought to be able to be displayed in the app
    '''
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def getPixmap():
        pass