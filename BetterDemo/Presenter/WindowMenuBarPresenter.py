'''
A presenter to act as a middleman between the view and model
'''

#from AbstractPresenter import AbstractPresenter
from Model.WindowMenuBarModel import WindowMenuBarModel

class WindowMenuBarPresenter():
    
    def __init__(self):
        self.model = WindowMenuBarModel()
        pass
    
    def getFilteredFolderContents(self, directoryPath):
        '''
        requests filtered contents of a selected directory
        '''

        self.model.openFolder(directoryPath)


    def closeApplication(self):
        '''
        FIXME Sends a request to close the application
        '''
        print("FIXME")