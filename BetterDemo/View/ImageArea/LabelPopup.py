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
        boxIDField.setFocusPolicy(Qt.NoFocus)

        #ask for cell(s)
        cellsLabel = qtw.QLabel("Add cell(s): ")
        cellsDropdown = qtw.QComboBox()
        cellsDropdown.addItems(self.existingCells)
        cellsDropdown.addItem("Add new cell")
        cellsDropdown.currentTextChanged.connect(self.cellSelected)
            #add currently existing cells
            #define a new cell
        
        #generate new cell ID
        newID = 
        newCellIDLabel = qtw.QLabel("New cell ID: ")
        newCellIDField = qtw.QLineEdit()
        
        newCellTypeLabel = qtw.QLabel("New cell type: ")
        newCellTypeField = qtw.QLineEdit()
        newCellTypeField.textChanged.connect()

        if self.newCellMode == False:
            newCellIDLabel.hide()
            newCellIDField.hide()
            newCellTypeLabel.hide()
            newCellTypeField.hide()
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
    
    def cellSelected(self):

        pass

    def eventSelected(self):
        pass