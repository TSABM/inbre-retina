#FIXME replace most or all instances of self with the main window instance or layout or whatever, setmenubar needs the main window
class MenuBar():
    menu = qtw.QMenuBar()
    def __init__():
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

    def closeApplication(self):
        print("exiting application")
        sys.exit()