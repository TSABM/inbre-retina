from Presenter.AbstractPresenter import AbstractPresenter
from Model.masterMemory import MasterMemory
from Model.LabelData import LabelData

class InfoDisplayPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
    
    def getFrame(self, frameNumber : int):
        labelData : LabelData = MasterMemory.getLabelData()
        return labelData.getFrame(frameNumber)
    
    def refresh(self):
        pass