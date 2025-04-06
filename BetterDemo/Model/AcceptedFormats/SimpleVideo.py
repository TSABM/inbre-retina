from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import pyqtSignal, QTimer
from moviepy import VideoFileClip
from Model.AcceptedFormats.CompatableVideo import CompatableVideo
#import numpy as np

class SimpleVideo(CompatableVideo):
    frameChanged = pyqtSignal(int)
    def __init__(self, fileName: str):
        super().__init__(fileName)
        #self.video: VideoFileClip | None = None
        self.frame_rate: float = 24.0 #default val, gets set when video is set
        self._current_frame_index = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self._advanceFrame)

    def setMovie(self, moviePath: str) -> bool:
        try:
            self.movie = VideoFileClip(moviePath)
            self.frame_rate = self.movie.fps
            self._current_frame_index = 0
            return True
        except Exception as e:
            print(f"Failed to load movie: {e}")
            return False

    def getTotalFrames(self) -> int:
        if not self.movie:
            return 0
        return int(self.movie.duration * self.movie.fps)

    def getPixmap(self) -> QPixmap | None:
        if not self.movie:
            return None
        return self._get_frame_pixmap(self._current_frame_index)

    def setFrame(self, frame: int):
        if not self.movie:
            return
        if self._current_frame_index == frame:
            return #in the event the frame we want to set is already the frame we are at return so no signal is sent
        self._current_frame_index = frame
        pixmap = self._get_frame_pixmap(frame)
        if pixmap:
            self.frameChanged.emit(self._current_frame_index)

    def stepFrameForward(self):
        if not self.movie:
            print("cannot step frame forward, video format is falsey")
            return
        if self._current_frame_index < self.getTotalFrames() - 1:
            self._current_frame_index += 1
            pixmap = self._get_frame_pixmap(self._current_frame_index)
            if pixmap:
                self.frameChanged.emit(self._current_frame_index)

    def stepFrameBackward(self):
        if not self.movie:
            return
        if self._current_frame_index > 0:
            self._current_frame_index -= 1
            pixmap = self._get_frame_pixmap(self._current_frame_index)
            if pixmap:
                self.frameChanged.emit(self._current_frame_index)
        else:
            print("cannot step back to prevent negative frame traversal")

    def startMovie(self):
        if not self.movie:
            return
        interval_ms = int(1000 / self.frame_rate)
        self.timer.start(interval_ms)

    def stopMovie(self):
        self.timer.stop()

    def _advanceFrame(self):
        if self._current_frame_index >= self.getTotalFrames() - 1:
            self.stopMovie()
            return
        self._current_frame_index += 1
        pixmap = self._get_frame_pixmap(self._current_frame_index)
        if pixmap:
            self.frameChanged.emit(self._current_frame_index)

    def bindFrameChangedSignal(self, functionToCall):
        self.frameChanged.connect(functionToCall)

    def _get_frame_pixmap(self, frame_index: int) -> QPixmap | None:
        if not self.movie:
            return None
        try:
            t = frame_index / self.frame_rate
            frame = self.movie.get_frame(t)  # Returns a (H, W, 3) or (H, W, 4) ndarray
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            return QPixmap.fromImage(image.rgbSwapped())  # MoviePy gives RGB, Qt expects BGR
        except Exception as e:
            print(f"Error retrieving frame {frame_index}: {e}")
            return None
