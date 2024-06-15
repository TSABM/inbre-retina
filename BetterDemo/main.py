#demo application
import PyQt5.QtWidgets as qtw
import View.MainWindow as MainWindow


app = qtw.QApplication([])
window = MainWindow.MainWindow()
app.exec_()
