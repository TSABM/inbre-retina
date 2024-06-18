import PyQt5.QtWidgets as qtw

from Presenter.WindowMenuBarPresenter import WindowMenuBarPresenter

class WindowMenuBar():
    #initalize menubar and the selectable options
    def __init__(self, parentLayout):
        self.parentLayout = parentLayout
        #main menu
        self.menu = qtw.QMenuBar()
        self.parentLayout.setMenuBar(self.menu)
        self.presenter = WindowMenuBarPresenter()

        #actions #FIXME move some of this to the model
        actions = []
        
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
    def openFolder(self):
        #Open file dialog
        fileDialog = qtw.QFileDialog(self.parentLayout)
        directoryPath = fileDialog.getExistingDirectory()
        #Send the directory path off for file list extraction
        self.presenter.getFilteredFolderContents(directoryPath)

    def closeApplication(self):
        self.presenter.closeApplication()