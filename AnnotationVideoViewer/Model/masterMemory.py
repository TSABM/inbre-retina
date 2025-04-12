'''
snub
'''

class MasterMemory():
    subscribers = dict() #must be a view (or maybe a presenter?) that extends the abstract class
    canvas = None
    labelData = None
    currentFrameNumber : int = 0
    sourcePath : str = "" #this is the path to the graphic resource being used by the project. Used in project opening/importing and exporting

    def __init__(self):
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