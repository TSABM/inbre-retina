import cv2
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl
from Model.AcceptedFormats.Displayable import Displayable

class SimpleMovie(Displayable):
    '''
    Class that accepts MP4 and similar video formats with precise frame control using OpenCV
    '''
    def __init__(self, fileName: str):
        super().__init__(fileName)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget()
        self.label = QLabel()  # For displaying individual frames
        
        layout = QVBoxLayout()
        layout.addWidget(self.videoWidget)
        layout.addWidget(self.label)  # Optional: Add QLabel to show extracted frames

        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.cap = None  # OpenCV VideoCapture object
        self.total_frames = 0
        self.fps = 30  # Default FPS, will update later

    def setMovie(self, moviePath: str) -> bool:
        '''Loads the video file for both playback and OpenCV frame extraction.'''
        if moviePath:
            self.mediaPlayer.setMedia(QUrl.fromLocalFile(moviePath))
            self.cap = cv2.VideoCapture(moviePath)
            
            if not self.cap.isOpened():
                print("Failed to open video file.")
                return False
            
            self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
            self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            print(f"Movie set | FPS: {self.fps} | Total Frames: {self.total_frames}")
            return True
        print("Invalid movie path")
        return False

    def startMovie(self):
        if self.mediaPlayer.mediaStatus() == QMediaPlayer.NoMedia:
            print("No media loaded")
            return
        self.mediaPlayer.play()

    def stopMovie(self):
        self.mediaPlayer.stop()

    def setFrame(self, frame: int):
        '''Sets the video position to a specific frame using OpenCV.'''
        if self.cap is None:
            print("Video not loaded.")
            return
        
        if frame < 0 or frame >= self.total_frames:
            print("Invalid frame number.")
            return

        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
        success, frame_data = self.cap.read()
        
        if success:
            pixmap = self.convertFrameToPixmap(frame_data)
            self.label.setPixmap(pixmap)  # Display frame in QLabel
        else:
            print("Failed to retrieve frame.")

    def getPixmap(self) -> QPixmap | None:
        '''Returns a pixmap of the current video frame using OpenCV.'''
        if self.cap is None:
            print("Video not loaded.")
            return None
        
        success, frame_data = self.cap.read()
        if success:
            return self.convertFrameToPixmap(frame_data)
        else:
            print("Failed to get frame.")
            return None

    def getTotalFrames(self) -> int:
        '''Returns the exact total number of frames in the video.'''
        return self.total_frames

    def convertFrameToPixmap(self, frame) -> QPixmap:
        '''Converts an OpenCV frame (NumPy array) to a QPixmap.'''
        height, width, channels = frame.shape
        bytes_per_line = channels * width
        q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        return QPixmap.fromImage(q_image)

    
    def bindFrameChangedSignal(self, functionToCall):
        if self.movie is not None:
            #FIXME bind a signal to trigger this function