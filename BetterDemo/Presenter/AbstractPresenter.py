from abc import ABC, abstractmethod

class AbstractPresenter(ABC):
    @abstractmethod
    def __init__(self, view, model = None):
        self.view  = view
        self.model = model
        self.subscribers = []
    
    def getView(self):
        return self.view
    
    def getModel(self):
        return self.model
    
    def addSubscriber(self, subscriber):
        self.subscribers.append(subscriber)