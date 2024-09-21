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

        self.existingCells : set= self.presenter.getCellIDs()
        self.existingEvents : set= self.presenter.getEventIDs()
        self.existingCellTypes : set = self.presenter.getCellTypes()
        self.existingEventTypes : set = self.presenter.getEventTypes()

        self.newCellType : str = ""
        self.newEventType : str = ""
        self.cellToAddToList = None
        self.newCells = set()
        self.selectedCells = set()

        self.eventToAddToList = None
        self.newEvents = set()
        self.selectedEvents = set()

        #show box ID
        self.boxIDLabel = qtw.QLabel("BoxID: ")
        self.boxIDField = qtw.QLineEdit()
        self.boxIDField.setText(boxID)
        self.boxIDField.setReadOnly(True)
        self.layout.addWidget(self.boxIDLabel)
        self.layout.addWidget(self.boxIDField)

        #ask for cell(s)
        self.cellsLabel = qtw.QLabel("Cell(s): ")
        self.cellsDropdown = qtw.QComboBox()
        self.cellsDropdown.addItems(self.existingCells)
        self.cellsDropdown.addItem("-")
        self.cellsDropdown.addItem("Add new cell")
        self.cellsDropdown.currentTextChanged.connect(self.cellSelected)
        self.layout.addWidget(self.cellsLabel)
        self.layout.addWidget(self.cellsDropdown)
            
        #Defining a new cell fields
        self.newCellIDLabel = qtw.QLabel("New cell ID: ")
        self.newCellIDField = qtw.QLineEdit()
        self.newCellIDField.setReadOnly(True)
        self.layout.addWidget(self.newCellIDLabel)
        self.layout.addWidget(self.newCellIDField)
        
        self.newCellTypeLabel = qtw.QLabel("New cell type: ")
        self.newCellTypeField = qtw.QLineEdit()
        self.newCellTypeField.textChanged.connect(self.stageCustomCellName) #FIXME?
        self.layout.addWidget(self.newCellTypeLabel)
        self.layout.addWidget(self.newCellTypeField)

        self.hideNewCellFields()

        #add cell button
        self.includeCellButton = qtw.QPushButton()
        self.includeCellButton.setText("Include cell")
        self.includeCellButton.pressed.connect(self.addCellToList)
        self.layout.addWidget(self.includeCellButton)

        #list the included cells
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
    
    def addCellToList(self):
        if self.cellToAddToList != None:
            self.selectedCells.add(self.cellToAddToList)
            self.cellList.clear()
            self.cellList.addItems(self.selectedCells)
    
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

    def stageCustomCellName(self, customName):
        self.cellToAddToList = customName

    def eventSelected(self):
        pass

    def submitData(self):
        #grab the data
        
        boxID = self.boxIDField.text()
        boxDimensions = self.rectangle.getRect()
        #cellIDs
        newCellsToAdd = self.newCells
        cellIDs = self.selectedCells
        #eventIDs
        newEventsToAdd = self.newEvents
        eventIDs = self.selectedEvents

        self.presenter.submitData(boxID, boxDimensions, newCellsToAdd, cellIDs, newEventsToAdd, eventIDs)
                
        pass