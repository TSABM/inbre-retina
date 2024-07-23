'''
The QGraphics Scene that all drawing takes place
'''
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage, QColor
from PyQt5.QtCore import Qt
#from Model.masterMemory import MasterMemory

defaultWidth = 400
defaultHeight = 200



class Canvas(QGraphicsScene):
    def __init__(self, fileName, frameNumber, labels = []):
        super().__init__(0, 0, defaultWidth, defaultHeight)
        self.fileName = fileName
        self.frameNumber = frameNumber
        self.labels = labels
        self.pixmap = QPixmap(defaultWidth, defaultHeight)
        self.pixmap_item = QGraphicsPixmapItem(self.pixmap)
        
        self.setBackgroundBrush(QColor(200, 200, 200)) #drawing background to a light gray to indicate the end of the drawable canavs
        self.drawBaseImage()
        self.addItem(self.pixmap_item)

    def getScene(self):
        return self.scene
    
    def getPixmap(self):
        return self.pixmap
    
    def addBox(self, rectangleToAdd):
        self.labels.append(rectangleToAdd)
        self.updatePixmap()

    def drawBaseImage(self):
        self.pixmap.fill(Qt.white)

    def updatePixmap(self):
        self.drawBaseImage()
        painter = QPainter(self.pixmap)
        painter.setPen(QColor(255, 0, 0)) #FIXME let the user choose the color in the future, and maybe the width too.
        for rect in self.labels:
            painter.drawRect(rect)
        painter.end()
        self.pixmap_item.setPixmap(self.pixmap)