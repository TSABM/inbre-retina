'''
The QGraphics Scene that all drawing takes place
'''
from PyQt5.QtWidgets import QGraphicsScene
import PyQt5.QtWidgets as qtw

class Canvas(QGraphicsScene):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.drawing = False
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
    def getWidth():
        pass

    def getHeight():
        pass

    def setBaseLayer(self, graphicsItem):
        pass
   
    def addLayer(self):
        self.layers.append()
        pass
    
    def selectLayer():
        pass
    
    def deleteLayer():
        pass

    

        
