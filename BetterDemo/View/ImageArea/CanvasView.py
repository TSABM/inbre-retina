import PyQt5.QtWidgets as qtw

from Presenter.CanvasPresenter import CanvasPresenter

class CanvasView(qtw.QGraphicsView):
    '''
    The canvas
    '''
    def __init__(self):
        super().__init__()
        self.presenter = CanvasPresenter(self)
        self.getScene()

        print("canvas initalized")
    
    def getCanvas(self):
        canvas = self.presenter.getCanvas()
        self.setScene(canvas.getScene())