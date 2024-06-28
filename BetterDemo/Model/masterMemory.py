'''
snub
'''

import Model
import Model.Canvas
import Model.OpenScenes


class MasterMemory():
    subscribers = dict()
    keys = {} #a key set
    def __init__(self):
        #self.addSubscriber("openScenes", Model.OpenScenes.OpenScenes())
        self.addSubscriber("canvas", Model.Canvas.Canvas())
        pass
    
    def addSubscriber(self, key, model):
        self.subscribers[key] = model

    def getKeys(self):
        return self.keys

    def subscribe():
        pass

    def unsubscribe():
        pass

    def publish():
        pass