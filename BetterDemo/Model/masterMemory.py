'''
snub
'''

import Model
import Model.OpenScenes


class MasterMemory():
    subscribers = dict()
    def __init__(self):
        self.addSubscriber("openScenes", Model.OpenScenes.OpenScenes())
        self.addSubscriber("")
        pass
    
    def addSubscriber(self, key, model):
        self.subscribers[key] = model

    def subscribe():
        pass

    def unsubscribe():
        pass

    def publish():
        pass