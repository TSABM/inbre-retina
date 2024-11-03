from InfoDisplay import InfoDisplay
import PyQt5.QtWidgets as qtw
from Model.LabelData import Frame


class FrameInfoDisplay(InfoDisplay):
    def __init__(self, frame):
        super.__init__(self.__addDisplayContent)
        self.frame : Frame = frame
    
    def __addDisplayContent(self):
        self.frameNumberLabel = qtw.QLabel("Frame: ")
        self.boxIDsLabel = qtw.QLabel("Box Ids: ")
        self.boxIDList = qtw.QListWidget()
        
        self.eventIDsLabel = qtw.QLabel("Event Ids: ")
        self.eventIDList = qtw.QListWidget()
        
        self.layout().addWidget(self.frameNumberLabel)
        self.layout().addWidget(self.boxIDsLabel)
        self.layout().addWidget(self.boxIDList)
        self.layout().addWidget(self.eventIDsLabel)
        self.layout().addWidget(self.eventIDList)
    
    def refreshContents(self):
        #FIXME grab an updated version of frame the curr one may be outdated presenter.updateCurrFrame?
        #update frame number label
        self.frameNumberLabel.setText("Frame : " + self.frame.getFrameNumber())
        #update box id list
        boxIDs = self.frame.getBoxIds()
        self.boxIDList.addItems(boxIDs)
        #update eventid list
        eventIDs = self.frame.getEventIds()
        self.eventIDList.addItems(eventIDs)