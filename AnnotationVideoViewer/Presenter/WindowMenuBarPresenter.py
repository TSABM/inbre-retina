'''
A presenter to act as a middleman between the view and model
'''
from Presenter.AbstractPresenter import AbstractPresenter
from Model.WindowMenuBarModel import WindowMenuBarModel
from Model.ProjectExporter import ProjectExporter


class WindowMenuBarPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
        self.__generalModel = WindowMenuBarModel()
        self.__exportModel = ProjectExporter()

    def openProject(self, projectPath):
        self.__generalModel.openProject(projectPath)

    def openImage(self, imagePath, projectName):
        '''
        opens a dialog and returns one selected image
        '''
        #set the open image
        self.__generalModel.openImage(imagePath, projectName)

    def exportLabelData(self, projectDestinationPath : str, overwriteMode : bool):
        #FIXME add error catching
        print("Menu bar presenter passing along export request")
        self.__exportModel.export(projectDestinationPath, overwriteMode)