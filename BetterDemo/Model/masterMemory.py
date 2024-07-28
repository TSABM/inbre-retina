'''
snub
'''

import Model
import Model.Canvas
import Model.OpenScenes
from Presenter.AbstractPresenter import AbstractPresenter


class MasterMemory():
    subscribers = dict() #must be a view (or maybe a presenter?) that extends the abstract class
    openVideoPath = None #the full path to a video to be viewed frame by frame
    currentFrameNumber = None #current frame in a video
    frameLabels = dict() #frame num is the key, contents will be a list of the labels on that frame
    interactionMode = "Select label"

    def __init__(self):
        #self.addSubscriber("openScenes", Model.OpenScenes.OpenScenes())
        self.addSubscriber("canvas", Model.Canvas.Canvas("test2", 0))
        pass
    
    #interact with interaction mode
    @classmethod
    def setInteractionMode(cls, mode : str):
        '''
        Set global interaction mode to a string. Preset strings are select, and square (so far)
        '''
        cls.interactionMode = mode
    
    @classmethod
    def getInteractionMode(cls):
        return cls.interactionMode

    #deal with subscribers
    @classmethod
    def addSubscriber(cls, key, model):
        cls.subscribers[key] = model

    @classmethod
    def getSubscriberByKey(cls, key):
        return cls.subscribers.get(key)
    
    @classmethod
    def publishToSubscribers(cls, subsToPubTo : AbstractPresenter):
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
    def updateFrame(cls, frameNumber : int, frame : list):
        cls.frameLabels.update({frameNumber : frame})

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