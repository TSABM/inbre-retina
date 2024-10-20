import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import QIntValidator
from Presenter.LabelDataPresenter import LabelDataPresenter
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
        self.metadataLabel = qtw.QLabel("Select Metadata: ")
        self.metadataDropdown = qtw.QComboBox()
        #self.metadataDropdown.addItem("All Metadata")  # You can add specific chunks if needed
        self.__addItemsToComboBox__(self.metadataDropdown, self.presenter.getMetadata())
        layout.addWidget(self.metadataLabel)
        layout.addWidget(self.metadataDropdown)

        # Frames Dropdown
        self.framesLabel = qtw.QLabel("Select Frames: ")
        self.framesDropdown = qtw.QComboBox()
        #self.framesDropdown.addItems()#FIXME
        self.__addItemsToComboBox__(self.framesDropdown, self.presenter.getFrames())
        layout.addWidget(self.framesLabel)
        layout.addWidget(self.framesDropdown)

        # Bounding Boxes Dropdown
        self.boundingBoxesLabel = qtw.QLabel("Select Bounding Boxes: ")
        self.boundingBoxesDropdown = qtw.QComboBox()
        #self.boundingBoxesDropdown.addItems() #FIXME
        self.__addItemsToComboBox__(self.boundingBoxesDropdown, self.presenter.getBoundingBoxes())
        layout.addWidget(self.boundingBoxesLabel)
        layout.addWidget(self.boundingBoxesDropdown)

        # Cells Dropdown
        self.cellsLabel = qtw.QLabel("Select Cells: ")
        self.cellsDropdown = qtw.QComboBox()
        #self.cellsDropdown.addItems() #FIXME
        self.__addItemsToComboBox__(self.cellsDropdown, self.presenter.getCells())
        layout.addWidget(self.cellsLabel)
        layout.addWidget(self.cellsDropdown)

        # Events Dropdown
        self.eventsLabel = qtw.QLabel("Select Events: ")
        self.eventsDropdown = qtw.QComboBox()
        #self.eventsDropdown.addItems() #FIXME
        self.__addItemsToComboBox__(self.eventsDropdown, self.presenter.getEvents())
        layout.addWidget(self.eventsLabel)
        layout.addWidget(self.eventsDropdown)

        # Load Data Button
        self.refreshDataButton = qtw.QPushButton("Refresh Data")
        self.refreshDataButton.clicked.connect(self.reloadLabelData)

        #layout.addWidget(self.loadDataButton)

        self.setLayout(layout)

    
    def reloadLabelData(self):
        '''
        reloads data
        '''
        # unsure how to handle this
        self.metadataDropdown.clear()
        self.framesDropdown.clear()
        self.boundingBoxesDropdown.clear()
        self.cellsDropdown.clear()
        self.eventsDropdown.clear()

        # Re-fetch the updated data from the presenter
        updated_metadata = self.presenter.getMetadata()
        updated_frames = self.presenter.getFrames()
        updated_bounding_boxes = self.presenter.getBoundingBoxes()
        updated_cells = self.presenter.getCells()
        updated_events = self.presenter.getEvents()

        # Re-populate the dropdowns with the new data
        self.__addItemsToComboBox__(self.metadataDropdown, updated_metadata)
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
