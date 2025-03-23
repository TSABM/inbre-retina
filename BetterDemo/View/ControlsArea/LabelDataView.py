import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt
from Presenter.LabelDataPresenter import LabelDataPresenter

class LabelDataView(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.presenter = LabelDataPresenter(self)
        self.initUI()
    
    def initUI(self):
        layout = qtw.QVBoxLayout()
        
        self.dataContainer = qtw.QScrollArea()
        self.dataContainer.setWidgetResizable(True)
        self.dataWidget = qtw.QWidget()
        self.dataLayout = qtw.QVBoxLayout()
        self.dataWidget.setLayout(self.dataLayout)
        self.dataContainer.setWidget(self.dataWidget)
        
        layout.addWidget(self.dataContainer)
        
        self.refreshButton = qtw.QPushButton("Refresh Data")
        self.refreshButton.clicked.connect(self.reloadLabelData)
        layout.addWidget(self.refreshButton)

        self.setLayout(layout)
    
    def reloadLabelData(self):
        label_data = self.presenter.getLabelData()
        self.populateUI(label_data)
    
    def populateUI(self, data):
        for i in reversed(range(self.dataLayout.count())):
            widget = self.dataLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        
        self.buildUIComponents(self.dataLayout, data)
    
    def buildUIComponents(self, parent_layout, data, indent=0):
        if isinstance(data, dict):
            for key, value in data.items():
                label = qtw.QLabel(f"{' ' * indent}{key}:")
                parent_layout.addWidget(label)
                self.buildUIComponents(parent_layout, value, indent + 2)
        elif isinstance(data, list):
            for index, value in enumerate(data):
                label = qtw.QLabel(f"{' ' * indent}[{index}]:")
                parent_layout.addWidget(label)
                self.buildUIComponents(parent_layout, value, indent + 2)
        else:
            value_label = qtw.QLabel(f"{' ' * indent}{data}")
            value_label.setAlignment(Qt.AlignLeft) # type: ignore
            parent_layout.addWidget(value_label)
