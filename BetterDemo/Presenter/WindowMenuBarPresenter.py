'''
A presenter to act as a middleman between the view and model
'''
from Presenter.AbstractPresenter import AbstractPresenter
from Model.WindowMenuBarModel import WindowMenuBarModel
from Model.LabelExporter import LabelExporter


class WindowMenuBarPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
        self.__generalModel = WindowMenuBarModel()
        self.__exportModel = LabelExporter()
    
    def refresh(self):
        super().refresh()

    def openImage(self, imagePath):
        '''
        opens a dialog and returns one selected image
        '''
        #set the open image
        self.__generalModel.openImage(imagePath)

    def exportLabelData(self):
        #FIXME add error catching
        self.__exportModel.export()

    def closeApplication(self):
        '''
        FIXME Sends a request to close the application
        '''
        print("FIXME close app unimplmented")