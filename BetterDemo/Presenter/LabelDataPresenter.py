from Presenter.AbstractPresenter import AbstractPresenter

class LabelDataPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
        #send label data area to the master memory
        self.registerNewSubscriber("labelData", self)