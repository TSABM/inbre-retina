import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import QIntValidator
from Presenter.MainControlsPresenter import MainControlsPresenter


class MainControlsView(qtw.QWidget):
    '''
    The primary control widgets for the app.
    '''
    def __init__(self):
        super().__init__()
        self.presenter = MainControlsPresenter(self)
        self.setLayout(qtw.QVBoxLayout())
        self.drawColors = {}
        self.__addToolbox__()  # Build toolbox
        print("Main controls initialized")

    def __addToolbox__(self):
        self.toolbox = qtw.QToolBox()
        self.layout().addWidget(self.toolbox)

        self.toolbox.addItem(self.__videoNavigationPanel__(), "🎞️ Video Navigation")
        self.toolbox.addItem(self.__annotationPanel__(), "🎨 Annotation Colors")

    def __videoNavigationPanel__(self):
        panel = qtw.QWidget()
        layout = qtw.QVBoxLayout(panel)

        self.play_button = qtw.QPushButton("Play")
        self.pause_button = qtw.QPushButton("Pause")
        self.step_forward_button = qtw.QPushButton("Step Forward")
        self.step_backward_button = qtw.QPushButton("Step Backward")

        self.jump_input = qtw.QLineEdit()
        self.jump_input.setPlaceholderText("Enter frame number...")
        self.jump_input.setValidator(QIntValidator())
        self.jump_input.returnPressed.connect(self.__jumpToFrame__)

        layout.addWidget(self.play_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.step_forward_button)
        layout.addWidget(self.step_backward_button)
        layout.addWidget(self.jump_input)

        self.play_button.clicked.connect(self.playVideo)
        self.pause_button.clicked.connect(self.pauseVideo)
        self.step_forward_button.clicked.connect(self.stepForward)
        self.step_backward_button.clicked.connect(self.stepBackward)

        return panel

    def __annotationPanel__(self):
        panel = qtw.QWidget()
        layout = qtw.QVBoxLayout(panel)

        self.cell_type_dropdown = qtw.QComboBox()
        self.cell_type_dropdown.setPlaceholderText("Select Cell Type")
        for cell_type in self.getCellTypes().keys():
            self.cell_type_dropdown.addItem(cell_type)

        self.color_dropdown = qtw.QComboBox()
        self.color_dropdown.setPlaceholderText("Select Color")
        self.colors = self.getColors()
        if self.colors is not None:
            for color_name in self.colors:
                self.color_dropdown.addItem(color_name)

        self.assign_button = qtw.QPushButton("Assign Color")
        self.assign_button.clicked.connect(self.__assignColorToCellType__)

        self.refreshButton = qtw.QPushButton("Refresh color/cellType fields")
        self.refreshButton.clicked.connect(self.refresh)

        layout.addWidget(self.refreshButton)
        layout.addWidget(self.cell_type_dropdown)
        layout.addWidget(self.color_dropdown)
        layout.addWidget(self.assign_button)

        return panel

    def __jumpToFrame__(self):
        frame_num = self.jump_input.text()
        if frame_num.isdigit():
            self.jumpTo(int(frame_num))

    def __assignColorToCellType__(self):
        if self.colors is not None:
            selected_cell_type = self.cell_type_dropdown.currentText()
            selected_color_name = self.color_dropdown.currentText()
            if selected_cell_type and selected_color_name:
                selected_color = self.colors[selected_color_name]
                self.mapCellTypeToColor(selected_cell_type, selected_color)
                print(f"Mapped {selected_cell_type} to {selected_color_name}")

    # Video control methods
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

    # Color mapping
    def getColors(self):
        return self.presenter.getColors()

    def mapCellTypeToColor(self, cellTypeToBind, color):
        self.presenter.mapCellTypeToColor(cellTypeToBind, color)

    def getCellTypes(self):
        cellTypes = self.presenter.getCellTypes()
        return {} if cellTypes is None else cellTypes

    def refresh(self):
        self.cell_type_dropdown.clear()
        self.color_dropdown.clear()

        for cell_type in self.getCellTypes().keys():
            self.cell_type_dropdown.addItem(cell_type)

        self.colors = self.getColors()
        if self.colors is not None:
            for color_name in self.colors:
                self.color_dropdown.addItem(color_name)
