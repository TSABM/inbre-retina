import PyQt5.QtWidgets as qtw

class OpenFilesMenu():
    def __init__(self, parentWidget):
        menuContainer = qtw.QWidget()
        menuContainer.setLayout(qtw.QHBoxLayout())
        menu = qtw.QMenuBar()
        ''' #FIXME this is a bit of initial test code, remove when confident its working correctly
        for i in range(30):  # Add 30 demo items
            action = qtw.QAction(f"Item {i+1}", menu)
            menu.addAction(action)
        '''
        menuContainer.layout().setMenuBar(menu)
        parentWidget.layout().addWidget(menuContainer)