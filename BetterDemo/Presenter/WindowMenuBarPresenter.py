'''
A presenter to act as a middleman between the view and model
'''

from Presenter.AbstractPresenter import AbstractPresenter
from Model.WindowMenuBarModel import WindowMenuBarModel

class WindowMenuBarPresenter(AbstractPresenter):
    
    def __init__(self, view):
        super().__init__(view)
        self.model = WindowMenuBarModel()
        pass
    

    def openImage(self, imagePath):
        '''
        opens a dialog and returns one selected image
        '''
        
        self.model.openImage(imagePath)
        

    def getFilteredFolderContents(self, directoryPath):
        '''
        requests filtered contents of a selected directory
        '''

        self.model.openFolder(directoryPath)
        pass


    def closeApplication(self):
        '''
        FIXME Sends a request to close the application
        '''
        print("FIXME")