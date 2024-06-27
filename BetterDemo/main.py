#demo application
import PyQt5.QtWidgets as qtw

from View.MainWindowView import MainWindowView
from Model.masterMemory import MasterMemory

print("starting")
app = qtw.QApplication([])

#Initalize the master memory, this will hold the subscribers
masterMemory = MasterMemory()

#Initalize the main view
mainView = MainWindowView()

#display the main view
mainView.show()
app.exec_()
