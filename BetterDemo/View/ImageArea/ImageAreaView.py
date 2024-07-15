import PyQt5.QtWidgets as qtw
from View.ImageArea.CanvasView import CanvasView
from View.ImageArea.OpenFilesMenu import OpenFilesMenu
from Presenter.ImageAreaPresenter import ImageAreaPresenter
from View.AbstractView import AbstractView

class ImageAreaView(AbstractView):
    '''
    A container holding the image as well as a menubar that displays the open files. FIXME move the filebar to the toolbars or dock widgets layer
    '''
    def __init__(self):
        super().__init__(qtw.QWidget())
        self.presenter = ImageAreaPresenter(self.viewWidget)
        #Overarching widget that holds the image area together
        self.viewWidget.setLayout(qtw.QVBoxLayout())

        #the currently open files
        openFilesMenu = OpenFilesMenu()
        self.viewWidget.layout().setMenuBar(openFilesMenu.getWidget())

        #the canvas
        canvas = CanvasView()
        self.viewWidget.layout().addWidget(canvas.getWidget())

        print("image area initalized")
    
    def refresh(self):
        super().refresh()
        pass

