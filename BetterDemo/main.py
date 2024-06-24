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

#mainModel = Model.MainWindowModel.MainWindowModel() #FIXME
mainView = View.MainWindowView.MainWindowView()
mainPresenter = Presenter.MainWindowPresenter.MainWindowPresenter(mainView, None) #possibly FIXME

mainView.show()
app.exec_()
