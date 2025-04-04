from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal
from Model.AcceptedFormats.Displayable import Displayable

class CompatableVideo(Displayable):
    #frameChanged = pyqtSignal(QPixmap)
    def __init__(self, sourceName):
        super().__init__(sourceName)
        self.movie = None

    def setFrame(self, frame: int):
        """Sets the video to a specific frame (to be implemented by subclasses)."""
        raise NotImplementedError("setFrame() must be implemented by the subclass.")

    def getPixmap(self) -> QPixmap | None:
        """Returns a pixmap of the current frame (to be implemented by subclasses)."""
        raise NotImplementedError("getPixmap() must be implemented by the subclass.")

    def getTotalFrames(self) -> int:
        """Returns the total number of frames in the video (to be implemented by subclasses)."""
        raise NotImplementedError("getTotalFrames() must be implemented by the subclass.")

    def setMovie(self, moviePath: str) -> bool:
        """Sets the video file to play (to be implemented by subclasses)."""
        raise NotImplementedError("setMovie() must be implemented by the subclass.")

    def startMovie(self):
        """Starts the video playback (to be implemented by subclasses)."""
        raise NotImplementedError("startMovie() must be implemented by the subclass.")

    def stopMovie(self):
        """Stops the video playback (to be implemented by subclasses)."""
        raise NotImplementedError("stopMovie() must be implemented by the subclass.")

    def stepFrameForward(self):
        """Steps to the next frame (to be implemented by subclasses)."""
        raise NotImplementedError("stepFrameForward() must be implemented by the subclass.")

    def stepFrameBackward(self):
        """Steps to the previous frame (to be implemented by subclasses)."""
        raise NotImplementedError("stepFrameBackward() must be implemented by the subclass.")

    def bindFrameChangedSignal(self, functionToCall):
        """binds a function to run when the frame changes. Essential for live annotation drawing during video playback. Probably janky though"""
        raise NotImplementedError("bindFrameChangedSignal() must be implemented by the subclass.")