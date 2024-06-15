'''
The area that holds the images and directly related gui I reckon
'''
class ImageArea():
    def __init__(self):
        print("unimplemented")

    def imageArea(self, mainBox):
        '''
        A container holding the image as well as a file loader bar. FIXME move the filebar to the toolbars or dock widgets layer
        '''
        #Overarching widget that holds the image area together
        displayArea = qtw.QWidget()
        displayArea.setLayout(qtw.QVBoxLayout())
        mainBox.addWidget(displayArea)

        #A file "menu" for the images in a folder
        menuContainer = qtw.QWidget()
        menuContainer.setLayout(qtw.QHBoxLayout())
        menu = qtw.QMenuBar()
        ''' #this is a bit of initial test code, remove when confident its working correctly
        for i in range(30):  # Add 30 demo items
            action = qtw.QAction(f"Item {i+1}", menu)
            menu.addAction(action)
        '''
        menuContainer.layout().setMenuBar(menu)
        displayArea.layout().addWidget(menuContainer)


        scene = qtw.QGraphicsScene(0, 0, 400, 200)
        view = qtw.QGraphicsView(scene)
        displayArea.layout().addWidget(view)