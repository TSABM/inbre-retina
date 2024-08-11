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

        self.selectedCells = []
        self.newCellMode = False

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
            #add currently existing cells
            #define a new cell
        
        self.newCellIDLabel = qtw.QLabel("New cell ID: ")
        self.newCellIDField = qtw.QLineEdit()
        self.newCellIDField.setReadOnly(True)
        
        self.newCellTypeLabel = qtw.QLabel("New cell type: ")
        self.newCellTypeField = qtw.QLineEdit()
        self.newCellTypeField.textChanged.connect()

        if self.newCellMode == False:
            self.newCellIDLabel.hide()
            self.newCellIDField.hide()
            self.newCellTypeLabel.hide()
            self.newCellTypeField.hide()
                #show new cell ID
                #define cell type

        #ask for event(s)
        eventsLabel = qtw.QLabel("Add event(s): ")
        self.selectedEvents = []
        eventsDropdown = qtw.QComboBox()
        eventsDropdown.addItems(self.existingEvents)
        eventsDropdown.addItem("Add new event")
        eventsDropdown.currentTextChanged.connect(self.eventSelected)
            #show event ID
            #ask for event type
            #show the participating cells? (grabbed from above?)
    
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
            pass
        else:
            pass
        pass

    def eventSelected(self):
        pass