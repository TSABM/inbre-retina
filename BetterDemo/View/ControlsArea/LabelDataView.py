import PyQt5.QtWidgets as qtw

class LabelDataView(qtw.QWidget):
    def __init__(self):
        self.labelToDisplay = None
        self.presenter = None
        self.setLayout(qtw.QVBoxLayout())
    
    def loadLabelDataFields(self):
        labelIDLabel = qtw.QLabel("Label Id: ")


        iDField = qtw.QLineEdit()
        typeField = qtw.QLineEdit()
        frameNumberField = qtw.QLineEdit()
        topLeftField = qtw.QLineEdit()
        BottomRightField = qtw.QLineEdit()
        pass

    def displayLabel(self, label):
        pass

    def requestLabel(self)

    def updateLabelData(self):
        pass