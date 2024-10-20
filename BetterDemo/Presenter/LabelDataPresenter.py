from Presenter.AbstractPresenter import AbstractPresenter
from Model.LabelData import LabelData
from Model.masterMemory import MasterMemory
from Presenter.CanvasPresenter import CanvasPresenter
from abc import ABC, abstractmethod

class AbstractLabelData(ABC):
    @abstractmethod
    def setLabelToDisplay():
        pass
    @abstractmethod
    def displayLabelData():
        pass

class LabelDataPresenter(AbstractPresenter):
    def __init__(self, view : AbstractLabelData):
        super().__init__(view)
        #send label data area to the master memory
        self.model : LabelData = None
        #MasterMemory.setLabels(self)
        #self.registerNewSubscriber("labelData", self)
        #self.addSubscriber("canvas")

    def refresh(self):
        super().refresh()
        if self.__verifyFileOpen__() == False:
            return
        #FIXME 

    def __verifyFileOpen__(self):
        labelData = MasterMemory.getLabelData()
        if labelData == None:
            print("label data model is not initalized")
            return False
        else:
            self.model = labelData
            return True

    def getFrames(self):
        if self.__verifyFileOpen__() == False:
            return
        return self.model.getFrames()

    def getBoundingBoxes(self):
        if self.__verifyFileOpen__() == False:
            return
        return self.model.getBoundingBoxes()

    def getCells(self):
        if self.__verifyFileOpen__() == False:
            return
        return self.model.getCells()

    def getEvents(self):
        if self.__verifyFileOpen__() == False:
            return
        return self.model.getEvents()

    def getCellTypes(self):
        if self.__verifyFileOpen__() == False:
            return
        return self.model.getCellTypes()

    def getEventTypes(self):
        if self.__verifyFileOpen__() == False:
            return
        return self.model.getEventTypes()

    def getMetadata(self):
        if self.__verifyFileOpen__() == False:
            return
        return self.model.getMetaData()
    
    def setLabelData(self, labelData : LabelData):
        self.model = labelData
    
    def getMaxXVal(self):
        return 9999 #temp number

    def getMaxYVal(self):
        return 9999
    
    def getLargestBoxVal(self):
        self.model.getLargestBoxIdVal()