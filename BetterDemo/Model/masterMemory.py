'''
snub
'''

import Model
import Model.Canvas
import Model.OpenScenes


class MasterMemory():
    subscribers = dict() #must be a view (or maybe a presenter?) that extends the abstract class
    openNd2File = None #Must be in a numpy array?
    labels = dict() #remember you will need to be able to access specific labels by key, all labels for a frame, and all labels in general
    
    def __init__(self):
        #self.addSubscriber("openScenes", Model.OpenScenes.OpenScenes())
        self.addSubscriber("canvas", Model.Canvas.Canvas())
        pass
    
    #deal with subscribers
    @classmethod
    def addSubscriber(cls, key, model):
        cls.subscribers[key] = model

    @classmethod
    def getSubscriberByKey(cls, key):
        return cls.subscribers.get(key)
    
    @classmethod
    def publishToSubscribers(cls, subsToPubTo):
        for subKey in subsToPubTo:
            sub = cls.getSubscriberByKey(subKey)
            sub.refresh() #FIXME this will only work for views that extend the abstract... there must be a better way to handle this...

    def unsubscribe():
        pass

    #deal with the open file
    @classmethod
    def setOpenFile(cls, openFile):
        cls.openNd2Files = openFile

    @classmethod
    def getOpenFiles(cls):
        return cls.openNd2Files
    
    #deal with labels
    @classmethod
    def addLabel(cls, label):
        pass

    @classmethod
    def getLabel(cls, key):
        '''
        return a specific label by key
        '''
        pass

    @classmethod
    def overrideLabel(cls, key, frame, newLabel):
        '''
        replace an existing label with a new one
        '''
        pass

    @classmethod
    def deleteLabel(cls, key):
        '''
        '''
        pass

    @classmethod
    def getAllLabelsForAFrame(cls, frame : int):
        '''
        get all the labels for a specific frame of the image
        '''
        pass
    
    @classmethod
    def deleteAllLabelsForAFrame(cls, frame : int):
        '''
        delete all the labels for a specific frame of the image
        '''
        pass

    @classmethod
    def getAllLabels(cls):
        pass

    @classmethod
    def deleteAllLabels(cls):
        pass

    @classmethod
    def saveAllLabels(cls):
        '''
        take all labels and save them into a file
        '''
        pass

    @classmethod
    def readLabelsFromFile(cls):
        '''
        given a file containing label data extract all the labels for display
        '''
        pass