from Presenter.AbstractPresenter import AbstractPresenter
from Model.masterMemory import MasterMemory
from Model.CanvasModel import CanvasModel
from Model.LabelData import LabelData
#from Model.AcceptedFormats.SimpleMovie import SimpleMovie
from Model.AcceptedFormats.CompatableVideo import CompatableVideo

class MainControlsPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
        self.canvas: CanvasModel | None = MasterMemory.getCanvas()

    def __updateCanvas(self):
        """Update canvas reference if not initialized and return whether it's valid."""
        self.canvas = MasterMemory.getCanvas()

    def __isValidCanvas(self) -> bool:
        """Ensure the canvas and its source are valid."""
        if self.canvas == None:
            self.__updateCanvas()
            if isinstance(self.canvas, CanvasModel):
                return True
            print("Canvas is not initalized, cannot do requested menu function")
            return False
        else:
            if isinstance(self.canvas, CanvasModel):
                return True
        return False

    def __isValidMovie(self):
        if self.__isValidCanvas():
            if isinstance(self.canvas.sourceToDisplay, CompatableVideo): # type: ignore
                return True
            print("Canvas is initalized but source is not a valid movie format. Cannot do requested menu function")
        return False

    def playMovie(self):
        self.__updateCanvas()
        if self.__isValidMovie():
            self.canvas.playMovie() # type: ignore

    def pauseMovie(self):
        self.__updateCanvas()
        if self.__isValidMovie():
            self.canvas.pauseMovie() # type: ignore

    def stepForward(self):
        self.__updateCanvas()
        if self.__isValidMovie():
            self.canvas.stepForward() # type: ignore

    def stepBackward(self):
        self.__updateCanvas()
        if self.__isValidMovie():
            self.canvas.stepBackward() # type: ignore

    def jumpToFrameNum(self, frameNum: int):
        self.__updateCanvas()
        if self.__isValidMovie():
            self.canvas.jumpToFrame(frameNum) # type: ignore
        
    def mapCellTypeToColor(self, cellTypeToBind, color):
        self.__updateCanvas()
        if self.canvas != None:
            self.canvas.mapCellToColor(cellTypeToBind, color)

    def getColors(self):
        self.__updateCanvas()
        if self.canvas != None:
            return self.canvas.getColors()
        return None
    
    def getCellTypes(self):
        labelData = MasterMemory.getLabelData()
        if isinstance(labelData, LabelData):
            cellTypes = labelData.getCellTypes()
            return cellTypes
        return None