import PyQt5.QtWidgets as qtw
from View.ImageArea.CanvasView import CanvasView
from View.ImageArea.OpenFilesMenu import OpenFilesMenu
from Presenter.ImageAreaPresenter import ImageAreaPresenter

class ImageAreaView(qtw.QWidget):
    '''
    A container holding the image as well as a menubar that displays the open files. FIXME move the filebar to the toolbars or dock widgets layer
    '''
    def __init__(self):
        super().__init__()
        self.presenter = ImageAreaPresenter(self)
        #Overarching widget that holds the image area together
        self.setLayout(qtw.QVBoxLayout())

        #the currently open files 
        # #FIXME this is likely no longer a useful widget  replace with a frame number counter increment and decrement buttons 
        # and an index search.
        self.layout().setMenuBar(OpenFilesMenu())
        #the canvas
        self.layout().addWidget(CanvasView())

        print("image area initalized")

