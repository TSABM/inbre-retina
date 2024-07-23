from PyQt5.QtCore import QRect

class Label():
    '''
    A rectangular box which "labels" or indicates the presence of something. Also contains data about what the object being labelled is.
    '''
    def __init__(self, frameNumber: int, rectangle : QRect, type: str, itemID: str, description: str = ""):
        self.frameNumber : int = frameNumber
        self.rectangle : QRect = rectangle
        self.itemId : str = itemID
        self.type : str = type
        self.description : str = description