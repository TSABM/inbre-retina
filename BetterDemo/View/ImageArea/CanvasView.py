import PyQt5.QtWidgets as qtw

class CanvasView(qtw.QGraphicsView):
    '''
    The canvas
    '''
    def __init__(self):
        #self.presenter = CanvasPresenter()
        #scene = self.presenter.getScene() #Is this going to let the view be updated live?
        #self.view = qtw.QGraphicsView(scene)
        #parentWidget.layout().addWidget(self.view)
        super().__init__()
        
    
    def setScene(self, scene):
        self.setScene(scene)