#demo application
import PyQt5.QtWidgets as qtw

#presenters
import Presenter
#models
import Model
#views
import Presenter.MainWindowPresenter
import View
import View.MainWindowView


app = qtw.QApplication([])

mainModel = Model.
mainView = View.MainWindowView.MainWindowView()
mainPresenter = Presenter.MainWindowPresenter.MainWindowPresenter()

mainView.show()
app.exec_()
