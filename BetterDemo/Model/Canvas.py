'''
The QGraphics Scene that all drawing takes place
'''
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage, QColor
#from Model.masterMemory import MasterMemory

defaultWidth = 400
defaultHeight = 200



class Canvas():
    def __init__(self):
        self.scene = QGraphicsScene(0, 0, defaultWidth, defaultHeight)
        self.pixmap = QPixmap()
        self.labels = []

    def getScene(self):
        return self.scene
    
    def getPixmap(self):
        return self.pixmap
    

    def setBaseImage(self, width, height, image):
        self.scene.width = width
        self.scene.height = height

        self.scene.addItem()
    
    def addBox(self, rectangleToAdd):
        self.labels.append(rectangleToAdd)
        painter = QPainter(self.pixmap)
        painter.setPen(QColor(255, 0, 0))
        painter.drawRect(rectangleToAdd)
        painter.end()
        #self.pixmap_item.setPixmap(self.pixmap)
        pass