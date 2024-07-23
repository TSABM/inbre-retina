'''
The QGraphics Scene that all drawing takes place
'''
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage, QColor
from PyQt5.QtCore import Qt
from Model.Label import Label

defaultWidth = 400
defaultHeight = 200


class Canvas(QGraphicsScene):
    def __init__(self, fileName : str, frameNumber : int, labels : list = []):
        super().__init__(0, 0, defaultWidth, defaultHeight)
        self.fileName : str = fileName
        self.frameNumber : int = frameNumber
        self.labels : list[Label] = labels
        self.pixmap = QPixmap(defaultWidth, defaultHeight)
        self.pixmap_item = QGraphicsPixmapItem(self.pixmap)
        
        self.setBackgroundBrush(QColor(200, 200, 200)) #drawing background to a light gray to indicate the end of the drawable canavs
        self.drawBaseImage()
        self.addItem(self.pixmap_item)
    
    def getPixmap(self):
        return self.pixmap
    
    def getLabels(self):
        return self.labels
    
    def getFrameNumber(self):
        return self.frameNumber
    
    def addBox(self, labelToAdd : Label):
        #append label to local list
        self.labels.append(labelToAdd)
        #update pixmap so boxes display
        self.updatePixmap()
        #return labels to update the master mem
        return self.getLabels()
        

    def drawBaseImage(self):
        self.pixmap.fill(Qt.white)

    def updatePixmap(self, point):
        self.drawBaseImage()
        painter = QPainter(self.pixmap)
        painter.setPen(QColor(255, 0, 0)) #FIXME let the user choose the color in the future, and maybe the width too.
        for label in self.labels:
            painter.drawRect(label.rectangle)
        painter.end()
        self.pixmap_item.setPixmap(self.pixmap)
    
    def selectBox(self, point):
        for label in self.labels:
            if label.rectangle.contains(point):
                print("box selected")
                self.updatePixmap(point)
            else:
                print("no box selected")