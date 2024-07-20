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
        self.origin = QPoint()
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
        #check if the event 
        if event.button() == Qt.LeftButton:
            if self.drawing == True:
                pass
            else:
                #mapping from the view coordinates to the scene to fix issues when resized
                self.origin = self.mapToScene(event.pos()).toPoint()
                #Adjusting back because the rubber band box needs the unadjusted values
                self.rubberBand.setGeometry(QRect(self.mapFromScene(self.origin), QSize())) #note the new QSize object has width and height of 0
                self.drawing = True
                self.rubberBand.show()
     
    def mouseMoveEvent(self, event):
        if not self.origin.isNull():
            self.rubberBand.setGeometry(QRect(self.mapFromScene(self.origin), event.pos()).normalized())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.drawing == False:
                pass
            else:
                self.rubberBand.hide()
                endPoint = self.mapToScene(event.pos()).toPoint()
                rect = QRect(self.origin, endPoint).normalized()
                self.drawBox(rect)
                self.origin = QPoint()
                self.drawing = False
    
    def drawBox(self, rect):
        #FIXME most of this needs to be changed to communicate with the presenter
        self.presenter.addBox(rect)
        
    
    def redrawBoxes(self):
        '''
        redraws boxes to canvas if one or multiple boxes have been altered or deleted
        '''
        pass