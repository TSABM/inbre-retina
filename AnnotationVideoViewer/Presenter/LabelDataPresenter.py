from Presenter.AbstractPresenter import AbstractPresenter
from Model.LabelData import LabelData
from Model.masterMemory import MasterMemory
from Presenter.CanvasPresenter import CanvasPresenter

class LabelDataPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
        self.model : LabelData | None = None

    def getLabelData(self):
        if self.__verifyFileOpen__() == False:
            return None
        return self.model #fixme if model isnt saved by reference this will create unexpected behavior
       
    def __verifyFileOpen__(self):
        labelData = MasterMemory.getLabelData()
        if labelData == None:
            print("label data model is not initalized")
            return False
        else:
            self.model = labelData
            return True