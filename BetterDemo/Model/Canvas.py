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
    def __init__(self):
        super().__init__(0, 0, defaultWidth, defaultHeight)
        #drawing background to a light gray to indicate the end of the drawable canavs
        self.setBackgroundBrush(QColor(200, 200, 200))
        #init the pixmap FIXME: need to handle its size better and probably move this to a method
        self.pixmap = QPixmap(defaultWidth, defaultHeight)
        self.drawBaseImage()
        self.pixmap_item = QGraphicsPixmapItem(self.pixmap)
        self.addItem(self.pixmap_item)
        #init label storage FIXME: need to integrate this with the master memory better
        self.labels = []

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