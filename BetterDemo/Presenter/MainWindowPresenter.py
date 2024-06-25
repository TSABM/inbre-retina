from Presenter.AbstractPresenter import AbstractPresenter
#from Presenter.WindowMenuBarPresenter import WindowMenuBarPresenter
#from Presenter.CenterBoxPresenter import CenterBoxPresenter

class MainWindowPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view, None)