import PyQt5.QtWidgets as qtw
#import PyQt5.QtCore as qtc
from PyQt5.QtGui import QIntValidator


from Presenter.MainControlsPresenter import MainControlsPresenter

class MainControlsView(qtw.QWidget):
    '''
    The primary control widgets for the app.
    '''
    def __init__(self):
        super().__init__()
        self.presenter = MainControlsPresenter(self)
        self.setLayout(qtw.QVBoxLayout())  # Setting layout
        self.__addControls__()
        self.drawColors = {}
        print("Main controls initialized")

    def __addControls__(self):
        # Creating buttons
        self.play_button = qtw.QPushButton("Play")
        self.pause_button = qtw.QPushButton("Pause")
        self.step_forward_button = qtw.QPushButton("Step Forward")
        self.step_backward_button = qtw.QPushButton("Step Backward")

        # buttons to assign color to each cell type
         # Cell type dropdown
        self.cell_type_dropdown = qtw.QComboBox()
        self.cell_type_dropdown.setPlaceholderText("Select Cell Type")
        for cell_type in self.getCellTypes().keys():
            self.cell_type_dropdown.addItem(cell_type)
        # Color dropdown
        self.color_dropdown = qtw.QComboBox()
        self.color_dropdown.setPlaceholderText("Select Color")
        self.colors = self.getColors()
        if self.colors != None:
            for color_name in self.colors:
                self.color_dropdown.addItem(color_name)
        # Assign button
        self.assign_button = qtw.QPushButton("Assign Color")
        self.assign_button.clicked.connect(self.__assignColorToCellType__)
        #refresh fields
        self.refreshButton = qtw.QPushButton("Refresh color/cellType fields")
        self.refreshButton.clicked.connect(self.refresh)

        # Creating input field for frame jumping
        self.jump_input = qtw.QLineEdit()
        self.jump_input.setPlaceholderText("Enter frame number...")
        self.jump_input.setValidator(QIntValidator())  # Only allows integer input
        self.jump_input.returnPressed.connect(self.__jumpToFrame__)  # Calls function on Enter

        # Adding widgets to layout
        layout = self.layout()
        layout.addWidget(self.play_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.step_forward_button)
        layout.addWidget(self.step_backward_button)
        layout.addWidget(self.jump_input)

        layout.addWidget(self.cell_type_dropdown)
        layout.addWidget(self.color_dropdown)
        layout.addWidget(self.assign_button)
        layout.addWidget(self.refreshButton)

        # Connecting buttons to functions
        self.play_button.clicked.connect(self.playVideo)
        self.pause_button.clicked.connect(self.pauseVideo)
        self.step_forward_button.clicked.connect(self.stepForward)
        self.step_backward_button.clicked.connect(self.stepBackward)
        self.assign_button.clicked.connect(self.__assignColorToCellType__)

    def __jumpToFrame__(self):
        frame_num = self.jump_input.text()
        if frame_num.isdigit():  # Ensure it's a valid number
            self.jumpTo(int(frame_num))

    def __assignColorToCellType__(self):
        if self.colors != None:
            selected_cell_type = self.cell_type_dropdown.currentText()
            selected_color_name = self.color_dropdown.currentText()
            if selected_cell_type and selected_color_name:
                selected_color = self.colors[selected_color_name]
                self.mapCellTypeToColor(selected_cell_type, selected_color)
                print(f"Mapped {selected_cell_type} to {selected_color_name}")

    def playVideo(self):
        self.presenter.playMovie()
    
    def pauseVideo(self):
        self.presenter.pauseMovie()
    
    def stepForward(self):
        self.presenter.stepForward()

    def stepBackward(self):
        self.presenter.stepBackward()
    
    def jumpTo(self, frameNum):
        self.presenter.jumpToFrameNum(frameNum)

    def getColors(self): #returns a dict of colors
        return self.presenter.getColors()

    def mapCellTypeToColor(self, cellTypeToBind, color):
        self.presenter.mapCellTypeToColor(cellTypeToBind, color)

    def getCellTypes(self): #returns a dicitonary of cell types
        cellTypes = self.presenter.getCellTypes()
        if cellTypes == None:
            return {}
        else:
            return cellTypes
        
    def refresh(self):
        self.cell_type_dropdown.clear()
        self.color_dropdown.clear()
        for cell_type in self.getCellTypes().keys():
            self.cell_type_dropdown.addItem(cell_type)
        self.colors = self.getColors()
        if self.colors != None:
            for color_name in self.colors:
                self.color_dropdown.addItem(color_name)
        pass