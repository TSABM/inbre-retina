'''
The QGraphics Scene that all drawing takes place
'''
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage, QColor
from PyQt5.QtCore import QRect, QPoint, Qt, QSize
from BetterDemo.Model.Labels import Label

defaultWidth = 400
defaultHeight = 200
cornerSize = 6


class Canvas(QGraphicsScene):
    def __init__(self, fileName : str, frameNumber : int, labels : list = []):
        super().__init__(0, 0, defaultWidth, defaultHeight)
        self.fileName : str = fileName
        self.frameNumber : int = frameNumber
        self.labels : list[Label] = labels
        self.pixmap = QPixmap(defaultWidth, defaultHeight)
        self.pixmap_item = QGraphicsPixmapItem(self.pixmap)

        self.selectedLabel = None
        self.resizing = False
        self.resizecorner = None
        
        self.setBackgroundBrush(QColor(200, 200, 200)) #drawing background to a light gray to indicate the end of the drawable canavs
        self.drawBaseImage()
        self.addItem(self.pixmap_item)
    
    def getPixmap(self):
        return self.pixmap
    
    def getLabels(self):
        return self.labels
    
    def getFrameNumber(self):
        return self.frameNumber
    
    def getSelectedLabel(self):
        return self.selectedLabel
    
    def addBox(self, labelToAdd : Label):
        #append label to local list
        self.labels.append(labelToAdd)
        #update pixmap so boxes display
        self.updatePixmap()
        #return labels to update the master mem
        return self.getLabels()
        

    def drawBaseImage(self):
        self.pixmap.fill(Qt.white)

    def updatePixmap(self, selectedlabel : Label = None):
        self.drawBaseImage()
        painter = QPainter(self.pixmap)
        painter.setPen(QColor(255, 0, 0)) #FIXME let the user choose the color in the future, and maybe the width too.
        for label in self.labels:
            if label == selectedlabel:
                painter.setPen(QPen(QColor(0, 0, 255), 2))  # Blue pen for selected rectangle
                painter.drawRect(label.rectangle)
                self.drawResizeHandles(painter, label)
                painter.setPen(QColor(255, 0, 0)) #set painter color back to red for the non selected labels
            else:
                painter.drawRect(label.rectangle)
        painter.end()
        self.pixmap_item.setPixmap(self.pixmap)
    
    def drawResizeHandles(self, painter, label : Label):
        handles = self.getResizeHandles(label.rectangle)
        painter.setBrush(QColor(0, 0, 255)) #blue handle fill
        #draw each handle
        for handle in handles:
            painter.drawRect(handle)
        #remove blue fill for future rectangles
        painter.setBrush(Qt.NoBrush)

    def getResizeHandles(self, rect):
        return [
            QRect(rect.topLeft() - QPoint(cornerSize//2, cornerSize//2), QSize(cornerSize, cornerSize)),
            QRect(rect.topRight() - QPoint(cornerSize//2, cornerSize//2), QSize(cornerSize, cornerSize)),
            QRect(rect.bottomLeft() - QPoint(cornerSize//2, cornerSize//2), QSize(cornerSize, cornerSize)),
            QRect(rect.bottomRight() - QPoint(cornerSize//2, cornerSize//2), QSize(cornerSize, cornerSize))
        ]
    
    def selectBox(self, point):
        for label in self.labels:
            if label.rectangle.contains(point):
                print("box selected")
                self.selectedLabel = label
                self.updatePixmap(label)
                return self.selectedLabel
            else:
                pass
        print("no box selected")
        self.deselectBox()
        return None
    
    def deselectBox(self):
        self.selectedLabel = None
        self.updatePixmap()

    def selectResizeCorner(self, point):
        #if no box is selected do nothing
        if self.selectedLabel == None:
            print("corner cannot be selected: no label marked as selected")
            return None
        else:
            handles = self.getResizeHandles(self.selectedLabel.rectangle)
            for index in range(len(handles)):
                if handles[index].contains(point):
                    return index
    
    def resizeBox(self, point, corner):
        if corner == 0:  # Top-left
            self.selectedLabel.rectangle.setTopLeft(point)
        elif corner == 1:  # Top-right
            self.selectedLabel.rectangle.setTopRight(point)
        elif corner == 2:  # Bottom-left
            self.selectedLabel.rectangle.setBottomLeft(point)
        elif corner == 3:  # Bottom-right
            self.selectedLabel.rectangle.setBottomRight(point)

        self.updatePixmap(self.selectedLabel)
    
    def moveBox(self, point):
        self.selectedLabel.rectangle.moveCenter(point)
        self.updatePixmap(self.selectedLabel)