#demo application
import PyQt5.QtWidgets as qtw

import View.MainWindowView

print("starting")
app = qtw.QApplication([])

mainView = View.MainWindowView.MainWindowView()

mainView.show()
app.exec_()
