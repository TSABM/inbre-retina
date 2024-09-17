import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt, QRect
from Presenter.LabelPopupPresenter import LabelPopupPresenter

class LabelPopup(qtw.QDialog):
    '''
    The popup that appears when a new bounding box is being drawn on the image. If the user fills out the fields a valid label data item can
    be created and recorded.
    '''
    def __init__(self, boxID, rectangle : QRect):
        super().__init__()
        self.presenter = LabelPopupPresenter()
        self.setWindowTitle("Classify the selection")

        self.rectangle : QRect = rectangle

        self.setLayout(qtw.QVBoxLayout())

        #already existing cells and events in the files label data. Needed to ensure old data does not get overwritten by accident
        self.existingCells : list= self.presenter.getCellIDs()
        self.existingEvents : list= self.presenter.getEventIDs()

        #indicates new cell to add for the UI, and has a list for new cells (never before recorded on file) and selected cells (seen here but not for the first time)
        self.cellToAddToList = None
        self.newCells = set()
        self.selectedCells = set()

        #follows a similar pattern to cells above
        self.eventToAddToList = None
        self.newEvents = set()
        self.selectedEvents = set()

        #show box ID
        self.boxIDLabel = qtw.QLabel("BoxID: ")
        self.boxIDField = qtw.QLineEdit()
        self.boxIDField.setText(boxID)
        self.boxIDField.setReadOnly(True)

        #ask for cell(s)
        self.cellsLabel = qtw.QLabel("Add cell(s): ")
        self.cellsDropdown = qtw.QComboBox()
        self.cellsDropdown.addItems(self.existingCells)
        self.cellsDropdown.addItem("Add new cell")
        self.cellsDropdown.currentTextChanged.connect(self.cellSelected)
            
        #Defining a new cell fields
        self.newCellIDLabel = qtw.QLabel("New cell ID: ")
        self.newCellIDField = qtw.QLineEdit()
        self.newCellIDField.setReadOnly(True)
        
        self.newCellTypeLabel = qtw.QLabel("New cell type: ")
        self.newCellTypeField = qtw.QLineEdit()
        self.newCellTypeField.textChanged.connect() #FIXME?

        self.hideNewCellFields()

        #list the added cells
        self.cellList = qtw.QListWidget()

        #add cell button
        self.addCellButton = qtw.QPushButton()
        self.addCellButton.setText("Add cell")
        self.addCellButton.pressed.connect(self.addCellToList)

        #ask for events(s)
        self.eventsLabel = qtw.QLabel("Add events(s): ")
        self.eventsDropdown = qtw.QComboBox()
        self.eventsDropdown.addItems(self.existingEvents)
        self.eventsDropdown.addItem("Add new event")
        self.eventsDropdown.currentTextChanged.connect(self.eventSelected)
            
        #Defining new event fields
        self.newEventIDLabel = qtw.QLabel("New event ID: ")
        self.newEventIDField = qtw.QLineEdit()
        self.newEventIDField.setReadOnly(True)
        
        self.newEventTypeLabel = qtw.QLabel("New event type: ")
        self.newEventTypeField = qtw.QLineEdit()
        self.newEventTypeField.textChanged.connect() #FIXME?
        
        #SUBMIT BUTTON
        #once all data set user presses this to finalize the box label data
        submitButton = qtw.QPushButton()
        submitButton.setText("Submit label data")
        submitButton.pressed.connect(self.submitData)
    
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
        if mode == "Add new cell":
            #show new cell fields
            self.showNewCellFields()
            self.cellToAddToList = None
        else:
            self.hideNewCellFields()
            self.cellToAddToList = mode


    def eventSelected(self):
        pass

    def submitData(self):
        #grab the data
        
        boxID = self.boxIDField.text()
        boxDimensions = self.rectangle.getRect()
        #cellIDs
        newCellIdsToAdd = self.newCells
        otherCellIDs = self.selectedCells
        #eventIDs
        newEventsToAdd = self.newEvents
        otherEventIDs = self.selectedEvents
        
        self.presenter.submitData(boxID, boxDimensions, newCellIdsToAdd, otherCellIDs, newEventsToAdd, otherEventIDs)
        pass