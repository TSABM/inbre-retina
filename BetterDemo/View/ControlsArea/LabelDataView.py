import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import QIntValidator
from Presenter.LabelDataPresenter import LabelDataPresenter
from Model.Label import Label

class LabelDataView(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.labelToDisplay = None
        self.presenter = LabelDataPresenter(self)
        self.setLayout(qtw.QVBoxLayout())
    
    def loadLabelDataFields(self):
        #init labels
        iDLabel = qtw.QLabel("Label Id: ")
        typeLabel = qtw.QLabel("Label type: ")
        frameNumLabel = qtw.QLabel("Label frame number: ")
        topLeftXLabel = qtw.QLabel("Label corner 1 X: ")
        topLeftYLabel = qtw.QLabel("Label corner 1 Y: ")
        bottomRightXLabel = qtw.QLabel("Label corner 2 X: ")
        bottomRightYLabel = qtw.QLabel("Label corner 2 Y: ")

        #init fields
        self.iDField = qtw.QLineEdit()
        self.typeField = qtw.QLineEdit()
        self.frameNumberField = qtw.QLineEdit()
        self.topLeftXField = qtw.QLineEdit()
        self.topLeftYField = qtw.QLineEdit()
        self.bottomRightXField = qtw.QLineEdit()
        self.bottomRightYField = qtw.QLineEdit()

        #restrict valid inputs to ints where applicable
        maxX = self.presenter.getMaxXVal()
        maxY = self.presenter.getMaxYVal()
        self.frameNumberField.setValidator(QIntValidator(0, 99999999)) #this validator requires an upper limit, the values I used are arbitrary. To make any int acceptable a custom validator would be required
        self.topLeftXField.setValidator(QIntValidator(0, maxX))
        self.topLeftYField.setValidator(QIntValidator(0, maxY))
        self.bottomRightXField.setValidator(QIntValidator(0, maxX))
        self.bottomRightYField.setValidator(QIntValidator(0, maxY))

        #connect fields to functions (currently only triggers when a user changes the values in the ui)
        self.iDField.textEdited.connect()
        self.typeField.textEdited.connect()
        self.frameNumberField.textEdited.connect()
        self.topLeftXField.textEdited.connect()
        self.topLeftYField.textEdited.connect()
        self.bottomRightXField.textEdited.connect()
        self.bottomRightYField.textEdited.connect()

        #add labels and fields to the widget
        self.layout().addWidget(iDLabel)
        self.layout().addWidget(self.iDField)

        self.layout().addWidget(typeLabel)
        self.layout().addWidget(self.typeField)

        self.layout().addWidget(frameNumLabel)
        self.layout().addWidget(self.frameNumberField)

        self.layout().addWidget(topLeftXLabel)
        self.layout().addWidget(self.topLeftXField)

        self.layout().addWidget(topLeftYLabel)
        self.layout().addWidget(self.topLeftYField)

        self.layout().addWidget(bottomRightXLabel)
        self.layout().addWidget(self.bottomRightXField)

        self.layout().addWidget(bottomRightYLabel)
        self.layout().addWidget(self.bottomRightYField)
        

    def displayLabelData(self, label : Label):
        #set fields to data vals
        self.iDField.setText(label.itemId)
        self.typeField.setText(label.type)
        self.frameNumberField.setText(label.frameNumber)
        self.topLeftXField.setText(label.rectangle.topLeft().x)
        self.topLeftYField.setText(label.rectangle.topLeft().y)
        self.bottomRightXField.setText(label.rectangle.bottomRight().x)
        self.bottomRightYField.setText(label.rectangle.bottomRight().y)

        #show the widget
        self.show()

    def publishLabelData(self):
        #when the text is changed update the label on the canvas
        #determine what changed?
        #call the presenter and ask the canvas to update, may need to send the label back but proabbly not.
        self.presenter.publish("canvas")

    def hideLabelData(self):
        self.hide()