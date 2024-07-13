from abc import ABC, abstractmethod


class AbstractView(ABC):
    @abstractmethod
    def __init__(self, view):
        self.view = view
        pass

    @abstractmethod
    def refresh(self):
        pass

    def getView(self):
        return self.view