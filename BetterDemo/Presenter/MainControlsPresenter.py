from AbstractPresenter import AbstractPresenter
from View.MainControls import MainControls

class MainControlsPresenter(AbstractPresenter):
    def __init__(self):
        super().__init__(MainControls, None)
        
    