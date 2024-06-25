'''
A presenter to act as a middleman between the view and model
'''

from Presenter.AbstractPresenter import AbstractPresenter


from Model.WindowMenuBarModel import WindowMenuBarModel

class WindowMenuBarPresenter(AbstractPresenter):
    
    def __init__(self, view):
        super().__init__(view, WindowMenuBarModel())
        pass
    

    def openImage(self, fileDialog):
        '''
        opens a dialog and returns one selected image
        '''
        fileDialog.setFilter("Images (*.png *.jpg *jpeg)")
        imagePath = fileDialog.getOpenFile()
        

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