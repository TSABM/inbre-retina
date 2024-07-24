import PyQt5.QtWidgets as qtw

from PyQt5.QtCore import QRect, QPoint, Qt, QSize
from Presenter.CanvasPresenter import CanvasPresenter
from PyQt5.QtGui import QPixmap, QPainter, QColor

class CanvasView(qtw.QGraphicsView):
    '''
    The canvas
    '''
    def __init__(self):
        super().__init__()
        #init presenter and request QGraphicsScene
        self.presenter = CanvasPresenter(self)
        self.setCanvas()

        #init variables for drawing labels
        self.drawing = False
        self.resizing = False
        self.moving = False
        self.initialPoint = QPoint()
        self.resizeCorner = None
        self.rubberBand = qtw.QRubberBand(qtw.QRubberBand.Rectangle, self)

        #turn mouse tracking on
        self.setMouseTracking(True)
        #setting render hints (askes engine to try to antialias and use smooth pixmap transforming)
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        print("canvas initalized")
    
    def setCanvas(self):
        canvas = self.presenter.getCanvas()
        self.setScene(canvas)

    def mousePressEvent(self, event):
        #check if the event is a left click
        if event.button() == Qt.LeftButton:
            mode = self.presenter.getInteractionMode()
            self.initialPoint = self.mapToScene(event.pos()).toPoint()
            if mode == "Select label":
                if self.presenter.selectResizeCorner() != None:
                    pass
                self.presenter.selectBox(self.initialPoint)
            elif mode == "Draw label":
                #Adjusting back because the rubber band box needs the unadjusted values
                self.rubberBand.setGeometry(QRect(self.mapFromScene(self.initialPoint), QSize())) #note the new QSize object has width and height of 0
                self.rubberBand.show()
            else:
                print("invalid interaction mode ", mode)
     
    def mouseMoveEvent(self, event):
        mode = self.presenter.getInteractionMode()
        new_pos = self.mapToScene(event.pos()).toPoint()
        if mode == "Select label":
            if self.resizing == True and self.resizeCorner != None:
                self.presenter.resizeBox(new_pos, self.resizeCorner)
            elif self.resizing == False:
                self.presenter.moveBox(new_pos)
        elif mode == "Draw label":
            if not self.point.isNull():
                self.rubberBand.setGeometry(QRect(self.mapFromScene(self.initialPoint), self.mapFromScene(new_pos)).normalized())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            mode = self.presenter.getInteractionMode()
            if mode == "Select label":
                if self.resizing == True:
                    self.resizing = False
            elif mode == "Draw label":
                self.rubberBand.hide()
                endPoint = self.mapToScene(event.pos()).toPoint()
                rect = QRect(self.initialPoint, endPoint).normalized()
                self.drawBox(rect)
                self.point = QPoint() #not sure the need for this
    
    def drawBox(self, rect):
        self.presenter.addBox(rect)