from Presenter.AbstractPresenter import AbstractPresenter
from Model.LabelData import LabelData
from Model.masterMemory import MasterMemory
from Presenter.CanvasPresenter import CanvasPresenter

class LabelDataPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
        #send label data area to the master memory
        self.model : LabelData = LabelData()
        MasterMemory.setLabels(self)
        #self.registerNewSubscriber("labelData", self)
        #self.addSubscriber("canvas")

    def refresh(self):
        super().refresh()
        print("attempted to refresh label data")
        canvasPresenter : CanvasPresenter = MasterMemory.getCanvas()
        label = canvasPresenter.getSelectedLabel()
        self.view.setLabelToDisplay(label)
        self.view.displayLabelData()

    def getModel(self):
        return self.model
    
    def setLabelData(self, labelData : LabelData):
        self.model = labelData
    
    def getMaxXVal(self):
        return 9999 #temp number

    def getMaxYVal(self):
        return 9999
    
    def getLargestBoxVal(self):
        self.model.getLargestBoxIdVal()