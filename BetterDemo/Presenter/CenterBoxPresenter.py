from Presenter.AbstractPresenter import AbstractPresenter
from Presenter.MainControlsPresenter import MainControlsPresenter
from Presenter.ImageAreaPresenter import ImageAreaPresenter
from View.CenterBox import CenterBox

class CenterBoxPresenter(AbstractPresenter):
    def __init__(self):
        super().__init__(CenterBox(), None)

        #create the main controls view
        self.mainControlsPresenter = MainControlsPresenter()
        #add the main controls view
        self.view.addMainControlsArea(self.mainControlsPresenter.getView())

        #create the image area view
        self.imageAreaPresenter = ImageAreaPresenter()
        #add the image area view
        self.view.addImageArea(self.imageAreaPresenter.getView())