#demo application
import PyQt5.QtWidgets as qtw

from View.MainWindowView import MainWindowView
from Model.OpenScenes import OpenScenes

print("starting")
app = qtw.QApplication([])

#Initalize the container that holds the scenes
openScenes = OpenScenes()

#Initalize the main view
mainView = MainWindowView()

#display the main view
mainView.show()
app.exec_()
