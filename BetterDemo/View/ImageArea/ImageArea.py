import PyQt5.QtWidgets as qtw
import CanvasView
import OpenFilesMenu

class ImageArea():
    '''
    A container holding the image as well as a menubar that displays the open files. FIXME move the filebar to the toolbars or dock widgets layer
    '''
    def __init__(self, parentWidget):
        #Overarching widget that holds the image area together
        self.displayArea = qtw.QWidget()
        self.displayArea.setLayout(qtw.QVBoxLayout())
        parentWidget.addWidget(self.displayArea)

        #A file "menu" for the open files in a folder
        self.openFilesMenu = OpenFilesMenu(self.displayArea)

        #rendering the canvas
        self.canvas = CanvasView(self.displayArea)