import PyQt5.QtWidgets as qtw

from Presenter.CanvasPresenter import CanvasPresenter
from View.AbstractView import AbstractView

class CanvasView(AbstractView):
    '''
    The canvas
    '''
    def __init__(self):
        super().__init__(qtw.QGraphicsView)
        self.presenter = CanvasPresenter(self)
        self.getCanvas()

        print("canvas initalized")
    
    def getCanvas(self):
        canvas = self.presenter.getCanvas()
        self.viewWidget.setScene(canvas.getScene())