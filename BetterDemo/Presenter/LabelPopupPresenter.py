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
        self.model.submitData()
    
    def getCellIDs(self):
        # Retrieve the list of cell IDs
        return list(self.model.data["Cells"].keys())
    
    def getEventIDs(self):
        # Retrieve the list of event IDs
        return list(self.model.data["Events"].keys())

    def getBoundingBoxes(self):
        # Retrieve the bounding boxes
        return self.model.data["BoundingBoxes"]
    
    def getFrames(self):
        # Retrieve the frames
        return self.model.data["Frames"]

    def getMetaData(self):
        # Retrieve the metadata
        return self.model.data["MetaData"]