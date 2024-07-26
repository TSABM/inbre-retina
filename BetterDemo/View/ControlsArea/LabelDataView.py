import PyQt5.QtWidgets as qtw

class LabelDataView(qtw.QWidget):
    def __init__(self):
        self.labelToDisplay = None
        self.presenter = None
        self.setLayout(qtw.QVBoxLayout())
    
    def loadLabelDataFields(self):
        labelIDLabel = qtw.QLabel("Label Id: ")

        #init fields
        iDField = qtw.QLineEdit()
        typeField = qtw.QLineEdit()
        frameNumberField = qtw.QLineEdit()
        topLeftField = qtw.QLineEdit()
        BottomRightField = qtw.QLineEdit()

        #get current values
        #FIXME

        #connect fields to functions
        iDField.textChanged.connect()
        typeField.textChanged.connect()
        frameNumberField.textChanged.connect()
        topLeftField.textChanged.connect()
        BottomRightField.textChanged.connect()
        

    def displayLabel(self, label):
        pass

    def requestLabel(self):
        pass

    def updateLabelData(self):
        pass