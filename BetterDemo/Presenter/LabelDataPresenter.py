from Presenter.AbstractPresenter import AbstractPresenter

class LabelDataPresenter(AbstractPresenter):
    def __init__(self, view):
        super().__init__(view)
        #send label data area to the master memory
        self.registerNewSubscriber("labelData", self)
        self.addSubscriber("canvas")
    
    def refresh(self):
        super().refresh()
        #print("attempted to refresh label data")
        label = self.getSubscriberByKey("canvas").getSelectedLabel()
        self.view.setLabelToDisplay(label)
        self.view.displayLabelData()
    
    def getMaxXVal(self):
        return 9999 #temp number

    def getMaxYVal(self):
        return 9999