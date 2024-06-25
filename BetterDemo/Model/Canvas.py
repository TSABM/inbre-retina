'''
The QGraphics Scene that all drawing takes place
'''
from PyQt5.QtWidgets import QGraphicsScene
import PyQt5.QtWidgets as qtw

defaultWidth = 400
defaultHeight = 200

class Canvas():
    def __init__(self):
        super().__init__()
        self.scene = qtw.QGraphicsScene(0, 0, self.getWidth(), self.getHeight())
        self.layers = []
        self.currentLayer = None

    #handling drawing
    def onClick():
        pass
    def onDrag():
        pass
    def onRelease():
        pass

    #handling layers
    def getWidth(self):
        if self.getBaseLayer() == None:
            return defaultWidth
        else:
            pass

    def getHeight(self):
        if self.getBaseLayer() == None:
            return defaultHeight
        else:
            pass

    def getBaseLayer(self):
        return None
   
    def addLayer(self):
        self.layers.append()
        pass
    
    def selectLayer():
        pass
    
    def deleteLayer():
        pass

    

        
