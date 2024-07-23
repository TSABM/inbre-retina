from Presenter.AbstractPresenter import AbstractPresenter
#from View.MainControlsView import MainControlsView
from Model.masterMemory import MasterMemory

class MainControlsPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
        
    def setInteractionMode(self, mode : str):
        MasterMemory.setInteractionMode(mode)
    