import PyQt5.QtWidgets as qtw

class CanvasView:
    '''
    The canvas
    '''
    def __init__(self, parentWidget):
        self.presenter = CanvasPresenter()
        scene = self.presenter.getScene() #Is this going to let the view be updated live?
        self.view = qtw.QGraphicsView(scene)
        parentWidget.layout().addWidget(self.view)
    
    def refresh(self):
        pass