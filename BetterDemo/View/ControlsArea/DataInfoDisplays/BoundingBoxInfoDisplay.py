from View.ControlsArea.DataInfoDisplays.InfoDisplay import InfoDisplay
import PyQt5.QtWidgets as qtw

class BoundingBoxInfoDisplay(InfoDisplay):
    def __init(self, ):
        super().__init__(self, self.__addDisplayContent)
    
    
    def __addDisplayContent(self):
        self.frameNumberLabel = qtw.QLabel("BoundingBox: ")
        pass
    
    def refreshContents():
        pass