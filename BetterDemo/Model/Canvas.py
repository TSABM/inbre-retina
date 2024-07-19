'''
The QGraphics Scene that all drawing takes place
'''
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage, QColor
#from Model.masterMemory import MasterMemory

defaultWidth = 400
defaultHeight = 200



class Canvas(QGraphicsScene):
    def __init__(self):
        super().__init__(0, 0, defaultWidth, defaultHeight)
        #self.setBaseImage(defaultWidth, defaultHeight)
        self.pixmap = QPixmap()
        self.pixmap_item = QGraphicsPixmapItem(self.pixmap)
        self.addItem(self.pixmap_item)
        self.labels = []

    def getScene(self):
        return self.scene
    
    def getPixmap(self):
        return self.pixmap
    

    def setBaseImage(self, width, height, image = None):
        self.scene.width = width
        self.scene.height = height

        if (image != None):
            self.scene.addItem()
    
    def addBox(self, rectangleToAdd):
        self.labels.append(rectangleToAdd)
        self.paintEvent(rectangleToAdd)
        

    def paintEvent(self, rectangleToAdd):
        painter = QPainter(self.pixmap)
        painter.setPen(QColor(255, 0, 0))
        painter.drawRect(rectangleToAdd)
        painter.end()
        self.pixmap_item.setPixmap(self.pixmap)
        