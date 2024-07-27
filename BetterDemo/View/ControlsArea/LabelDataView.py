import PyQt5.QtWidgets as qtw
from Presenter.LabelDataPresenter import LabelDataPresenter

class LabelDataView(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.labelToDisplay = None
        self.presenter = LabelDataPresenter(self)
        self.setLayout(qtw.QVBoxLayout())
    
    def loadLabelDataFields(self):
        iDLabel = qtw.QLabel("Label Id: ")
        typeLabel = qtw.QLabel("Label type: ")
        frameNumLabel = qtw.QLabel("Label frame number: ")
        topLeftLabel = qtw.QLabel("Label corner 1: ")
        bottomRightLabel = qtw.QLabel("Label corner 2: ")

        #init fields
        iDField = qtw.QLineEdit()
        typeField = qtw.QLineEdit()
        frameNumberField = qtw.QLineEdit()
        topLeftField = qtw.QLineEdit()
        bottomRightField = qtw.QLineEdit()

        #connect fields to functions
        iDField.textChanged.connect()
        typeField.textChanged.connect()
        frameNumberField.textChanged.connect()
        topLeftField.textChanged.connect()
        bottomRightField.textChanged.connect()
        

    def displayLabelData(self, label):
        #show this widget
        pass

    def updateLabelData(self):
        #when the text is changed update the label on the canvas

        pass

    def hideLabelData():
        pass