import os
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QDir
from Model.AcceptedFormats.Displayable import Displayable
from CompatableVideo import CompatableVideo

class ImageSequenceVideo(CompatableVideo):
    def __init__(self, directoryPath: str):
        super().__init__(directoryPath)
        self.images = []
        self.current_frame_index = 0

        # Load all images from the directory
        self.loadImagesFromDirectory(directoryPath)

    def loadImagesFromDirectory(self, directoryPath: str):
        """Load all images from the directory in sorted order."""
        if not os.path.isdir(directoryPath):
            print("Invalid directory.")
            return

        # Get all image files in the directory (considering jpg, png, etc.)
        supported_formats = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
        for file_name in sorted(os.listdir(directoryPath)):
            if any(file_name.lower().endswith(ext) for ext in supported_formats):
                file_path = os.path.join(directoryPath, file_name)
                self.images.append(file_path)

        if len(self.images) == 0:
            print("No supported image files found in the directory.")
    
    def setFrame(self, frame: int):
        """Set the current frame by index."""
        if frame < 0 or frame >= len(self.images):
            print("Invalid frame number.")
            return

        self.current_frame_index = frame

    def getPixmap(self) -> QPixmap | None:
        """Return the current frame as a QPixmap."""
        if not self.images:
            print("No images loaded.")
            return None

        # Load the image at the current frame index
        image_path = self.images[self.current_frame_index]
        pixmap = QPixmap(image_path)
        return pixmap

    def getTotalFrames(self) -> int:
        """Return the total number of frames (images) in the directory."""
        return len(self.images)

    def setMovie(self, moviePath: str) -> bool:
        """For ImageSequenceVideo, moviePath is the directory path."""
        self.loadImagesFromDirectory(moviePath)
        return len(self.images) > 0

    def startMovie(self):
        """Start the "video" playback (start from the first frame)."""
        if not self.images:
            print("No images loaded.")
            return
        self.current_frame_index = 0

    def stopMovie(self):
        """Stop the "video" playback."""
        self.current_frame_index = 0

    def stepFrameForward(self):
        """Step forward one frame (image)."""
        if self.current_frame_index < len(self.images) - 1:
            self.current_frame_index += 1
        else:
            print("Already at the last frame.")

    def stepFrameBackward(self):
        """Step backward one frame (image)."""
        if self.current_frame_index > 0:
            self.current_frame_index -= 1
        else:
            print("Already at the first frame.")
