'''
The QGraphics Scene that all drawing takes place
'''
from PyQt5.QtWidgets import QGraphicsScene
import Model.Marker as Marker

class Canvas(QGraphicsScene):
    drawing = False
    marker = Marker()
    layers = []
    def __init__(self, parent = None):
        super().__init__(parent)
        self.drawing = False
        layers = []
    
    #handling drawing
    def onClick():
        pass
    def onDrag():
        pass
    def onRelease():
        pass

    #handling layers
    def createLayer():
        pass
    def changeLayer():
        pass

    

        
