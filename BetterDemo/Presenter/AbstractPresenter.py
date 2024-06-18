from abc import ABC, abstractmethod

class AbstractPresenter(ABC):
    @abstractmethod
    def __init__(self, view, model = None):
        self.view  = view
        self.model = model