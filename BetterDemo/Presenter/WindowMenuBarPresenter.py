'''
A presenter to act as a middleman between the view and model
'''

import AbstractPresenter
from Model import WindowMenuBarModel

class WindowMenuBarPresenter(AbstractPresenter):
    
    def __init__(self, mainWindow):
        super().__init__(mainWindow)
    
    def getFilteredFolderContents(self, directoryPath):
        '''
        requests filtered contents of a selected directory
        '''
        WindowMenuBarModel.WindowMenuBarModel.openFolder(directoryPath)


    def closeApplication(self):
        '''
        FIXME Sends a request to close the application
        '''
        print("FIXME")