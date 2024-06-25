#demo application
import PyQt5.QtWidgets as qtw

import View.MainWindowView


app = qtw.QApplication([])

mainView = View.MainWindowView.MainWindowView()

mainView.show()
app.exec_()
