import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt, QRect
from Presenter.LabelPopupPresenter import LabelPopupPresenter

class LabelPopup(qtw.QDialog):
    '''
    The popup that appears when a new bounding box is being drawn on the image. If the user fills out the fields a valid label data item can
    be created.
    '''
    def __init__(self, boxID, rectangle : QRect):
        super().__init__()
        self.presenter = LabelPopupPresenter(self)
        self.setWindowTitle("Classify the selection")

        self.rectangle : QRect = rectangle

        self.layout : qtw.QLayout = qtw.QVBoxLayout()
        self.setLayout(self.layout)

        #definining some quick references to data in label data so users can include existing cells and events in the new bounding box
        self.frameNum : int = self.presenter.getFrameNumber()
        self.existingCells : set= self.presenter.getCellIDs()
        self.existingEvents : set= self.presenter.getEventIDs()
        self.existingCellTypes : set = self.presenter.getCellTypes()
        self.existingEventTypes : set = self.presenter.getEventTypes()

        #this is where unfinished new cell types are stored before they can be "staged"
        self.newCellType : str = ""
        self.newEventType : str = ""

        #these are "staging ground" variables where completed items to be assotiated with the box wait for the user to confirm the relationship
        self.cellTypeToAddToList = None
        self.eventTypeToAddToList = None
        self.cellToAddToList = None
        self.eventToAddToList = None

        #this is where items that have been assotiated with the box here in the popup window are stored before being submitted to the master memory
        self.newCellTypes = set()
        self.newEventTypes = set()
        self.includedCells = dict()
        self.includedEvents = dict()

        #Add popup UI elements
        self.addBoxIDField(boxID)
        self.addCellInclusionFields()

        self.addCellCreationFields()
        self.hideNewCellFields()

        #the add cell button (creates a new cell and adds it to the included list)
        self.includeCellButton = qtw.QPushButton()
        self.includeCellButton.setText("Include cell")
        self.includeCellButton.pressed.connect(self.includeCellInList)
        self.layout.addWidget(self.includeCellButton)

        #a list of the included cells
        self.cellListLabel = qtw.QLabel("Included cells:")
        self.cellList = qtw.QListWidget()
        self.layout.addWidget(self.cellListLabel)
        self.layout.addWidget(self.cellList)

        #ask for events(s)
        self.eventsLabel = qtw.QLabel("Add events(s): ")
        self.eventsDropdown = qtw.QComboBox()
        self.eventsDropdown.addItems(self.existingEvents)
        self.eventsDropdown.addItem("Add new event")
        self.eventsDropdown.currentTextChanged.connect(self.eventSelected)
        self.layout.addWidget(self.eventsLabel)
        self.layout.addWidget(self.eventsDropdown)
            
        #Defining new event fields
        self.newEventIDLabel = qtw.QLabel("New event ID: ")
        self.newEventIDField = qtw.QLineEdit()
        self.newEventIDField.setReadOnly(True)
        self.layout.addWidget(self.newEventIDLabel)
        self.layout.addWidget(self.newEventIDField)
        
        self.newEventTypeLabel = qtw.QLabel("New event type: ")
        self.newEventTypeField = qtw.QLineEdit()
        #self.newEventTypeField.textChanged.connect() #FIXME?
        
        #SUBMIT BUTTON
        #once all data set user presses this to finalize the cell and box
        self.submitButton = qtw.QPushButton()
        self.submitButton.setText("Submit label data")
        self.submitButton.pressed.connect(self.submitData)
        self.layout.addWidget(self.submitButton)
    
    def addBoxIDField(self, boxID):
        self.boxIDLabel = qtw.QLabel("BoxID: ")
        self.boxIDField = qtw.QLineEdit()
        self.boxIDField.setText(boxID)
        self.boxIDField.setReadOnly(True)
        self.layout.addWidget(self.boxIDLabel)
        self.layout.addWidget(self.boxIDField)
    
    def addCellInclusionFields(self):
        self.cellsLabel = qtw.QLabel("Included cell(s): ")
        self.cellsDropdown = qtw.QComboBox()
        self.cellsDropdown.addItems(self.existingCells)
        self.cellsDropdown.addItem("-")
        self.cellsDropdown.addItem("Add new cell")
        self.cellsDropdown.currentTextChanged.connect(self.cellSelected)
        self.layout.addWidget(self.cellsLabel)
        self.layout.addWidget(self.cellsDropdown)
    
    def addCellCreationFields(self):
        self.newCellIDLabel = qtw.QLabel("New cell ID: ")
        self.newCellIDField = qtw.QLineEdit()
        self.newCellIDField.setReadOnly(True)
        self.layout.addWidget(self.newCellIDLabel)
        self.layout.addWidget(self.newCellIDField)
        
        self.newCellTypeLabel = qtw.QLabel("Cell type: ")
        self.cellTypesDropdown = qtw.QComboBox()
        self.cellTypesDropdown.addItems(self.existingCellTypes)
        self.cellTypesDropdown.addItem("-")
        self.cellTypesDropdown.addItem("Add new cell type")
        self.cellTypesDropdown.currentTextChanged.connect(self.cellTypeSelected)

        self.newCellTypeField = qtw.QLineEdit()
        self.newCellTypeField.textChanged.connect(self.stageCustomCellName) #FIXME?
        self.layout.addWidget(self.newCellTypeLabel)
        self.layout.addWidget(self.newCellTypeField)

    def generateCellID(self):
        #quickly scan the existing cells and grab the largest number, add 1 then return a new id
        largestValue = 0
        for id in self.existingCells:
            x = id.split('_')[1]
            x = int(x)
            if x > largestValue:
                largestValue = x
        newValue = largestValue + 1
        newID = "cell_" + str(newValue)
        return newID

    def showNewCellFields(self):
        #get the cell Id
        newID = self.generateCellID()
        self.newCellIDField.setText(newID)

        #show the fields
        self.newCellIDLabel.show()
        self.newCellIDField.show()
        self.newCellTypeLabel.show()
        self.newCellTypeField.show()
    
    def hideNewCellFields(self):
        self.newCellIDLabel.hide()
        self.newCellIDField.hide()
        self.newCellTypeLabel.hide()
        self.newCellTypeField.hide()
    
    def includeCellInList(self):
        if self.cellToAddToList != None:
            self.includedCells.add(self.cellToAddToList)
            self.cellList.clear()
            self.cellList.addItems(self.includedCells)
    
    def hideNewCellTypesFields(self):
        pass #FIXME

    def showNewCellTypesFields(self, mode):
        pass #FIXME

    def showNewEventFields(self):
        #get the cell Id
        newID = self.generateCellID()
        self.newCellIDField.setText(newID)

        #show the fields
        self.newCellIDLabel.show()
        self.newCellIDField.show()
        self.newCellTypeLabel.show()
        self.newCellTypeField.show()

    def cellSelected(self, mode):
        if mode == "-":
            #do nothing
            self.cellToAddToList = None
        elif mode == "Add new cell":
            #show new cell fields
            self.showNewCellFields()
            self.cellToAddToList = None
        else:
            self.hideNewCellFields()
            self.cellToAddToList = mode

    def cellTypeSelected(self, mode):
        if mode == "-":
            #do nothing
            self.hideNewCellFields()
            self.cellTypeToAddToList = None
        elif mode == "Add new cell type":
            #show new cell fields
            self.showNewCellTypesFields()
            self.cellTypeToAddToList = None
        else:
            self.hideNewCellFields()
            self.cellTypeToAddToList = mode

    def stageCustomCellName(self, customName):
        self.cellToAddToList = customName

    def eventSelected(self):
        pass

    def submitData(self):
        #grab the data
        
        boxID = self.boxIDField.text()
        boxDimensions : QRect = self.rectangle.getRect()

        self.presenter.submitData(boxID, self.frameNum, boxDimensions.getRect(), self.includedCells, self.includedEvents, self.newCellTypes)