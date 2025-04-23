import PyQt5.QtWidgets as qtw
from PyQt5.QtWidgets import QApplication


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
    
    def openProject(self):
        print("opening project")
        try:
            #open file dialog
            folderDialog = qtw.QFileDialog(self)
        except Exception as e:
            print(f"exception raised: {e}")
            return
        folderPath = folderDialog.getExistingDirectory()
        if folderPath == "":
            print("No directory selected")
        else:
            self.presenter.openProject(folderPath)

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
            print("No file selected, aborting")
            return
        projectName = "temporaryProjectName"
        self.presenter.openImage(imagePath, projectName)

    def exportLabels(self):
        print("user export request received, attempting to pass along ")
        # Ask the user for a file name
        text, ok = qtw.QInputDialog.getText(self, "Export File Name", "Enter a name for the export file:")
        
        if ok and text.strip():  # If user pressed OK and entered something
            exportFileName = text.strip()
            print(f"Export filename entered: {exportFileName}")
            
            # ask for destination directory
            exportDir = qtw.QFileDialog.getExistingDirectory(self, "Select Export Directory")
            if not exportDir:
                print("No export directory selected")
                return

            # Join the directory and file name
            import os
            projectDestinationPath = os.path.join(exportDir, exportFileName)
            overwriteMode = True  # You can add a checkbox later for this
            self.presenter.exportLabelData(projectDestinationPath, overwriteMode)
        else:
            print("Export cancelled or no filename entered")

    def closeApplication(self):
        #self.presenter.closeApplication()
        QApplication.quit()

    def __generateMainActions__(self):
        actions = []

        #newProject = qtw.QAction("New...", self)
        #newProject.triggered.connect(self.createNewProject)
        #actions.append(newProject)

        openImage = qtw.QAction("New project from image or video", self)
        openImage.triggered.connect(self.openImage)
        actions.append(openImage)


        importLabels = qtw.QAction("Open existing project", self)
        importLabels.triggered.connect(self.openProject)
        actions.append(importLabels)

        exportLabels = qtw.QAction("Export labels in project format", self)
        exportLabels.triggered.connect(self.exportLabels)
        actions.append(exportLabels)

        exit = qtw.QAction("Exit", self)
        exit.triggered.connect(self.closeApplication)
        actions.append(exit)
        return actions