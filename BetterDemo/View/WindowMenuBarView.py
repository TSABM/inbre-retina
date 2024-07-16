import PyQt5.QtWidgets as qtw
from View.AbstractView import AbstractView


from Presenter.WindowMenuBarPresenter import WindowMenuBarPresenter

class WindowMenuBarView(AbstractView):
    #initalize menubar and the selectable options
    def __init__(self):
        #main menu
        super().__init__(qtw.QMenuBar())

        self.presenter = WindowMenuBarPresenter(self.viewWidget)

        actions = self.generateMainActions()

        #submenus
        fileButton = qtw.QMenu("File", self.viewWidget)
        self.viewWidget.addMenu(fileButton)
        settingsButton = qtw.QMenu("Settings", self.viewWidget)
        self.viewWidget.addMenu(settingsButton)

        #add actions to buttons
        fileButton.addActions(actions)

        print("main menu bar initalized")
    

    def refresh(self):
        '''
        redraw view with updated data
        '''
        super().refresh()
        pass #FIXME 


    def getMenuBar(self):
        return self.viewWidget

    #Selectable options below here
    def createNewProject(self):
        print("unimplemented")
        pass
    
    #FIXME send some of this logic to the presenter layer or the model?
    def openImage(self):
        print("opening image")
        try:
            fileDialog = qtw.QFileDialog(self.viewWidget)
            if fileDialog.exec_():
                print("file dialog executed")
        except Exception as e:
            print(f"exception raised: {e}")
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
        fileDialog = qtw.QFileDialog(self.viewWidget)
        directoryPath = fileDialog.getExistingDirectory()
        #Send the directory path off for file list extraction
        self.presenter.getFilteredFolderContents(directoryPath)

    def closeApplication(self):
        self.presenter.closeApplication()

    def generateMainActions(self):
        actions = []

        newProject = qtw.QAction("New...", self.viewWidget)
        newProject.triggered.connect(self.createNewProject)
        actions.append(newProject)

        openImage = qtw.QAction("Open Image", self.viewWidget)
        openImage.triggered.connect(self.openImage)
        actions.append(openImage)
        
        openFolder = qtw.QAction("Open Folder", self.viewWidget)
        openFolder.triggered.connect(self.openFolder)
        actions.append(openFolder)

        exit = qtw.QAction("Exit", self.viewWidget)
        exit.triggered.connect(self.closeApplication)
        actions.append(exit)
        return actions