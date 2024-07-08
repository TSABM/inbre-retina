'''
snub
'''

import Model
import Model.Canvas
import Model.OpenScenes


class MasterMemory():
    subscribers = dict()
    nd2File = []
    
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

    def unsubscribe():
        pass