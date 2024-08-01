import PyQt5.QtWidgets as qtw
from View.ImageArea.CanvasView import CanvasView
from BetterDemo.Model.Canvases.MovieCanvas import MovieCanvas
from View.ImageArea.OpenFilesMenu import OpenFilesMenu
from Presenter.ImageAreaPresenter import ImageAreaPresenter
from PyQt5.QtGui import QPainter, QMovie

class MediaAreaView(qtw.QWidget):
    '''
    This is the media area. Used to hold the image/video and the direct controls for it
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
        #note that I probably need to add some sort of ability to zoom in and out.
        self.layout().addWidget(CanvasView())
        
        #Video controls
        #FIXME note that video controls should load only for videos not single images

        print("image area initalized")

