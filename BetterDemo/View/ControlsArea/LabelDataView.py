import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import QIntValidator
from Presenter.LabelDataPresenter import LabelDataPresenter
from PyQt5.QtGui import QColor, QPalette
from abc import ABC, abstractmethod
#from Model.LabelData import BoundingBox

class LabelDataView(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.labelToDisplay = None #FIXME
        self.presenter = LabelDataPresenter(self)
        self.initUI()
        self.showing = False

        #self.loadLabelDataFields()
        

    def initUI(self):
        layout = qtw.QVBoxLayout()

        # Metadata Dropdown
        self.fileNameLabel = qtw.QLabel("File name: No file open")
        self.totalFramesLabel = qtw.QLabel("Total frames: 0")
        layout.addWidget(self.fileNameLabel)
        layout.addWidget(self.totalFramesLabel)

        # Frames Dropdown
        self.framesLabel = qtw.QLabel("Select Frames: ")
        self.framesDropdown = qtw.QComboBox()
        #self.framesDropdown.addItems()#FIXME
        self.__addItemsToComboBox__(self.framesDropdown, self.presenter.getFrames())
        layout.addWidget(self.framesLabel)
        layout.addWidget(self.framesDropdown)

        #Frame info display
        self.frameInfoBox = FrameInfoDisplay()
        layout.addWidget(self.frameInfoBox)

        # Bounding Boxes Dropdown
        self.boundingBoxesLabel = qtw.QLabel("Select Bounding Boxes: ")
        self.boundingBoxesDropdown = qtw.QComboBox()
        #self.boundingBoxesDropdown.addItems() #FIXME
        self.__addItemsToComboBox__(self.boundingBoxesDropdown, self.presenter.getBoundingBoxes())
        layout.addWidget(self.boundingBoxesLabel)
        layout.addWidget(self.boundingBoxesDropdown)
        
        #BoundingBox info Display

        # Cells Dropdown
        self.cellsLabel = qtw.QLabel("Select Cells: ")
        self.cellsDropdown = qtw.QComboBox()
        #self.cellsDropdown.addItems() #FIXME
        self.__addItemsToComboBox__(self.cellsDropdown, self.presenter.getCells())
        layout.addWidget(self.cellsLabel)
        layout.addWidget(self.cellsDropdown)

        #Cell info Display

        # Events Dropdown
        self.eventsLabel = qtw.QLabel("Select Events: ")
        self.eventsDropdown = qtw.QComboBox()
        #self.eventsDropdown.addItems() #FIXME
        self.__addItemsToComboBox__(self.eventsDropdown, self.presenter.getEvents())
        layout.addWidget(self.eventsLabel)
        layout.addWidget(self.eventsDropdown)

        #Event info Display

        # Load Data Button
        self.refreshDataButton = qtw.QPushButton("Refresh Data")
        self.refreshDataButton.clicked.connect(self.reloadLabelData)
        layout.addWidget(self.refreshDataButton)

        #layout.addWidget(self.loadDataButton)

        self.setLayout(layout)

    def reloadLabelData(self):
        '''
        reloads data
        '''
        #clearing previous entries
        self.framesDropdown.clear()
        self.boundingBoxesDropdown.clear()
        self.cellsDropdown.clear()
        self.eventsDropdown.clear()

        # Re-fetch the updated data from the presenter
        #updated_metadata = self.presenter.getMetadata()
        updated_frames = self.presenter.getFrames()
        updated_bounding_boxes = self.presenter.getBoundingBoxes()
        updated_cells = self.presenter.getCells()
        updated_events = self.presenter.getEvents()

        # Re-populate the dropdowns with the new data
        self.fileNameLabel.setText("File name: " + self.getFileName())
        self.totalFramesLabel.setText("Total frames: " + self.getFrameCount())
        self.__addItemsToComboBox__(self.framesDropdown, updated_frames)
        self.__addItemsToComboBox__(self.boundingBoxesDropdown, updated_bounding_boxes)
        self.__addItemsToComboBox__(self.cellsDropdown, updated_cells)
        self.__addItemsToComboBox__(self.eventsDropdown, updated_events)    
        
    
    def __addItemsToComboBox__(self, comboBox : qtw.QComboBox, item : dict | None):
        if item == None:
            return
        for field in item:
            if isinstance(field, dict):
                self.__addItemsToComboBox__(comboBox, field)
            else:
                if isinstance(field, str):
                    comboBox.addItem(field)
                elif isinstance(field, int):
                    comboBox.addItem(str(field))
    
    def getFileName(self):
        filename = "No file open" #default
        metadata : dict = self.presenter.getMetadata()
        if metadata is None:
            pass
        else:
            storedName = metadata.get("fileName")
            if storedName != None:
                filename = storedName

        return filename
    
    def getFrameCount(self): 
        frames = "0"  # Default frame count
        metadata: dict = self.presenter.getMetadata()
    
        if metadata is None:
            pass
        else:
            storedFrames = metadata.get("frameTotal")
            if storedFrames is not None:
                frames = str(storedFrames)
    
        return frames
    
    def __showFrameInfoDisplay():
        pass

class InfoDisplay(qtw.QWidget):
    def __init__(self, addDisplayContentFunction):
        self.layout = qtw.QVBoxLayout()
        
        #set a grey background
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("grey"))
        self.setPalette(palette)
        
        addDisplayContentFunction()
        
        self.setLayout(self.layout)


class FrameInfoDisplay (InfoDisplay):
    def __init__(self):
        super.__init__(self.__addDisplayContent)
    
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
    
    def refreshContents():
        #update frame number label
        #update box id list
        #update eventid list
        pass
        