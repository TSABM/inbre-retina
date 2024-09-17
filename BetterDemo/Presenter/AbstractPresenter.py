from abc import ABC, abstractmethod
from Model.masterMemory import MasterMemory

class AbstractPresenter(ABC):
    @abstractmethod
    def __init__(self, view):
        self.view  = view

    @abstractmethod
    def refresh(self):
        pass
    
    def getView(self):
        return self.view