#demo application
import PyQt5.QtWidgets as qtw
import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class MainWindow(qtw.QMainWindow):
    def __init__(self):#telling main window to init 
        super().__init__()
        self.setWindowTitle("DemoApp")
        self.menuBar()

        mainBox = qtw.QSplitter(Qt.Horizontal)
        mainBox.setChildrenCollapsible(False)
        self.setCentralWidget(mainBox)
        
        
        self.mainControls(mainBox)
        self.imageDisplay(mainBox)


        self.show()

    def menuBar(self):
        #main menu
        menu = qtw.QMenuBar()
        self.setMenuBar(menu)

        #actions
        actions = []
        
        openFolder = qtw.QAction("Open Folder", self)
        openFolder.triggered.connect(self.openFolder)
        actions.append(openFolder)

        exit = qtw.QAction("Exit", self)
        exit.triggered.connect(self.closeApplication)
        actions.append(exit)

        #submenus
        fileButton = qtw.QMenu("File", self)
        menu.addMenu(fileButton)
        settingsButton = qtw.QMenu("Settings", self)
        menu.addMenu(settingsButton)

        #add actions to buttons
        fileButton.addActions(actions)

    def mainControls(self, mainBox):
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
        mainBox.addWidget(controlBox)

    def imageDisplay(self, mainBox):
        mainBox.label = qtw.QLabel(mainBox)
        pixmap = QPixmap('demoImage.jpg')
        if pixmap.isNull():
            print("failed to load image")
        mainBox.label.setPixmap(pixmap)
        mainBox.addWidget(mainBox.label)

    def closeApplication(self):
        print("exiting application")
        sys.exit()

    def openFolder(self):
        print("partially tested")

        #Open a file dialog to identify the directory to open
        fileDialog = qtw.QFileDialog(self)
        fileDialog.setFileMode(qtw.QFileDialog.Directory) #FIXME wont grab directories only grabbing files
        fileURL = fileDialog.getOpenFileUrl()

        #open folder
        files = os.listdir(fileURL[1])
        #now filter out all files of incompatable types
        filteredFiles = self.filterFileList(files)
        #then store the remaining files somewhere for interaction
        return filteredFiles

    def filterFileList(self, fileList):
        print("filtering is unimplemented")

    def loadImage(self):
        print("unimplemented")
    
    def adjustOpacity(self, value):
        print("opacity: ", value)
    
    def adjustContrastLimits(self, value):
        print("contrast lim: ", value)

    def toggleAutoContrast(self):
        print("unimplemented")
    
    def adjustGamma(self):
        print("unimplemented")

    def adjustGamma(self):
        print("unimplemented")
    
    def selectColor(self):
        print("unimplemented")

    def selectBlending(self):
        print("unimplemented")
    
    def selectInterpolation(self):
        print("unimplemented")
        

app = qtw.QApplication([])
window = MainWindow()
app.exec_()
