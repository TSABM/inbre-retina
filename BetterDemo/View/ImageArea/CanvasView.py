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
    
    def getScene(self):
        scene = self.presenter.getScene()
        self.setScene(scene)