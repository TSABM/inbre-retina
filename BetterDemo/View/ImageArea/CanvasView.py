# pylint: disable = no-name-in-module
import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import QRect, QPoint, Qt, QSize
from Presenter.CanvasPresenter import CanvasPresenter
from PyQt5.QtGui import QPixmap, QPainter, QColor
#from View.ImageArea.LabelPopup import LabelPopup

class CanvasView(qtw.QGraphicsView):
    '''
    The canvas
    '''
    def __init__(self):
        super().__init__()
        #init presenter and request QGraphicsScene
        self.presenter = CanvasPresenter(self)

        #init variables for drawing labels
        self.drawing = False
        self.resizing = False
        self.moving = False
        self.initialPoint = QPoint()
        self.resizeCornerIndex = None
        self.rubberBand = qtw.QRubberBand(qtw.QRubberBand.Rectangle, self)

        #turn mouse tracking on
        self.setMouseTracking(True)
        #setting render hints (askes engine to try to antialias and use smooth pixmap transforming)
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)

        self.setCanvas()
    
    def setCanvas(self):
        canvas = self.presenter.getCanvas()
        self.setScene(canvas.getScene())

    def mousePressEvent(self, event):
        #check if the event is a left click
        if event.button() == Qt.LeftButton:
            mode = self.presenter.getInteractionMode()
            self.initialPoint = self.mapToScene(event.pos()).toPoint()
            
            if mode == "Select label":
                selectedBox = self.presenter.selectBox(self.initialPoint)
                if selectedBox != None:
                    cornerIndex = self.presenter.selectResizeCorner(self.initialPoint)
                    if cornerIndex != None:
                        self.resizing = True
                        self.resizeCornerIndex = cornerIndex
                    else:
                        self.moving = True
                    
            elif mode == "Draw label":
                #ensure there are no boxes in select mode
                self.presenter.deselectBox()
                #begin rubber band box
                self.rubberBand.setGeometry(QRect(self.mapFromScene(self.initialPoint), QSize())) #note the new QSize object has width and height of 0
                self.rubberBand.show()
            
            elif mode == "Erase":
                print("Erase has not yet been implemented")
            
            else:
                print("invalid interaction mode ", mode)
     
    def mouseMoveEvent(self, event):
        mode = self.presenter.getInteractionMode()
        new_pos = self.mapToScene(event.pos()).toPoint()
        if mode == "Select label":
            if self.resizing == True and self.resizeCornerIndex != None:
                self.presenter.resizeBox(new_pos, self.resizeCornerIndex)
            elif self.moving == True:
                self.presenter.moveBox(new_pos)
        elif mode == "Draw label":
            if not self.initialPoint.isNull():
                self.rubberBand.setGeometry(QRect(self.mapFromScene(self.initialPoint), self.mapFromScene(new_pos)).normalized())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            mode = self.presenter.getInteractionMode()
            if mode == "Select label":
                if self.resizing == True:
                    self.resizing = False
                    if self.resizeCornerIndex != None:
                        self.resizeCornerIndex = None
                elif self.moving == True:
                    self.moving = False
            elif mode == "Draw label":
                self.rubberBand.hide()
                endPoint = self.mapToScene(event.pos()).toPoint()
                rect = QRect(self.initialPoint, endPoint).normalized()
                newBoxId = self.drawBox(rect)
                if newBoxId != None:
                    self.openPopUp(newBoxId)
                else:
                    print("Cant open label popup: boundingBox did not generate")
                self.point = QPoint() #resetting selected point data for next draw or select
            elif mode == "Erase":
                #send a hybrid select/erase request that identifies a box at a point and deletes it
                self.deleteBox(None) #FIXME move this into the select logic and have it delete actively selected boxes
                #also having a delete queue would be nice so people can undo deletes if they change their mind
    
    def openPopUp(self, boxID):
        print("tried to open popup")
        #opening popup
        #popup = LabelPopup(boxID)
        #popup.setWindowTitle("Enter label info")
        #popup.exec()
        pass

    def drawBox(self, rect):
        boxId = self.presenter.addBox(rect)
        return boxId
    
    def deleteBox(self, box):
        #FIXME instead of deleting by point select make this flexible by being able to delete already selected boxes.
        #self.presenter.deleteBox(box)
        print("FIXME")
        pass