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

        #TEMP CODE loading a pixmap
        #self.image = QImage(image_path)
        #self.pixmap = QPixmap.fromImage(self.image)
        #self.pixmap_item = QGraphicsPixmapItem(self.pixmap)
        #self.scene.addItem(self.pixmap_item)

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
        self.setScene(canvas.getScene())

    def mousePressEvent(self, event):
        #check if the event 
        if event.button() == Qt.LeftButton:
            if self.drawing == True:
                pass
            else:
                self.origin = event.pos()
                self.rubberBand.setGeometry(QRect(self.origin, QSize())) #note the new QSize object has width and height of 0
                self.drawing = True
                self.rubberBand.show()
     
    def mouseMoveEvent(self, event):
        if not self.origin.isNull():
            self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.drawing == False:
                pass
            else:
                self.rubberBand.hide()
                rect = self.rubberBand.geometry()
                self.drawBox(rect)
                self.origin = QPoint()
                self.drawing = False
    
    def drawBox(self, rect):
        #FIXME most of this needs to be changed to communicate with the presenter
        self.presenter.addBox(rect)
        #painter = QPainter(self.pixmap)
        #painter.setPen(QColor(255, 0, 0))
        #painter.drawRect(rect)
        #painter.end()
        #self.pixmap_item.setPixmap(self.pixmap)
    
    def redrawBoxes(self):
        '''
        redraws boxes to canvas if one or multiple boxes have been altered or deleted
        '''
        pass