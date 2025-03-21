import PyQt5.QtWidgets as qtw

from Presenter.MainControlsPresenter import MainControlsPresenter

class MainControlsView(qtw.QWidget):
    '''
    The primary control widgets for the app.
    '''
    def __init__(self):
        super().__init__()
        self.presenter = MainControlsPresenter(self)
        #setting layout
        self.setLayout(qtw.QVBoxLayout())
        self.__addControls__()
        print("main controls initalized")

    def __addControls__(self):
        pass

    def playVideo(self):
        self.presenter