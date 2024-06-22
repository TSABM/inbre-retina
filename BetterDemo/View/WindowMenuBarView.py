import PyQt5.QtWidgets as qtw


class WindowMenuBarView():
    #initalize menubar and the selectable options
    def __init__(self, parentLayout):
        self.parentLayout = parentLayout
        #main menu
        self.menu = qtw.QMenuBar()
        self.parentLayout.setMenuBar(self.menu)
        self.presenter = WindowMenuBarPresenter()

        #actions #FIXME move some of this to the model
        actions = []

        newProject = qtw.QAction("New...", self.parentLayout)
        newProject.triggered.connect(self.createNewProject)
        actions.append(newProject)

        openImage = qtw.QAction("Open Image", self.parentLayout)
        openImage.triggered.connect(self.OpenImage)
        actions.append(openImage)
        
        openFolder = qtw.QAction("Open Folder", self.parentLayout)
        openFolder.triggered.connect(self.openFolder)
        actions.append(openFolder)

        exit = qtw.QAction("Exit", self.parentLayout)
        exit.triggered.connect(self.closeApplication)
        actions.append(exit)
        

        #submenus
        fileButton = qtw.QMenu("File", self.parentLayout)
        self.menu.addMenu(fileButton)
        settingsButton = qtw.QMenu("Settings", self.parentLayout)
        self.menu.addMenu(settingsButton)

        #add actions to buttons
        fileButton.addActions(actions)
        
    #Selectable options below here
    def createNewProject(self):
        print("unimplemented")
        pass
    
    #FIXME send some of this logic to the presenter layer
    def openImage(self):
        fileDialog = qtw.QFileDialog(self.parentLayout)
        self.presenter.openImage(fileDialog)
        #FIXME need to figure out how to send the image path data to somewhere to be rendered...
        #Send to image area menu?
        #from image area menu send to canvas as new layer/base layer?

    def openFolder(self):
        #Open file dialog
        fileDialog = qtw.QFileDialog(self.parentLayout)
        directoryPath = fileDialog.getExistingDirectory()
        #Send the directory path off for file list extraction
        self.presenter.getFilteredFolderContents(directoryPath)

    def closeApplication(self):
        self.presenter.closeApplication()