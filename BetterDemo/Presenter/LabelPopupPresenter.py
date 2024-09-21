from Presenter.AbstractPresenter import AbstractPresenter
from Model.LabelPopupModel import LabelPopupModel

class LabelPopupPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
        self.model = LabelPopupModel()
        pass

    def refresh(self):
        pass

    def submitData(self, data):
        self.model.submitData(boundingBoxes, cellsToAdd, eventsToAdd)
    

    #existing data needs to be called up here so label popup can know what data is already existing and assotiated with each displayed item? 
    #self.model isnt the way though, either access label data or go through master mem (probably the latter.)
    def getCellIDs(self):
        # Retrieve the list of cell IDs
        return self.model.getCellIDs()
    
    def getEventIDs(self):
        # Retrieve the list of event IDs
        return self.model.getEventIDs()

    '''
    def getBoundingBoxes(self):
        # Retrieve the bounding boxes
        return self.model.get
    '''
    def getCellTypes(self):
        return self.model.getCellTypes()
    
    def getEventTypes(self):
        return self.model.getEventTypes()

    def getFrames(self):
        # Retrieve the frames
        return self.model.data["Frames"]

    def getMetaData(self):
        # Retrieve the metadata
        return self.model.data["MetaData"]