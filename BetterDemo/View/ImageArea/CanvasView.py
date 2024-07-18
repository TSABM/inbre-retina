import PyQt5.QtWidgets as qtw

from Presenter.CanvasPresenter import CanvasPresenter

class CanvasView(qtw.QGraphicsView):
    '''
    The canvas
    '''
    def __init__(self):
        super().__init__()
        self.presenter = CanvasPresenter(self)
        self.setCanvas()

        print("canvas initalized")
    
    def setCanvas(self):
        canvas = self.presenter.getCanvas()
        self.setScene(canvas.getScene())
    
    def __onClick():
        #check if drawing mode is already active (if so do nothing)
        #else
            # record start corner
            # begin draw mode
        pass
    def __onDrag():
        #grab mouse coords (will we need to worry about out of bounds mouse exploration?)
        #redraw the rectangle in progress
            #delete the old rectangle
            #draw the new rectangle 
        pass
    def __onRelease():
        #make sure drawing mode is active (if not something went wrong?)
        #else
            #record the end corner
            #end draw mode
        pass