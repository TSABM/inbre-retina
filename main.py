#demo application
import PyQt5.QtWidgets as qtw
import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class MainWindow(qtw.QMainWindow):

    openFiles = []

    def __init__(self):#telling main window to init 
        super().__init__()
        self.setWindowTitle("DemoApp")
        self.menuBar()

        mainBox = qtw.QSplitter(Qt.Horizontal)
        mainBox.setChildrenCollapsible(False)
        self.setCentralWidget(mainBox)
        
        
        self.mainControls(mainBox) #FIXME need to rework this into a controls Dock widget with more pertinent contents
        self.imageArea(mainBox) # FIXME need to rework into an image boc holding the image and the toolbar


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

    def imageArea(self, mainBox):
        '''
        mainBox.label = qtw.QLabel(mainBox)
        pixmap = QPixmap('demoImage.jpg')
        if pixmap.isNull():
            print("failed to load image")
        mainBox.label.setPixmap(pixmap)
        mainBox.addWidget(mainBox.label)
        '''
        #Overarching widget that holds the image area together
        displayArea = qtw.QWidget()
        displayArea.setLayout(qtw.QVBoxLayout())
        mainBox.addWidget(displayArea)

        #scrollable contents
        menuContainer = qtw.QWidget()
        menuContainer.setLayout(qtw.QHBoxLayout())
        

        menu = qtw.QMenuBar()
        for i in range(30):  # Add 30 demo items
            action = qtw.QAction(f"Item {i+1}", menu)
            menu.addAction(action)
        
        menuContainer.layout().setMenuBar(menu)
        displayArea.layout().addWidget(menuContainer)

        #Widget that holds the graphical interface

        scene = qtw.QGraphicsScene(0, 0, 400, 200)
        view = qtw.QGraphicsView(scene)
        displayArea.layout().addWidget(view)
        

    def closeApplication(self):
        print("exiting application")
        sys.exit()

    def openFolder(self):
        print("opening folder dialog")

        #Open a file dialog to identify the directory to open
        fileDialog = qtw.QFileDialog(self)
        directoryPath = fileDialog.getExistingDirectory()
        #print("directory path is: ", directoryPath)

        #open folder
        files = os.listdir(directoryPath)
        #now filter out all files of incompatable types
        filteredFiles = self.filterFileList(files)
        #now update the filtered files to include the whole path
        fullPathFiles = []
        for file in filteredFiles:
            filePath = directoryPath + "/" + file
            fullPathFiles.append(filePath)
        #then store the remaining files somewhere for interaction
        #print(fullPathFiles)
        return fullPathFiles

    def filterFileList(self, fileList):
        print("filtering for jpeg, jpg, and png")

        filteredList = []
        for file in fileList:
            if ".jpeg" in file or ".png" in file or ".jpg" in file:
                filteredList.append(file)
        #print(filteredList)
        return filteredList

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
