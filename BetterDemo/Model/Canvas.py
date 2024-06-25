'''
The QGraphics Scene that all drawing takes place
'''
#from PyQt5.QtWidgets import QGraphicsScene
#from PyQt5.QtGui import QPixmap, QPainter, QPen
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
    def getScene(self):
        '''
        returns current scene
        '''
        return self.scene

    def getWidth(self):
        '''
        returns current scene width
        '''
        if self.getBaseLayer() == None:
            return defaultWidth
        else:
            pass

    def getHeight(self):
        '''
        returns current scene height
        '''
        if self.getBaseLayer() == None:
            return defaultHeight
        else:
            pass

    def getBaseLayer(self):
        return None
   
    def addItem(self, itemPathToAdd):
        #self.layers.append()
        #pixmap = QPixmap(itemPathToAdd)
        #graphicsPixmapItem = qtw.QGraphicsPixmapItem(pixmap)
        #self.scene.addItem(graphicsPixmapItem)
        pass

    def selectLayer():
        pass
    
    def deleteLayer():
        pass

    

        
