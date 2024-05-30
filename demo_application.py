#demo application
import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt


class MainWindow(qtw.QWidget):
    def __init__(self):#telling main window to init 
        super().__init__()
        self.setWindowTitle("DemoApp")
        self.setLayout(qtw.QHBoxLayout()) #adding a veritcal container
        self.mainControls()
        #self.display()


        self.show()
    def mainControls(self):
        #setting layout
        controlBox = qtw.QWidget()
        controlBox.setLayout(qtw.QVBoxLayout())

        controls = qtw.QWidget()
        controls.setLayout(qtw.QGridLayout())

        #making the widgets
        opacityLabel = qtw.QLabel("Opacity")
        contrastLimitsLabel = qtw.QLabel("Contrast Limits")
        autoContrastLabel = qtw.QLabel("Auto Contrast")
        gammaLabel = qtw.QLabel("Gamma")
        colorLabel = qtw.QLabel("Color")
        blendingLabel = qtw.QLabel("Blending")
        interpolationLabel = qtw.QLabel("Interpolation")

        opacityControl = qtw.QSlider(Qt.Horizontal)
        contrastLimitsControl = qtw.QSlider(Qt.Horizontal)
        autoContrastControl = qtw.QRadioButton()
        gammaControl = qtw.QSlider(Qt.Horizontal)
        colorControl = qtw.QComboBox()
        blendingControl = qtw.QComboBox()
        interpolationControl = qtw.QComboBox()


        #binding widgets to layout
        controls.layout().addWidget(opacityLabel, 0, 0)
        controls.layout().addWidget(contrastLimitsLabel, 1, 0)
        controls.layout().addWidget(autoContrastLabel, 2, 0)
        controls.layout().addWidget(gammaLabel, 3, 0)
        controls.layout().addWidget(colorLabel, 4, 0)
        controls.layout().addWidget(blendingLabel, 5, 0)
        controls.layout().addWidget(interpolationLabel, 6, 0)

        controls.layout().addWidget(opacityControl, 0, 1)
        controls.layout().addWidget(contrastLimitsControl, 1, 1)
        controls.layout().addWidget(autoContrastControl, 2, 1)
        controls.layout().addWidget(gammaControl, 3, 1)
        controls.layout().addWidget(colorControl, 4, 1)
        controls.layout().addWidget(blendingControl, 5, 1)
        controls.layout().addWidget(interpolationControl, 6, 1)

        controlBox.layout().addWidget(controls)
        self.layout().addWidget(controlBox)
    #def display(self):
        
        

app = qtw.QApplication([])
window = MainWindow()
app.exec_()
