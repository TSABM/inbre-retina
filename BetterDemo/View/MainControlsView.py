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
        #controlBox = qtw.QWidget()
        self.setLayout(qtw.QVBoxLayout())

        controls = qtw.QWidget()
        controls.setLayout(qtw.QGridLayout())

        #making the widgets
        labelGroupLabel = qtw.QLabel("Label group")
        squareLabel = qtw.QLabel("Square")
        freeDrawLabel = qtw.QLabel("Free draw")
        fillLabel = qtw.QLabel("Fill")
        
        labelGroupSelect = qtw.QComboBox()
        squareModeButton = qtw.QPushButton()
        freeDrawModeButton = qtw.QPushButton()
        fillModeButton = qtw.QPushButton()

        #Connecting widgets to functions
        squareModeButton.pressed.connect(self.setModeToSquare)
        freeDrawModeButton.pressed.connect(self.setModeToFreeDraw)
        fillModeButton.pressed.connect(self.setModeToFill)


        #binding widgets to layout
        controls.layout().addWidget(labelGroupLabel, 0, 0)
        controls.layout().addWidget(squareLabel, 1, 0)
        controls.layout().addWidget(freeDrawLabel, 2, 0)
        controls.layout().addWidget(fillLabel, 3, 0)

        controls.layout().addWidget(labelGroupSelect, 0, 1)
        controls.layout().addWidget(squareModeButton, 1, 1)
        controls.layout().addWidget(freeDrawModeButton, 2, 1)
        controls.layout().addWidget(fillModeButton, 3, 1)
        

        self.layout().addWidget(controls)

        print("main controls initalized")

    #Functions to send udate requests to the presenter
    def setModeToSquare():
        pass
    def setModeToFreeDraw():
        pass
    def setModeToFill():
        pass