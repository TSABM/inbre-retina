from Presenter.AbstractPresenter import AbstractPresenter
from Presenter.WindowMenuBarPresenter import WindowMenuBarPresenter
from Presenter.CenterBoxPresenter import CenterBoxPresenter

class MainWindowPresenter(AbstractPresenter):
    def __init__(self, view, model):
        super().__init__(view, model)
        #create the menubar
        self.menuBarPresenter = WindowMenuBarPresenter()
        #add menubar to the view
        view.addMenuBar(self.menuBarPresenter.getView())

        #create the centerbox
        self.centerBoxPresenter = CenterBoxPresenter()
        #add the centerbox view to this view
        view.addCenterBox(self.centerBoxPresenter.getView())