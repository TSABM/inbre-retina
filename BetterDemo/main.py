#demo application
import PyQt5.QtWidgets as qtw
from View import MainWindow


app = qtw.QApplication([])
window = MainWindow.MainWindow()
app.exec_()
