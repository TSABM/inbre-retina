'''
The QGraphics Scene that all drawing takes place
'''
# pylint: disable = no-name-in-module
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QPainter, QColor, QPolygonF
from PyQt5.QtCore import QPointF, Qt
from Model.LabelData import LabelData
from Model.AcceptedFormats.Displayable import Displayable
from Model.AcceptedFormats.CompatableVideo import CompatableVideo
from Model.masterMemory import MasterMemory
from Model.Frame import Frame
from Model.Annotation import Annotation

## temporary default values ##
defaultWidth = 400
defaultHeight = 200
cornerSize = 8


class CanvasModel():
    colors = {
    "Red": QColor(255, 0, 0),
    "Green": QColor(0, 255, 0),
    "Blue": QColor(0, 0, 255),
    "Yellow": QColor(255, 255, 0),
    "Brown": QColor(165, 42, 42),
    "Purple": QColor(128, 0, 128),
    "Orange": QColor(255, 165, 0),
    "Pink": QColor(255, 192, 203),
    "Cyan": QColor(0, 255, 255),
    "Magenta": QColor(255, 0, 255),
    "Black": QColor(0, 0, 0),
    "White": QColor(255, 255, 255),
    }
    '''
    a canvas which renders a static image and accepts labels
    '''
    def __init__(self):
        self.sourceToDisplay : Displayable | None = None
        self.scene : QGraphicsScene = QGraphicsScene()
        self.pixmap : QPixmap | None = None
        self.pixmap_item = QGraphicsPixmapItem(self.pixmap)

        #self.frameNumber = 0 #FIXME
        self.currentFrame : Frame | None = None
        self.bindFrameChangedSignal()

        self.selectedItem : Annotation | None = None
        self.resizing = False
        self.resizecorner = None
        
        self.cellColorMap = {} #a dict with the cell type as the key and the color as the value
        self.scene.setBackgroundBrush(QColor(200, 200, 200)) #drawing background to a light gray to indicate the end of the drawable canavs
        self.updatePixmap()
        self.scene.addItem(self.pixmap_item)
    
    ### necissary methods, sort of miscallanious though
    def mapCellToColor(self, cellTypeToBind, color):
        self.cellColorMap.update({cellTypeToBind : color})
        self.updatePixmap()

    def getColors(self):
        return self.colors

    def loadNewProject(self, source : Displayable, projectName : str, projectID : int | None): #FIXME label data is defined here but the way wont work with the folders of images we intent to switch to
        '''
        If the source is type Displayable set it as the file to display and update the pixmap else print a message and return
        '''
        if isinstance(source, Displayable):
            totalFrames : int | None = source.getTotalFrames()
            #if isinstance(source, SimpleMovie):
            #    totalFrames = source.getTotalFrames()
            if totalFrames == None:
                print("error total frames was None")
                return
            sourceName = source.getSourceName()
            if sourceName == None:
                print("image source name was not found")
                return
            labelData : LabelData = LabelData(sourceName, totalFrames, projectName, projectID)
            MasterMemory.setLabelData(labelData)

            self.primeCanvas(source)
        else: 
            print("Canvas received a non displayable filetype")
            return

    def getScene(self):
        return self.scene
    
    def isFileOpen(self):
        '''
        returns True if label data is not None, False otherwise.
        '''
        if MasterMemory.getLabelData() == None:
            print("No file open")
            return False
        else:
            return True
    
    def primeCanvas(self, source : Displayable):
        if self.__setSource__(source):
            labelData : LabelData | None = MasterMemory.getLabelData()
            if type(labelData) is LabelData: 
                self.currentFrame = labelData.getFrame(0)

                print("image file set, attempting to refresh")
                self.updatePixmap()
            else:    
                print("cant prime canvas no valid labelData loaded")
                return
        else:
            print("cant prime canvas, source is inavlid type")

    def __setSource__(self, source :Displayable):
        if isinstance(source, Displayable):
            self.sourceToDisplay = source
            self.bindFrameChangedSignal()
            return True
        else:
            print("cant load source, not an instance of displayable")
            return False

    def bindFrameChangedSignal(self):
        if isinstance(self.sourceToDisplay, CompatableVideo):
            movie = self.sourceToDisplay.movie
            if movie is not None:
                # Connect the frameChanged signal
                self.sourceToDisplay.bindFrameChangedSignal(self.setCurrFrameLabelData)

    
    ### handle pixmap 
    def __setPixmap__(self):
        '''
        If there is a file to display get the pixmap at the current frame number
        '''
        if self.sourceToDisplay != None:
            print("trying to set pixmap")
            if self.currentFrame == None:
                print("error cant set pixmap no current frame set")
                return
            if isinstance(self.sourceToDisplay, CompatableVideo):
                self.sourceToDisplay.setFrame(self.currentFrame.getFrameNumber()) #IS this the func that sets current frame?
            self.pixmap = self.sourceToDisplay.getPixmap()
            self.pixmap_item.setPixmap(self.pixmap)

    def __drawLabels__(self, painter : QPainter):
        '''
        requests a list of the bounding boxes for the current frame, then renders each one of them (red if not selected, blue if it is)
        '''
        painter.setPen(self.colors["Orange"]) #default color
        if self.currentFrame is None:
            print("Tried to draw labels, but cannot find requested frame")
            return

        annotations = self.currentFrame.getFrameAnnotations()
        
        if not annotations:
            print(f"Frame {self.currentFrame.getFrameNumber()} has no associated annotations")
            return

        for annotation in annotations.values():
            cellType = annotation.get_cellType()
            mappedColor = self.cellColorMap.get(cellType)
            if mappedColor != None:
                painter.setPen(mappedColor)

            mask = annotation.getMask()
            if len(mask) < 3:
                print("Less than 3 points in mask, aborting draw")
                continue

            # Convert mask to a QPolygonF for efficient rendering
            polygon = QPolygonF([QPointF(x, y) for x, y in mask])
            
            # Draw polygon
            painter.drawPolygon(polygon)

        self.pixmap_item.setPixmap(self.pixmap)
    
    def updatePixmap(self):
        '''
        if there isnt a defined pixmap call setPixmap else init a QPainter and then call drawLabels
        '''
        print("updating canvas")
        if self.isFileOpen() == False:
            print("file not opened aborting pixmap update")
            return
        self.__setPixmap__()
        if self.pixmap != None:
            painter = QPainter(self.pixmap)
            if painter.isActive():
                self.__drawLabels__(painter)
            else:
                print("error: painter could not initalize. The pixmap: ", self.pixmap, " did not work")
                return
        else:
            print("pixmap == None, aborting update")
            return
    
    
    ### navigate videos:
    def playMovie(self):
        if isinstance(self.sourceToDisplay, CompatableVideo):
            self.sourceToDisplay.startMovie()

    def pauseMovie(self):
        if isinstance(self.sourceToDisplay, CompatableVideo):
            self.sourceToDisplay.stopMovie()

    def stepForward(self):
        if isinstance(self.sourceToDisplay, CompatableVideo):
            self.sourceToDisplay.stepFrameForward()
            if self.currentFrame != None:
                print(self.currentFrame.getFrameID())

    def stepBackward(self):
        if isinstance(self.sourceToDisplay, CompatableVideo):
            self.sourceToDisplay.stepFrameBackward()

    def jumpToFrame(self, frameNumber):
        if isinstance(self.sourceToDisplay, CompatableVideo):
            self.sourceToDisplay.setFrame(frameNumber)

    def setCurrFrameLabelData(self, frame_number : int): #fixme make this trigger on each video frame change
        labelData : LabelData | None = MasterMemory.getLabelData()
        if isinstance(labelData, LabelData):
            self.currentFrame = labelData.getFrame(frame_number)
            self.updatePixmap() #double check this...
        pass

    


    ### Handle everything related to the cell annotations ##
    def addAnnotation(self, maskPoints, cellType, cellId = None):  
        '''
        takes a Qrect and creates a new bounding box instance, then sends that box to label data to be recorded, then updates the canvas
        '''
        print("attempting to create new box object and add it to label data")
        if self.isFileOpen() == False:
            print("file is not open, aborting add box operation")
            return  
        if self.currentFrame == None:
            print("current frame not set, aborting addBox")
            return 
        
        #imageSource : str = self.currentFrame.getImageSource() #fixme get the image source name
        labelData : LabelData = MasterMemory.getLabelData() # type: ignore
        annotationId = labelData.getNewAnnotationID()
        frameNumber = self.currentFrame.getFrameNumber()
        #dims = rect.getRect()
        if cellId == None:
            cellId = labelData.get

        #self.__sendBoxUpdate__(boxId, frameNumber, dims[0], dims[1], dims[2], dims[3])
        self.__sendAnnotationUpdate__(annotationId, frameNumber, cellId, cellType, maskPoints)

        self.updatePixmap()
        return annotationId
       
    def __sendAnnotationUpdate__(self, annotationID, frameNumber, cellId, cellType, maskPoints):
        labelData : LabelData = MasterMemory.getLabelData() # type: ignore
        labelData.updateFrameWithAnnotation(annotationID, frameNumber, cellId, cellType, maskPoints)
    
    def __sendBoxDeleteRequest__(self, boxIdToDelete : int, frameKey : int):
        labelData : LabelData = MasterMemory.getLabelData() # type: ignore
        labelData.deleteAnnotation(boxIdToDelete, frameKey)

    def selectAnnotation(self, point): #FIXME return a list of all annotations the point could choose so the user can pick from overlapping annotations
        if self.isFileOpen() == False:
            print("no file is open, cannot select box")
            return
        #labelData : LabelData = MasterMemory.getLabelData() # type: ignore
        #frame : Frame | None = labelData.getFrame(self.frameNumber) #FIXME?
        if self.currentFrame == None:
            print("unable to select box, no current frame selected")
            return None
        annotations : dict[int, Annotation] = self.currentFrame.getFrameAnnotations()
        if annotations == {}:
            print("tried to select a box but frame ", self.currentFrame.getFrameNumber(), " annotations contianer is empty?")
            return None
        for annotation in annotations.values():
            shape : list = annotation.getMask()
            if self.is_point_inside_polygon(point, shape):
                print("selected a valid annotation")
                return annotation
        print("no box selected")
        self.deselectBox()
        return None
    
    def deselectBox(self):
        self.selectedItem = None
        self.updatePixmap()

    def is_point_inside_polygon(self, point, polygon_points):
        """
        Check if a given point (x, y) is inside a polygon.
        
        :param point: Tuple (x, y) of the test point
        :param polygon_points: List of (x, y) tuples representing the polygon
        :return: True if inside, False otherwise
        """
        polygon = QPolygonF([QPointF(x, y) for x, y in polygon_points])

        if polygon.isClosed() == False:
            print("tried to draw annotation mask but the polygon wasnt closed")
            return False

        test_point = QPointF(*point)
        
        return polygon.containsPoint(test_point, Qt.FillRule.OddEvenFill)  # Uses the even-odd rule