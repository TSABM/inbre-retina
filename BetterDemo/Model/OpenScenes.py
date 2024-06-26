import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import QPixmap

defaultWidth = 400
defaultHeight = 200

class OpenScenes():
    sceneContainer = []
    def __init__(self):
        self.appendDefault()
        pass

    def appendDefault(self):
        self.sceneContainer.append(qtw.QGraphicsScene(0, 0, self.getWidth(), self.getHeight()))

    def setSceneContainer(self, newSceneContainer):
        self.sceneContainer = newSceneContainer

    def getAllScenes(self):
        return self.sceneContainer

    def addScene(self, sceneToAdd):
        self.sceneContainer.append(sceneToAdd)

    def addSceneByPath(self, path):
        pixmap = QPixmap(path)
        graphicsPixmapItem = qtw.QGraphicsPixmapItem(pixmap)
        #self.scene.addItem(graphicsPixmapItem)
        newScene = qtw.QGraphicsScene(0, 0, self.getWidth(), self.getHeight())
        newScene.addItem(graphicsPixmapItem)
        self.sceneContainer.append(newScene)

    def getSceneByIndex(self, index):
        return self.sceneContainer[index]
    
    def updateExistingScene(self, index, sceneToUpdate):
        self.sceneContainer[index] = sceneToUpdate

    def getWidth(self):
        '''
        returns current scene width
        '''
        return defaultWidth

    def getHeight(self):
        '''
        returns current scene height
        '''
        return defaultHeight