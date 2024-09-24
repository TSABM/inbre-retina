'''
The QGraphics Scene that all drawing takes place
'''
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage, QColor
from PyQt5.QtCore import QRect, QPoint, Qt, QSize
from Model.LabelData import BoundingBox
from Model.AcceptedFormats.Displayable import Displayable
from Model.masterMemory import MasterMemory

## temporary default values ##
defaultWidth = 400
defaultHeight = 200
cornerSize = 6


class CanvasModel():
    '''
    a canvas which renders a static image and accepts labels
    '''
    def __init__(self):
        self.fileToDisplay : Displayable = None
        self.scene : QGraphicsScene = QGraphicsScene()
        
        self.pixmap : QPixmap = None
        #FIXME need to make compatable with videos (gif videos)
        #self.pixmap = QPixmap(defaultWidth, defaultHeight)
        self.pixmap_item = QGraphicsPixmapItem(self.pixmap)

        self.selectedItem = None
        self.resizing = False
        self.resizecorner = None
        
        self.scene.setBackgroundBrush(QColor(200, 200, 200)) #drawing background to a light gray to indicate the end of the drawable canavs
        self.updatePixmap()
        self.scene.addItem(self.pixmap_item)
    
    def getScene(self):
        return self.scene
    
    
    ## handle pixmap setting and getting ##  

    def setfile(self, file):
        #FIXME verify valid file format before setting (possibly in the presenter)
        self.fileToDisplay = file

    def __setPixmap__(self):
        if self.fileToDisplay != None:
            self.pixmap = self.fileToDisplay.getPixmap()
            self.pixmap_item.setPixmap(self.pixmap)

    def updatePixmap(self):
        self.__setPixmap__()
        if self.pixmap != None:
            painter = QPainter(self.pixmap)
            painter.setPen(QColor(255, 0, 0)) #FIXME let the user choose the color in the future, and maybe the width too.
            self.__drawLabels__(painter)

    def __drawLabels__(self, painter : QPainter):
        labelData = MasterMemory.getLabelDataModel()
        boundingBoxes : dict = labelData.get("BoundingBoxes")
        boxIds = MasterMemory.getAllBoxIDsForAFrame(MasterMemory.getCurrentFrameNumber())
        if boxIds != None:
            for boxId in boxIds:
                #if its selected render it blue and with handles
                box : BoundingBox = boundingBoxes.get(boxId)
                rectangle : QRect = box.get_boundingBox_as_rect()
                if box == self.selectedItem:
                    painter.setPen(QPen(QColor(0, 0, 255), 2))  # Blue pen for selected rectangle
                    painter.drawRect(rectangle)
                    self.drawResizeHandles(painter, rectangle)
                    painter.setPen(QColor(255, 0, 0)) #set painter color back to red for the non selected labels
                #else render it like normal
                else:
                    painter.drawRect(rectangle)
        painter.end()
        self.pixmap_item.setPixmap(self.pixmap)


    def getPixmap(self):
        return self.pixmap
    
    def getFrameNumber(self):
        return self.frameNumber
    
    ## Handle everything related to the bounding boxes ##
    def addCell(self, key, cell):
        #make the box into a label object
        #boxID
        #cellID
        #frame num
        #cell type
        #x, y, width, height
        #events
        cell = Cell()
        

        #append label to local list
        self.labels.update({key : cell})
        #update pixmap so boxes display
        self.updatePixmap()
        #return labels to update the master mem
        return self.getLabels()

    def selectBox(self, point):
        labelData = MasterMemory.getLabelDataModel()
        boundingBoxes : dict = labelData.get("BoundingBoxes")
        boxIds = MasterMemory.getAllBoxIDsForAFrame(0) #FIXME this index should update based on the frame looked at
        if boxIds == None:
            print("tried to select a box but boxIDs is none type?")
            return None
        for boxID in boxIds:
            box : BoundingBox = boundingBoxes.get(boxID)
            rectangle : QRect = box.get_boundingBox_as_rect()
            if rectangle == None:
                print("ERROR: no rectangle assigned to this label")
                pass
            elif rectangle.contains(point):
                print("box selected")
                self.selectedItem = box
                self.updatePixmap()
                return self.selectedItem
            else:
                pass
        print("no box selected")
        self.deselectBox()
        return None
    
    def deselectBox(self):
        self.selectedItem = None
        self.updatePixmap()
    
    def resizeBox(self, point, corner):
        if corner == 0:  # Top-left
            self.selectedItem.rectangle.setTopLeft(point)
        elif corner == 1:  # Top-right
            self.selectedItem.rectangle.setTopRight(point)
        elif corner == 2:  # Bottom-left
            self.selectedItem.rectangle.setBottomLeft(point)
        elif corner == 3:  # Bottom-right
            self.selectedItem.rectangle.setBottomRight(point)

        self.updatePixmap(self.selectedItem)
    
    def moveBox(self, point):
        self.selectedItem.rectangle.moveCenter(point)
        self.updatePixmap(self.selectedItem)

    def drawResizeHandles(self, painter, rectangle):
        handles = self.getResizeHandles(rectangle)
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

    def selectResizeCorner(self, point):
        #if no box is selected do nothing
        if self.selectedItem == None:
            print("corner cannot be selected: no label marked as selected")
            return None
        else:
            handles = self.getResizeHandles(self.selectedItem.rectangle)
            for index in range(len(handles)):
                if handles[index].contains(point):
                    return index
    
    def getLabels(self):
        return self.boundingBoxes
    
    def getSelectedLabel(self):
        return self.selectedItem