'''
The QGraphics Scene that all drawing takes place
'''
#from PyQt5.QtWidgets import QGraphicsScene
#from PyQt5.QtGui import QPixmap, QPainter, QPen
import PyQt5.QtWidgets as qtw
from Model.OpenScenes import OpenScenes

class Canvas():
    def __init__(self):
        super().__init__()
        self.currentSceneIndex = 0
        self.currentScene = OpenScenes().getSceneByIndex(self.currentSceneIndex)

    #handling layers
    def setCurrentScene(self, index):
        self.currentSceneIndex = index

    def getScene(self):
        '''
        returns current scene
        '''
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
    

        
