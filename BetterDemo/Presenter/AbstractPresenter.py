from abc import ABC, abstractmethod
from masterMemory import MasterMemory

class AbstractPresenter(ABC):
    @abstractmethod
    def __init__(self, view):
        self.view  = view
        self.subscribers = []

    def publish(self, subsToPubTo):
        MasterMemory.publishToSubscribers(subsToPubTo)
    
    def getView(self):
        return self.view
    
    def addSubscriber(self, key, newSubscriberObject = None):
        if newSubscriberObject != None:
            MasterMemory.addSubscriber(key, newSubscriberObject)
        self.subscribers.append(key)
    
    def getSubscriberByKey(self, key):
        return MasterMemory.getSubscriberByKey(key)