'''
snub
'''

import Model
import Model.Canvas
import Model.OpenScenes


class MasterMemory():
    subscribers = dict() #must be a view (or maybe a presenter?) that extends the abstract class
    openNd2File = None #Must be in a numpy array?
    
    def __init__(self):
        #self.addSubscriber("openScenes", Model.OpenScenes.OpenScenes())
        self.addSubscriber("canvas", Model.Canvas.Canvas())
        pass
    
    @classmethod
    def addSubscriber(cls, key, model):
        cls.subscribers[key] = model

    @classmethod
    def getSubscriberByKey(cls, key):
        return cls.subscribers.get(key)
    
    @classmethod
    def setOpenFile(cls, openFile):
        cls.openNd2Files = openFile

    @classmethod
    def getOpenFiles(cls):
        return cls.openNd2Files
    
    @classmethod
    def publishToSubscribers(cls, subsToPubTo):
        for subKey in subsToPubTo:
            sub = cls.getSubscriberByKey(subKey)
            sub.refresh() #FIXME this will only work for views that extend the abstract... there must be a better way to handle this...

    def unsubscribe():
        pass