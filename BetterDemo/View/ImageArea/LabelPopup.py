import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt
from Presenter.LabelPopupPresenter import LabelPopupPresenter

class LabelPopup(qtw.QDialog):
    '''
    The popup that appears when a new bounding box is being drawn on the image. If the user fills out the fields a valid label data item can
    be created.
    '''
    def __init__(self, boxID):
        super().__init__()
        self.presenter = LabelPopupPresenter()
        self.setWindowTitle("Classify the selection")

        self.setLayout(qtw.QVBoxLayout())

        self.existingCells : list= self.presenter.getCellIDList()
        self.existingEvents : list= self.presenter.getEventIDList()

        self.cellToAdd = None
        self.selectedCells = set()
        #self.newCellMode = False

        #show box ID
        boxIDLabel = qtw.QLabel("BoxID: ")
        boxIDField = qtw.QLineEdit()
        boxIDField.setText(boxID)
        boxIDField.setReadOnly(True)

        #ask for cell(s)
        cellsLabel = qtw.QLabel("Add cell(s): ")
        cellsDropdown = qtw.QComboBox()
        cellsDropdown.addItems(self.existingCells)
        cellsDropdown.addItem("Add new cell")
        cellsDropdown.currentTextChanged.connect(self.cellSelected)
            
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

        #ask for event(s) FIXME
        eventsLabel = qtw.QLabel("Add event(s): ")
        self.selectedEvents = []
        eventsDropdown = qtw.QComboBox()
        eventsDropdown.addItems(self.existingEvents)
        eventsDropdown.addItem("Add new event")
        eventsDropdown.currentTextChanged.connect(self.eventSelected)
            #show event ID
            #ask for event type
            #show the participating cells? (grabbed from above?)
        
        #SUBMIT BUTTON
        #once all data set user presses this to finalize the cell and box
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
        if self.cellToAdd != None:
            self.selectedCells.add(self.cellToAdd)
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
            self.cellToadd = None
        else:
            self.hideNewCellFields()
            self.cellToAdd = mode


    def eventSelected(self):
        pass

    def submitData(self):
        #grab the data

        #check that required fields are filled
            #if so make a new label
            #if not give a toast
        pass