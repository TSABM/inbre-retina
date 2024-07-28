from abc import ABC, abstractmethod
from Model.masterMemory import MasterMemory

class AbstractPresenter(ABC):
    @abstractmethod
    def __init__(self, view):
        self.view  = view
        self.subscribers = []

    @abstractmethod
    def refresh(self):
        pass

    def publishToSubs(self):
        MasterMemory.publishToSubscribers(self.subscribers)
    
    def getView(self):
        return self.view
    
    def registerNewSubscriber(self, key, newSubscriberObject):
        '''
        Adds a subscriber object to the master memory so it can be published to by other classes
        '''
        MasterMemory.addSubscriber(key, newSubscriberObject)
    
    def addSubscriber(self, key):
        '''
        Adds a subscriber key so this object can publish to it
        '''
        self.subscribers.append(key)
    
    def getSubscriberByKey(self, key):
        return MasterMemory.getSubscriberByKey(key)