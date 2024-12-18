from Model.AcceptedFormats.Displayable import Displayable

class StandardImage(Displayable):
    def __init__(self, fileName : str):
        super().__init__(fileName)