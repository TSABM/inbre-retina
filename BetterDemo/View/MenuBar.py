import PyQt5.QtWidgets as qtw

from Presenter import MenuBarPresenter

class MenuBar():
    #initalize menubar and the selectable options
    def __init__(self, parentLayout):
        self.parentLayout = parentLayout
        #main menu
        self.menu = qtw.QMenuBar()
        self.parentLayout.setMenuBar(self.menu)

        #actions
        actions = []
        
        openFolder = qtw.QAction("Open Folder", self.parentLayout)
        openFolder.triggered.connect(self.parentLayout.openFolder)
        actions.append(openFolder)

        exit = qtw.QAction("Exit", self.parentLayout)
        exit.triggered.connect(self.parentLayout.closeApplication)
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
        fileDialog = qtw.QFileDialog(self)
        directoryPath = fileDialog.getExistingDirectory()
        #Send the directory path off for file list extraction
        MenuBarPresenter.MenuBarPresenter.getFilteredFolderContents(directoryPath)

    def closeApplication(self):
        MenuBarPresenter.MenuBarPresenter.closeApplication()