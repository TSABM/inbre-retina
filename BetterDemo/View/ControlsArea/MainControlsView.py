import PyQt5.QtWidgets as qtw

from Presenter.MainControlsPresenter import MainControlsPresenter

class MainControlsView(qtw.QWidget):
    '''
    The primary control widgets for the app.
    '''
    def __init__(self):
        super().__init__()
        self.presenter = MainControlsPresenter(self)
        #setting layout
        self.setLayout(qtw.QVBoxLayout())
        self.__addControls()
        print("main controls initalized")

    def __addControls(self):
        #controls = qtw.QWidget()
        #controls.setLayout(qtw.QGridLayout())

        #making the widgets
        interactionModeLabel = qtw.QLabel("Select interaction mode")

        interactionModeSelect = qtw.QComboBox()

        #Connecting widgets to functions
        #squareModeButton.pressed.connect(self.setModeToSquare)
        interactionModeSelect.addItem("Select label")
        interactionModeSelect.addItem("Draw label")
        interactionModeSelect.addItem("Erase")

        interactionModeSelect.currentTextChanged.connect(self.setInteractionMode)

        #binding widgets to layout
        self.layout().addWidget(interactionModeLabel)

        self.layout().addWidget(interactionModeSelect)

        #add widget to layout
        #self.layout().addWidget(controls)

    #Functions to send update requests to the presenter
    def setInteractionMode(self, mode):
        self.presenter.setInteractionMode(mode)