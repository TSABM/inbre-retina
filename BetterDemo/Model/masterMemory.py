'''
snub
'''

import Model
import Model.Canvas
import Model.OpenScenes


class MasterMemory():
    subscribers = dict()
    def __init__(self):
        self.addSubscriber("openScenes", Model.OpenScenes.OpenScenes())
        self.addSubscriber("canvas", Model.Canvas.Canvas())
        pass
    
    def addSubscriber(self, key, model):
        self.subscribers[key] = model

    def subscribe():
        pass

    def unsubscribe():
        pass

    def publish():
        pass