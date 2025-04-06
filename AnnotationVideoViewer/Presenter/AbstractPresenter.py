from abc import ABC, abstractmethod
#from Model.masterMemory import MasterMemory

class AbstractPresenter(ABC):
    @abstractmethod
    def __init__(self, view):
        self.view  = view
    
    def getView(self):
        return self.view