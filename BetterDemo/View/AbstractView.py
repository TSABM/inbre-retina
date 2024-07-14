from abc import ABC, abstractmethod


class AbstractView(ABC):
    @abstractmethod
    def __init__(self, viewWidget):
        self.viewWidget = viewWidget
        pass

    @abstractmethod
    def refresh(self):
        pass

    def getWidget(self):
        return self.viewWidget