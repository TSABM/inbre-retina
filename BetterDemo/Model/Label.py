

class Label():
    '''
    A rectangular box which "labels" or indicates the presence of something. Also contains data about what the object being labelled is.
    '''
    def __init__(self, frameNumber: int, topLCornerLocation: tuple, bottomRCornerLocation: tuple, type: str, itemID: str, description: str = ""):
        self.frameNumber = frameNumber
        self.topLeftCornerLocation = topLCornerLocation
        self.bottomRightCornerLocation = bottomRCornerLocation
        self.itemId = itemID
        self.type = type
        self.description = description