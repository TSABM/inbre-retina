'''
snub
'''

#import Model
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
    
    @classmethod
    def getLabelData(cls):
        return cls.labelData