import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt

class primaryControls():
    def __init__(self):
        controlBox = qtw.QWidget()
        controlBox.setLayout(qtw.QVBoxLayout())

        controls = qtw.QWidget()
        controls.setLayout(qtw.QGridLayout())

        menuBox = qtw.QWidget()
        menuBox.setLayout(qtw.QHBoxLayout())

        #making the widgets
        opacityLabel = qtw.QLabel("Opacity")
        contrastLimitsLabel = qtw.QLabel("Contrast Limits")
        autoContrastLabel = qtw.QLabel("Auto Contrast")
        gammaLabel = qtw.QLabel("Gamma")
        colorLabel = qtw.QLabel("Color")
        blendingLabel = qtw.QLabel("Blending")
        interpolationLabel = qtw.QLabel("Interpolation")
        

        opacityControl = qtw.QSlider(Qt.Horizontal)
        opacityControl.setRange(0, 100)
        opacityControl.setSliderPosition(100)
        opacityControl.setSingleStep(1)
        opacityControl.valueChanged['int'].connect(self.adjustOpacity)

        contrastLimitsControl = qtw.QSlider(Qt.Horizontal)
        contrastLimitsControl.setRange(-100, 100)
        contrastLimitsControl.setSliderPosition(0)
        contrastLimitsControl.setSingleStep(1)
        contrastLimitsControl.valueChanged['int'].connect(self.adjustContrastLimits)
        

        autoContrastControl = qtw.QRadioButton()
        
        gammaControl = qtw.QSlider(Qt.Horizontal)
        gammaControl.setRange(-100, 100)
        gammaControl.setSliderPosition(0)
        contrastLimitsControl.setSingleStep(1)
        gammaControl.valueChanged['int'].connect(self.adjustGamma)

        colorControl = qtw.QComboBox()
        blendingControl = qtw.QComboBox()
        interpolationControl = qtw.QComboBox()
        fileExplorerButton = qtw.QPushButton("File")
        saveButton = qtw.QPushButton("Save")


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

        menuBox.layout().addWidget(fileExplorerButton)
        menuBox.layout().addWidget(saveButton)

        controlBox.layout().addWidget(controls)
        self.layout().addWidget(controlBox)
        controlBox.layout().addWidget(menuBox)
    
    