import cv2
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer, pyqtSignal, QObject
from Model.AcceptedFormats.Displayable import Displayable
from CompatableVideo import CompatableVideo

class SimpleVideo(CompatableVideo, QObject):
    frameChanged = pyqtSignal(int)  # Signal emitted when the frame changes

    def __init__(self, fileName: str):
        super().__init__(fileName)
        QObject.__init__(self)  # Required for signals
        self.cap = None
        self.total_frames = 0
        self.fps = 30

        self.current_frame = 0
        self.current_pixmap = None  # Store last retrieved frame
        
        self.timer = QTimer()
        self.timer.timeout.connect(self._playNextFrame)  # Calls next frame when playing

    def setFrame(self, frame: int):
        """Set the frame of the video and store its image."""
        if self.cap is None or frame < 0 or frame >= self.total_frames:
            print("Invalid frame number.")
            return
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
        success, frame_data = self.cap.read()
        if success:
            self.current_frame = frame
            self.current_pixmap = self.convertFrameToPixmap(frame_data)
            self.frameChanged.emit(frame)  # Emit signal to notify UI
        else:
            print("Failed to retrieve frame.")

    def getPixmap(self) -> QPixmap | None:
        """Return the last retrieved frame as a QPixmap."""
        return self.current_pixmap  # Always return stored frame

    def getTotalFrames(self) -> int:
        """Get total frames of the video."""
        return self.total_frames

    def setMovie(self, moviePath: str) -> bool:
        """Set the video file."""
        self.cap = cv2.VideoCapture(moviePath)
        if not self.cap.isOpened():
            print("Failed to open video.")
            return False
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.setFrame(0)  # Load first frame
        return True

    def startMovie(self):
        """Start video playback."""
        if self.cap is None:
            print("No video loaded.")
            return
        self.timer.start(int(1000 / self.fps))  # Start playback based on FPS

    def stopMovie(self):
        """Stop video playback."""
        self.timer.stop()  # Stop playing

    def stepFrameForward(self):
        """Step to the next frame."""
        if self.current_frame + 1 < self.total_frames:
            self.setFrame(self.current_frame + 1)

    def stepFrameBackward(self):
        """Step to the previous frame."""
        if self.current_frame > 0:
            self.setFrame(self.current_frame - 1)

    def convertFrameToPixmap(self, frame) -> QPixmap:
        """Convert OpenCV frame to QPixmap."""
        height, width, channels = frame.shape
        bytes_per_line = channels * width
        q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        return QPixmap.fromImage(q_image)

    def _playNextFrame(self):
        """Play the next frame during playback."""
        if self.current_frame + 1 < self.total_frames:
            self.setFrame(self.current_frame + 1)
        else:
            self.stopMovie()  # Stop at the end of the video

    def bindFrameChangedSignal(self, functionToCall):
        """Bind a function to the frameChanged signal."""
        self.frameChanged.connect(functionToCall)
