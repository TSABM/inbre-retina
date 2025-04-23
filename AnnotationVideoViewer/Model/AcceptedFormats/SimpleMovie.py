from PyQt5.QtGui import QMovie, QPixmap
#from PyQt5.QtCore import QUrl
#from PyQt5.QtMultimedia import QMediaPlayer
#from Model.AcceptedFormats.Displayable import Displayable
from Model.AcceptedFormats.CompatableVideo import CompatableVideo

class SimpleMovie(CompatableVideo):
    def __init__(self, fileName: str):
        super().__init__(fileName)
        #self.movie: QMovie | None = None

    def setFrame(self, frame: int):
        """Set the frame of the movie."""
        if not self.movie:
            print("No movie loaded.")
            return
        self.movie.jumpToFrame(frame)

    def getPixmap(self) -> QPixmap | None:
        """Return the current pixmap from the movie."""
        if not self.movie:
            print("No movie loaded.")
            return None
        return self.movie.currentPixmap()

    def getTotalFrames(self) -> int:
        """Get total frames of the movie."""
        if not self.movie:
            return 0
        return self.movie.frameCount()

    def setMovie(self, moviePath: str) -> bool:
        """Set the movie file."""
        self.movie = QMovie(moviePath)
        if not self.movie.isValid():
            print("Invalid movie format.")
            return False
        return True

    def startMovie(self):
        """Start movie playback."""
        if not self.movie:
            print("No movie loaded.")
            return
        self.movie.start()

    def stopMovie(self):
        """Stop movie playback."""
        if not self.movie:
            print("No movie loaded.")
            return
        self.movie.stop()

    def stepFrameForward(self):
        """Step to the next frame in the movie."""
        if not self.movie:
            print("No movie loaded.")
            return  
        self.movie.jumpToNextFrame()

    def stepFrameBackward(self):
        """Step to the previous frame in the movie."""
        if not self.movie:
            print("No movie loaded.")
            return
        current_frame = self.movie.currentFrameNumber()
        if current_frame > 0:
            self.movie.jumpToFrame(current_frame - 1)
    
    def bindFrameChangedSignal(self, functionToCall):
        if self.movie is not None:
            self.movie.frameChanged.connect(functionToCall)
