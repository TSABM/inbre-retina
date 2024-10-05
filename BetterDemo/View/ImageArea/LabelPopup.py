import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt, QRect
from Presenter.LabelPopupPresenter import LabelPopupPresenter

class LabelPopup(qtw.QDialog):
    def __init__(self, boxID : str):
        super().__init__()
        self.presenter = LabelPopupPresenter(self)
        self.setWindowTitle("Classify the selection")

        self.layout : qtw.QLayout = qtw.QVBoxLayout()
        self.setLayout(self.layout)

        #boxID
        #frame Number?

        #cell box
            #list of cell Ids and their types
            #fields for assotiating existing cells
            #fields for creating new cells
        
        #event box
            #list of event ids and their types
            #fields for assotiating existing events
            #fields for creating new events
        
        
        '''
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
        self.cellTypeToAdd = None
        self.eventTypeToAdd = None
        self.cellToAddToList = None
        self.eventToAddToList = None

        #this is where items that have been assotiated with the box here in the popup window are stored before being submitted to the master memory
        self.newCellTypes = set()
        self.newEventTypes = set()
        self.includedCells = dict()
        self.includedEvents = dict()

        #Add popup UI elements
        self.__addBoxIDField(boxID)
        self.__addCellFields()
        self.hideNewCellFields()

        self.__addEventsFields()
        self.hideNewEventFields()
        
        self.__addSubmissionButton()
    

    def getUniqueCellID(self): #FIXME: if I added multiple unique cells before submission I'd get duplicate id's! account for staged cells!
        #quickly scan the existing cells and grab the largest number, add 1 then return a new id
        largestValue = 0
        for id in self.existingCells:
            x = id.split('_')[1]
            x = int(x)
            if x > largestValue:
                largestValue = x
        newValue = largestValue + 1
        newID = "test_cell_" + str(newValue)
        return newID
    
    def generateEventId(self):
        #FIXME
        pass

    def showNewCellFields(self):
        #show the fields
        self.newCellIDLabel.show()
        self.newCellIDField.show()
        self.cellTypesDropdown.show()
        self.newCellTypeLabel.show()
        #self.newCellTypeField.show()
    
    def hideNewCellFields(self):
        self.newCellIDLabel.hide()
        self.newCellIDField.hide()
        self.cellTypesDropdown.hide()
        self.newCellTypeLabel.hide()
        self.newCellTypeField.hide()
    
    def showNewCellTypeFields(self):
        self.newCellTypeField.show()

    def hideNewCellTypeFields(self):
        self.newCellTypeField.hide()
    
    def includeCellInList(self):
        print("attempted to include cell")
        if self.cellToAddToList != None:
            if self.cellTypeToAdd != None:
                self.includedCells.update({self.cellToAddToList : self.cellTypeToAdd})
            else:
                self.includedCells.update({self.cellToAddToList : self.newCellTypeField.text()})
            self.cellList.clear() #clear the whole list
            print("attempting to list the following cells: ", self.includedCells.keys())
            self.cellList.addItems(self.includedCells.keys()) #add all included cells back to the list display
        else:
            print("tried to include cell of type None")
    
    def hideNewCellTypesFields(self):
        self.newCellTypeField.hide()

    def showNewCellTypesFields(self):
        self.newCellTypeField.show()
        
    def showNewEventFields(self):
        self.newEventIDLabel.show()
        self.newEventIDField.show()
        self.newEventTypeLabel.show()
        self.newEventTypeField.show()

    def hideNewEventFields(self):
        self.newEventIDLabel.hide()
        self.newEventIDField.hide()
        self.newEventTypeLabel.hide()
    
    def showNewEventTypeFields(self):
        self.newEventTypeField.show()

    def hideNewEventTypesFields(self):
        self.newEventTypeField.hide()

    def includeACell(self, mode):
        if mode == "-":
            #do nothing
            self.cellToAddToList = None
        elif mode == "Add new cell":
            #show new cell fields
            #get the cell Id
            newID = self.generateCellID()
            self.newCellIDField.setText(newID)
            self.showNewCellFields()
            self. = None
        else:
            self.hideNewCellFields()
            self.cellToAddToList = mode

    def cellTypeSelected(self, mode):
        if mode == "-":
            #do nothing
            self.hideNewCellTypesFields()
            self.cellTypeToAdd = None
        elif mode == "Add new cell type":
            #show new cell fields
            self.showNewCellTypesFields()
            self.cellTypeToAdd = None
        else:
            self.hideNewCellTypesFields()
            self.cellTypeToAdd = mode
    
    def eventSelected(self, mode):
        if mode == "-":
            # Do nothing
            self.eventToAddToList = None
        elif mode == "Add new event":
            # Show new event fields
            #get the cell Id
            newID = self.generateCellID()
            self.newCellIDField.setText(newID)
            self.showNewEventFields()
            self.eventToAddToList = None
        else:
            self.hideNewEventFields()
            self.eventToAddToList = mode

    def eventTypeSelected(self, mode):
        if mode == "-":
            # Do nothing
            self.hideNewEventTypesFields()
            self.eventTypeToAdd = None
        elif mode == "Add new event type":
            # Show new event type fields
            self.showNewEventTypeFields()
            self.eventTypeToAdd = None
        else:
            self.hideNewEventTypesFields()
            self.eventTypeToAdd = mode

    def submitData(self):
        #grab the data
        boxID = self.boxIDField.text()
        boxDimensions : QRect = self.rectangle.getRect()
        self.presenter.submitData(boxID, self.frameNum, boxDimensions.getRect(), self.includedCells, self.includedEvents, self.newCellTypes, self.newEventTypes)

    #helper methods for adding the UI elements to the layout
    def __addBoxIDField(self, boxID):
        self.boxIDLabel = qtw.QLabel("BoxID: ")
        self.boxIDField = qtw.QLineEdit()
        self.boxIDField.setText(boxID)
        self.boxIDField.setReadOnly(True)
        self.layout.addWidget(self.boxIDLabel)
        self.layout.addWidget(self.boxIDField)
    

    def __addCellFields(self):
        self.cellsLabel = qtw.QLabel("Included cell(s): ")
        self.cellsDropdown = qtw.QComboBox()
        self.cellsDropdown.addItems(self.existingCells)
        self.cellsDropdown.addItem("-")
        self.cellsDropdown.addItem("Add new cell")
        self.cellsDropdown.currentTextChanged.connect(self.includeACell)
        self.layout.addWidget(self.cellsLabel)
        self.layout.addWidget(self.cellsDropdown)

        #new cell creation fields
        self.newCellIDLabel = qtw.QLabel("New cell ID: ")
        self.newCellIDField = qtw.QLineEdit()
        self.newCellIDField.setReadOnly(True)
        self.layout.addWidget(self.newCellIDLabel)
        self.layout.addWidget(self.newCellIDField)
        
        #fields for defining new cell types
        self.newCellTypeLabel = qtw.QLabel("Cell type: ")
        self.cellTypesDropdown = qtw.QComboBox()
        self.cellTypesDropdown.addItem("-")
        self.cellTypesDropdown.addItems(self.existingCellTypes)
        self.cellTypesDropdown.addItem("Add new cell type")
        self.cellTypesDropdown.currentTextChanged.connect(self.cellTypeSelected)
        self.layout.addWidget(self.newCellTypeLabel)
        self.layout.addWidget(self.cellTypesDropdown)

        #cell type creation fields
        self.newCellTypeField = qtw.QLineEdit()
        self.layout.addWidget(self.newCellTypeField)

        #include cell button and included cells list
        self.includeCellButton = qtw.QPushButton()
        self.includeCellButton.setText("Include cell")
        self.includeCellButton.pressed.connect(self.includeCellInList)
        self.layout.addWidget(self.includeCellButton)

        self.cellListLabel = qtw.QLabel("Included cells:")
        self.cellList = qtw.QListWidget()
        self.layout.addWidget(self.cellListLabel)
        self.layout.addWidget(self.cellList)
        
    
    def __addEventsFields(self):
        self.eventsLabel = qtw.QLabel("Include Event(s): ")
        self.eventsDropdown = qtw.QComboBox()
        self.eventsDropdown.addItem("-")
        self.eventsDropdown.addItems(self.existingEvents)
        self.eventsDropdown.addItem("Add new event")
        self.eventsDropdown.currentTextChanged.connect(self.eventSelected)
        self.layout.addWidget(self.eventsLabel)
        self.layout.addWidget(self.eventsDropdown)

        #event creation fields
        self.newEventIDLabel = qtw.QLabel("New event ID: ")
        self.newEventIDField = qtw.QLineEdit()
        self.newEventIDField.setReadOnly(True)
        self.layout.addWidget(self.newEventIDLabel)
        self.layout.addWidget(self.newEventIDField)
        
        self.newEventTypeLabel = qtw.QLabel("New event type: ")
        self.newEventTypeField = qtw.QLineEdit()
        self.layout.addWidget(self.newEventTypeLabel)
        self.layout.addWidget(self.newEventTypeField)
        
    
    def __addSubmissionButton(self):
        self.submitButton = qtw.QPushButton()
        self.submitButton.setText("Submit label data")
        self.submitButton.pressed.connect(self.submitData)
        self.layout.addWidget(self.submitButton)
    '''