'''
The QGraphics Scene that all drawing takes place
'''
from PyQt5.QtWidgets import QGraphicsScene
#from PyQt5.QtGui import QPixmap, QPainter, QPen

defaultWidth = 400
defaultHeight = 200

class Canvas():
    def __init__(self):
        self.setDefault()


    def setDefault(self):
        self.scene = QGraphicsScene(0, 0, defaultWidth, defaultHeight)

    def getScene(self):
        return self.scene

    '''
    #handling layers
    def setCurrentScene(self, index):
        self.currentSceneIndex = index

    def getScene(self):
        return self.currentScene

    
   
    def addItem(self, itemPathToAdd):
        #self.layers.append()
        #pixmap = QPixmap(itemPathToAdd)
        #graphicsPixmapItem = qtw.QGraphicsPixmapItem(pixmap)
        #self.scene.addItem(graphicsPixmapItem)
        pass

    #handling drawing
    def onClick():
        pass
    def onDrag():
        pass
    def onRelease():
        pass
    

    '''
