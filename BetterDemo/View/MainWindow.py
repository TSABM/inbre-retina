'''
Main window structure and contents. Defer rendering though to a view
'''
import PyQt5.QtWidgets as qtw
import View.WindowMenuBar as WindowMenuBar, CenterBox

class MainWindow(qtw.QMainWindow):
    def __init__(self):#telling main window to init 
        super().__init__()
        self.setWindowTitle("DemoApp")

        self.menuBar = WindowMenuBar(self) #initalize menubar and pass main window

        self.centerBox = CenterBox(self)

        self.show()