import PyQt5.QtWidgets as qtw

class CanvasView:
    '''
    The canvas
    '''
    def __init__(self, parentWidget):
        scene = qtw.QGraphicsScene(0, 0, 400, 200)
        view = qtw.QGraphicsView(scene)
        parentWidget.layout().addWidget(view)