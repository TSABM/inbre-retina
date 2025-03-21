from Presenter.AbstractPresenter import AbstractPresenter
#from View.MainControlsView import MainControlsView
from Model.masterMemory import MasterMemory
from Model.CanvasModel import CanvasModel

class MainControlsPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
        self.canvas : CanvasModel | None = MasterMemory.getCanvas()

    def __updateCanvas(self):
        '''
        the canvas very likely might not be initialized when the controls are. Call this to update it
        '''
        tempCanvas =  MasterMemory.getCanvas()
        if isinstance(tempCanvas, CanvasModel):
            print("updated canvas controls")
            self.canvas = tempCanvas
            return True
        else:
            print("canvas is still None, could not update controls")
            return False

    def refresh(self):
        super().refresh()
    