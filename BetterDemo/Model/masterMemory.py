'''
snub
'''

import Model
#import Model.Canvases.ImageCanvas
#import Model.OpenScenes
#from Presenter.LabelDataPresenter import LabelDataPresenter
#from Presenter.CanvasPresenter import CanvasPresenter


class MasterMemory():
    subscribers = dict() #must be a view (or maybe a presenter?) that extends the abstract class
    #openVideoPath = None #the full path to a video to be viewed frame by frame
    #currentFrameNumber = None #current frame in a video
    canvas = None
    labelData = None
    currentFrameNumber : int = 0
    sourcePath : str = ""

    def __init__(self):
        #self.addSubscriber("openScenes", Model.OpenScenes.OpenScenes())
        #self.addSubscriber("canvas", Model.Canvas.Canvas("test2", 0))
        pass
    
    @classmethod
    def getCanvas(cls):
        return cls.canvas

    @classmethod
    def getCurrentFrameNumber(cls):
        return cls.currentFrameNumber

    @classmethod
    def getSourcePath(cls):
        return cls.sourcePath
    
    @classmethod
    def setCanvas(cls, canvas):
        cls.canvas = canvas
    
    @classmethod
    def setLabelData(cls, labelData):
        cls.labelData = labelData

    @classmethod
    def setSourcePath(cls, sourcePath : str):
        cls.sourcePath = sourcePath

    #deal with subscribers
    '''
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

    '''
    #deal with the open file
    '''
    @classmethod
    def setOpenFile(cls, openFile):
        cls.openNd2Files = openFile

    @classmethod
    def getOpenFiles(cls):
        return cls.openNd2Files
    '''
    
    @classmethod
    def getLabelData(cls):
        return cls.labelData

    @classmethod
    def deleteAllLabels(cls):
        pass
    
    @classmethod
    def exportLabelData(cls):
        '''
        take all labels and save them into a file
        '''
        pass

    @classmethod
    def importLabelData(cls):
        '''
        given a file containing label data extract all the labels for display
        '''
        pass