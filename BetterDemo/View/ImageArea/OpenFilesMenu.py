import PyQt5.QtWidgets as qtw
import main

class OpenFilesMenu(qtw.QMenuBar):
    def __init__(self):
        super().__init__()
        #menuContainer = qtw.QWidget()
        #menuContainer.setLayout(qtw.QHBoxLayout())
        #menu = qtw.QMenuBar()
        ''' #FIXME this is a bit of initial test code, remove when confident its working correctly
        for i in range(30):  # Add 30 demo items
            action = qtw.QAction(f"Item {i+1}", menu)
            menu.addAction(action)
        '''
        #menuContainer.layout().setMenuBar(menu)
        #parentWidget.layout().addWidget(menuContainer)

        print("open files menubar initalized")