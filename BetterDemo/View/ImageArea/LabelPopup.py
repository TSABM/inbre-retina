import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt, QRect
from Presenter.LabelPopupPresenter import LabelPopupPresenter

class LabelPopup(qtw.QDialog):
    def __init__(self, selectedBoxID : str):
        super().__init__()
        self.presenter = LabelPopupPresenter(self)
        self.setWindowTitle("Classify the selection")

        self.layout : qtw.QLayout = qtw.QVBoxLayout()
        self.setLayout(self.layout)

        #boxID
        self.boxId = selectedBoxID
        #frame Number?
        self.__displayBoxInfo()
        self.frameNum : int = self.presenter.getFrameNumber()
        
        self.tempCells : list = []
        self.tempEvents : list = []
        
        self.existingCells : set= self.presenter.getCellIDs()
        self.existingEvents : set= self.presenter.getEventIDs()
        self.existingCellTypes : set = self.presenter.getCellTypes()
        self.existingEventTypes : set = self.presenter.getEventTypes()

        self.__addCellFields()
        #self.__addEventsFields()
    
    '''methods below for adding main content'''
       
    def __displayBoxInfo(self):
        self.boxIdLabel = qtw.QLabel("Box Id: "+ self.boxId)
        self.currFrameLabel = qtw.QLabel("Current frame: " + str(self.presenter.getFrameNumber()))
        self.layout.addWidget(self.boxIdLabel)
        self.layout.addWidget(self.currFrameLabel)
    
    def __addCellFields(self):
        self.__addListOfExistingCells()
        self.__addCellDropdown()
        self.__addNewCellFields()
        self.__addIncludeCellButton()
                
    def __addListOfExistingCells(self):
        self.cellListLabel = qtw.QLabel("Included cells:")
        self.cellList = qtw.QListWidget()
        self.layout.addWidget(self.cellListLabel)
        self.layout.addWidget(self.cellList)
        pass

    def __addCellDropdown(self):
        self.addCellsLabel = qtw.QLabel("Add cell(s):")
        self.cellsDropdown = qtw.QComboBox()
        self.cellsDropdown.addItems(self.existingCells)
        self.cellsDropdown.addItem("-")
        self.cellsDropdown.addItem("Add new cell")
        self.cellsDropdown.currentTextChanged.connect(self.__cellDropdownController)
        
        self.layout.addWidget(self.addCellsLabel)
        self.layout.addWidget(self.cellsDropdown)

    def __addNewCellFields(self):
        '''
        add all fields needed for defining new cells
        '''
        #new cell creation fields
        self.newCellIDLabel = qtw.QLabel("New cell ID: ")
        #self.newCellIDField = qtw.QLineEdit()
        #self.newCellIDField.setReadOnly(True)
        self.layout.addWidget(self.newCellIDLabel)
        self.layout.addWidget(self.newCellIDField)
        
        self.__addNewCellTypeDropdown()

        #cell type creation fields
        self.newCellTypeField = qtw.QLineEdit()
        self.layout.addWidget(self.newCellTypeField)
        self.__hideNewCellFields()

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
    
    #def __addEventDropdown(self):
    
    #def __addNewEventCreationFields(self):
    
    def __addNewCellTypeDropdown(self):
        '''
        add a dropdown for selecting a new cell type
        '''
        self.newCellTypeLabel = qtw.QLabel("Cell type: ")
        self.cellTypesDropdown = qtw.QComboBox()
        self.cellTypesDropdown.addItem("-")
        self.cellTypesDropdown.addItems(self.existingCellTypes)
        self.cellTypesDropdown.addItem("Add new cell type")
        self.cellTypesDropdown.currentTextChanged.connect(self.__selectCellType)
        self.layout.addWidget(self.newCellTypeLabel)
        self.layout.addWidget(self.cellTypesDropdown)
    
    def __addIncludeCellButton(self):
        self.includeCellButton = qtw.QPushButton()
        self.includeCellButton.setText("Include cell")
        self.includeCellButton.pressed.connect(self.__includeCellSelection)
        self.layout.addWidget(self.includeCellButton)   
    
    '''methods below for controlling some of the variable fields'''
    
    def __cellDropdownController(self, mode):
        if mode == "-":
            self.cellToAddToList = None
        elif mode == "Add new cell":
            self.__showNewCellFields()
        else:
            self.__hideNewCellFields()
            self.cellToAddToList = mode
        pass
    
    #def __eventDropdownController(self)
    
    def __showNewCellFields(self):
        #show the fields
        self.newCellIDLabel.show()
        self.newCellIDField.show()
        self.cellTypesDropdown.show()
        self.newCellTypeLabel.show()
        #self.newCellTypeField.show()
    
    def __hideNewCellFields(self):
        self.newCellIDLabel.hide()
        self.newCellIDField.hide()
        self.cellTypesDropdown.hide()
        self.newCellTypeLabel.hide()
        self.newCellTypeField.hide()
    
    def __showNewCellTypeFields(self):
        self.newCellTypeField.show()

    def __hideNewCellTypeFields(self):
        self.newCellTypeField.hide()
        
    '''other methods'''

    def __genTempID(self, type : str, tempIdList : list):
        newValue = len(tempIdList) + 1
        newID = "tempID_" + type + str(newValue)
        return newID

    def __includeCellSelection(self, mode):
        print("tried to include a cell")
        '''
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
        '''
    
    def __selectCellType(self, mode):
        print("tried to set the cell type")
        '''
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
        '''

    
        

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
    '''
    
    """
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
    
    def generateEventId(self): #FIXME add content here
        #FIXME
        pass

    
    
        
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
    
    def __addSubmissionButton(self):
        self.submitButton = qtw.QPushButton()
        self.submitButton.setText("Submit label data")
        self.submitButton.pressed.connect(self.submitData)
        self.layout.addWidget(self.submitButton)
    """