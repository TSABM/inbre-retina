import PyQt5.QtWidgets as qtw


from Presenter.WindowMenuBarPresenter import WindowMenuBarPresenter

class WindowMenuBarView(qtw.QMenuBar):
    #initalize menubar and the selectable options
    def __init__(self):
        #main menu
        super().__init__()

        self.presenter = WindowMenuBarPresenter(self)

        actions = []

        newProject = qtw.QAction("New...", self)
        newProject.triggered.connect(self.createNewProject)
        actions.append(newProject)

        openImage = qtw.QAction("Open Image", self)
        openImage.triggered.connect(self.openImage)
        actions.append(openImage)
        
        openFolder = qtw.QAction("Open Folder", self)
        openFolder.triggered.connect(self.openFolder)
        actions.append(openFolder)

        exit = qtw.QAction("Exit", self)
        exit.triggered.connect(self.closeApplication)
        actions.append(exit)
        

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
    
    #FIXME send some of this logic to the presenter layer
    def openImage(self):
        fileDialog = qtw.QFileDialog(self)
        #fileDialog.setFileMode(qtw.QFileDialog.AnyFile)
        #fileDialog.setFilter("Images (*.png *.jpg *jpeg)")
        imagePath = fileDialog.getOpenFileName()[0]
        print(imagePath)
        self.presenter.openImage(imagePath)
        #FIXME need to figure out how to send the image path data to somewhere to be rendered...
        #Send to image area menu?
        #from image area menu send to canvas as new layer/base layer?

    def openFolder(self):
        #Open file dialog
        fileDialog = qtw.QFileDialog(self)
        directoryPath = fileDialog.getExistingDirectory()
        #Send the directory path off for file list extraction
        self.presenter.getFilteredFolderContents(directoryPath)

    def closeApplication(self):
        self.presenter.closeApplication()