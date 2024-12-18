import PyQt5.QtWidgets as qtw


from Presenter.WindowMenuBarPresenter import WindowMenuBarPresenter

class WindowMenuBarView(qtw.QMenuBar):
    #initalize menubar and the selectable options
    def __init__(self):
        #main menu
        super().__init__()
        self.presenter = WindowMenuBarPresenter(self)
        actions = self.__generateMainActions__()
        #submenus
        fileButton = qtw.QMenu("File", self)
        self.addMenu(fileButton)
        settingsButton = qtw.QMenu("Settings", self)
        self.addMenu(settingsButton)
        #add actions to buttons
        fileButton.addActions(actions)
        print("main menu bar initalized")

    #Selectable options below here
    def createNewProject(self):
        print("unimplemented")
        pass
    
    def openImage(self):
        print("opening image")
        try:
            #open file dialog
            fileDialog = qtw.QFileDialog(self)
            
        except Exception as e:
            print(f"exception raised: {e}")
            return
        
        
        imagePath = fileDialog.getOpenFileName()[0]
        print(imagePath)
        #open image
        if imagePath == "":
            print("No file selected")
        else:
            self.presenter.openImage(imagePath)

    def importLabels(self):
        pass

    def exportLabels(self):
        print("user export request received, attempting to pass along ")
        exportFileName = "testExportFilename"
        destinationPath = ""
        overwriteMode = True
        self.presenter.exportLabelData(exportFileName, destinationPath, overwriteMode)
        pass

    def closeApplication(self):
        self.presenter.closeApplication()

    def __generateMainActions__(self):
        actions = []

        newProject = qtw.QAction("New...", self)
        newProject.triggered.connect(self.createNewProject)
        actions.append(newProject)

        openImage = qtw.QAction("Open image", self)
        openImage.triggered.connect(self.openImage)
        actions.append(openImage)
        

        importLabels = qtw.QAction("Import labels", self)
        importLabels.triggered.connect(self.importLabels)
        actions.append(importLabels)

        exportLabels = qtw.QAction("Export labels", self)
        exportLabels.triggered.connect(self.exportLabels)
        actions.append(exportLabels)

        exit = qtw.QAction("Exit", self)
        exit.triggered.connect(self.closeApplication)
        actions.append(exit)
        return actions