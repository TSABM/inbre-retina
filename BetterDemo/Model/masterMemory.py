'''
snub
'''

import Model
import Model.Canvas
import Model.OpenScenes


class MasterMemory():
    subscribers = dict()
    openNd2Files = []
    
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
    def addOpenFile(cls, openFile):
        cls.openNd2Files.append(openFile)

    @classmethod
    def getOpenFiles(cls):
        return cls.openNd2Files

    def unsubscribe():
        pass