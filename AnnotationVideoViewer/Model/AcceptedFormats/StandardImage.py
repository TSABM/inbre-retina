#pylint: disable = no-name-in-module
from Model.AcceptedFormats.Displayable import Displayable
from PyQt5.QtGui import QImage, QPixmap

class StandardImage(Displayable):
    '''
    class that accepts bmp, jpeg, jpg, png, gif, tiff, ppm, xbm, xpm, and webp
    '''
    def __init__(self, fileName : str):
        super().__init__(fileName)
        self.image : QImage | None = None
      
    def setImage(self, imagePath : str) -> bool:
        if imagePath != None:
            image =  QImage(imagePath)
            if image.isNull():
                print("set image failure. failure to load or incorrect format. image path was: " + imagePath)
                return False
            else:
                self.image = image
                print("image set")
                return True
            
        
    def getPixmap(self) -> QPixmap | None:
        if self.image != None:
            return QPixmap.fromImage(self.image)
        else:
            return None
    
    def getTotalFrames(self) -> int:
        super().getTotalFrames()
        return 1