from abc import ABC, abstractmethod

class AbstractPresenter(ABC):
    @abstractmethod
    def __init__(self, view):
        self.view  = view
        self.subscribers = []
    
    def getView(self):
        return self.view
    
    def addSubscriber(self, subscriber):
        self.subscribers.append(subscriber)