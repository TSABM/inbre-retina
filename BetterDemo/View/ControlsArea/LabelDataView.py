import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import QIntValidator
from Presenter.LabelDataPresenter import LabelDataPresenter
from View.ControlsArea.DataInfoDisplays.FrameInfoDisplay import FrameInfoDisplay
#from Model.LabelData import BoundingBox

class LabelDataView(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.labelToDisplay = None #FIXME
        self.presenter = LabelDataPresenter(self)
        self.__initUI()
        self.showing = False

        #self.loadLabelDataFields()
        
    ###Init helper methods ###

    def __initUI(self):
        layout = qtw.QVBoxLayout()
        self.setLayout(layout)

        # Metadata Dropdown
        self.__initMetadataFields()
        self.__addMetadataFieldsToLayout()

        # Frames Dropdown
        self.__initFrameDataFields()
        self.__addFramedataFieldsToLayout()

        # Bounding Boxes Dropdown
        self.__initBoundingBoxDataFields()
        self.__addBoundingBoxDataFieldsToLayout()

        # Cells Dropdown
        self.__initCellDataFields()
        self.__addCellDataFieldsToLayout()

        # Events Dropdown
        self.__initEventDataFields()
        self.__addEventDataFieldsToLayout()
        

        # Load Data Button
        self.refreshDataButton = qtw.QPushButton("Refresh Data")
        self.refreshDataButton.clicked.connect(self.reloadLabelData)
        layout.addWidget(self.refreshDataButton)

        #layout.addWidget(self.loadDataButton)
    
    def __addItemsToComboBox(self, comboBox : qtw.QComboBox, item : dict | None):
        #clear combobox?
        comboBox.clear()
        #add in "-"
        comboBox.insertItem(0, "-")
        self.__readItemsIntoComboBox(comboBox, item)
    
    def __readItemsIntoComboBox(self, comboBox : qtw.QComboBox, item : dict | None):
        if item == None:
            return
        for field in item:
            if isinstance(field, dict): #since much of the data is stored in sub dictionaries if you hit a dictionary call this method again to list the contents
                self.__addItemsToComboBox(comboBox, field)
            else:
                if isinstance(field, str):
                    comboBox.addItem(field)
                elif isinstance(field, int):
                    comboBox.addItem(str(field))
    
    def __initMetadataFields(self):
        self.fileNameLabel = qtw.QLabel("File name: No file open")
        self.totalFramesLabel = qtw.QLabel("Total frames: 0")
       
    def __initFrameDataFields(self):
        self.framesLabel = qtw.QLabel("Select Frames: ")
        self.framesDropdown = qtw.QComboBox()
        self.framesDropdown.currentTextChanged.connect(self.__frameComboBoxController)
        self.__addItemsToComboBox(self.framesDropdown, self.presenter.getFrames())
        #Frame info display
        self.frameInfoBox : FrameInfoDisplay = FrameInfoDisplay()
        
    def __initBoundingBoxDataFields(self):
        self.boundingBoxesLabel = qtw.QLabel("Select Bounding Boxes: ")
        self.boundingBoxesDropdown = qtw.QComboBox()
        #self.boundingBoxesDropdown.addItems() #FIXME
        self.__addItemsToComboBox(self.boundingBoxesDropdown, self.presenter.getBoundingBoxes())
        #BoundingBox info Display
        #self.boundingBoxInfoBox  = BoundingBoxInfoDisplay()
        
    def __initCellDataFields(self):
        self.cellsLabel = qtw.QLabel("Select Cells: ")
        self.cellsDropdown = qtw.QComboBox()
        #self.cellsDropdown.addItems() #FIXME
        self.__addItemsToComboBox(self.cellsDropdown, self.presenter.getCells())
        
    def __initEventDataFields(self):
        self.eventsLabel = qtw.QLabel("Select Events: ")
        self.eventsDropdown = qtw.QComboBox()
        #self.eventsDropdown.addItems() #FIXME
        self.__addItemsToComboBox(self.eventsDropdown, self.presenter.getEvents())
    
    ###Layout helper methods ###
     
    def __addMetadataFieldsToLayout(self):
        if not hasattr(self, "fileNameLabel"): return #FIXME you can make a more robust safety check than this
        self.layout().addWidget(self.fileNameLabel)
        self.layout().addWidget(self.totalFramesLabel)
    
    def __addFramedataFieldsToLayout(self):
        self.layout().addWidget(self.framesLabel)
        self.layout().addWidget(self.framesDropdown)
        self.layout().addWidget(self.frameInfoBox)
        self.__hideFrameInfoDisplay()
    
    def __addBoundingBoxDataFieldsToLayout(self):
        self.layout().addWidget(self.boundingBoxesLabel)
        self.layout().addWidget(self.boundingBoxesDropdown)
    
    def __addCellDataFieldsToLayout(self):
        self.layout().addWidget(self.cellsLabel)
        self.layout().addWidget(self.cellsDropdown)

        #Cell info Display
    def __addEventDataFieldsToLayout(self):
        self.layout().addWidget(self.eventsLabel)
        self.layout().addWidget(self.eventsDropdown)
    
    ### ###

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
        self.__addItemsToComboBox(self.framesDropdown, updated_frames)
        self.__addItemsToComboBox(self.boundingBoxesDropdown, updated_bounding_boxes)
        self.__addItemsToComboBox(self.cellsDropdown, updated_cells)
        self.__addItemsToComboBox(self.eventsDropdown, updated_events)    
        
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
    
    def __frameComboBoxController(self, mode):
        #if no frame is selected?
            #hide frame info display
        if mode == None or mode == "" or mode == "-":
            if not hasattr(self, "frameInfoBox"): return
            self.__hideFrameInfoDisplay()
        
        else:
            frameText = self.framesDropdown.currentText()
            frameNum = int(frameText)
            print(frameNum)
            self.frameInfoBox.setFrame(frameNum)
            self.__showFrameInfoDisplay()
            
    def __showFrameInfoDisplay(self):
        self.frameInfoBox.show()
        pass
    
    def __hideFrameInfoDisplay(self):
        self.frameInfoBox.hide()
        pass





    
        