'''
snub
'''

import Model
import Model.Canvas
import Model.OpenScenes


class MasterMemory():
    subscribers = dict()
    openNd2File = None
    
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
        for sub in cls.subscribers:
            #push the refresh FIXME
            pass
        pass

    def unsubscribe():
        pass