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
        print("Main controls initialized")

    def __addControls__(self):
        # Creating buttons
        self.play_button = qtw.QPushButton("Play")
        self.pause_button = qtw.QPushButton("Pause")
        self.step_forward_button = qtw.QPushButton("Step Forward")
        self.step_backward_button = qtw.QPushButton("Step Backward")

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

        # Connecting buttons to functions
        self.play_button.clicked.connect(self.playVideo)
        self.pause_button.clicked.connect(self.pauseVideo)
        self.step_forward_button.clicked.connect(self.stepForward)
        self.step_backward_button.clicked.connect(self.stepBackward)

    def __jumpToFrame__(self):
        frame_num = self.jump_input.text()
        if frame_num.isdigit():  # Ensure it's a valid number
            self.jumpTo(int(frame_num))

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
