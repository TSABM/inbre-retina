'''
A presenter to act as a middleman between the view and model
'''

from Presenter.AbstractPresenter import AbstractPresenter
from Model.WindowMenuBarModel import WindowMenuBarModel
from View.WindowMenuBarView import WindowMenuBarView

class WindowMenuBarPresenter(AbstractPresenter):
    
    def __init__(self):
        super().__init__(WindowMenuBarView(), WindowMenuBarModel())
        pass
    
    def openImage(self, fileDialog):
        '''
        opens a dialog and returns one selected image
        '''
        fileDialog.setFilter("Images (*.png *.jpg *jpeg)")
        imagePath = fileDialog.selectFile()
        self.model.openImage(imagePath)

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