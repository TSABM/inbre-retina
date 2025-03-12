'''
The QGraphics Scene that all drawing takes place
'''
# pylint: disable = no-name-in-module
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QPainter, QColor, QPolygonF
from PyQt5.QtCore import QPointF, Qt
from Model.LabelData import LabelData
from Model.AcceptedFormats.Displayable import Displayable
from Model.AcceptedFormats.SimpleMovie import SimpleMovie
from Model.masterMemory import MasterMemory
from Model.Frame import Frame
from Model.Annotation import Annotation

## temporary default values ##
defaultWidth = 400
defaultHeight = 200
cornerSize = 8


class CanvasModel():
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

        self.selectedItem : Annotation | None = None
        self.resizing = False
        self.resizecorner = None
        
        self.scene.setBackgroundBrush(QColor(200, 200, 200)) #drawing background to a light gray to indicate the end of the drawable canavs
        self.updatePixmap()
        self.scene.addItem(self.pixmap_item)
    
    ### necissary methods, sort of miscallanious though
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
    
    #def __getFrameNumber__(self):
    #    '''returns the current frames number'''
    #    return self.frameNumber

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
            return True
        else:
            print("cant load source, not an instance of displayable")
            return False

    ### handle pixmap 
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

    def __setPixmap__(self):
        '''
        If there is a file to display get the pixmap at the current frame number
        '''
        if self.sourceToDisplay != None:
            print("trying to set pixmap")
            if self.currentFrame == None:
                print("error cant set pixmap no current frame set")
                return
            if isinstance(self.sourceToDisplay, SimpleMovie):
                self.sourceToDisplay.setFrame(self.currentFrame.getFrameNumber()) #IS this the func that sets current frame?
            self.pixmap = self.sourceToDisplay.getPixmap()
            self.pixmap_item.setPixmap(self.pixmap)

    def __drawLabels__(self, painter : QPainter):
        '''
        requests a list of the bounding boxes for the current frame, then renders each one of them (red if not selected, blue if it is)
        '''
        print("attempting to draw labels")
        #labelData : LabelData = MasterMemory.getLabelData() # type: ignore
        #frame : Frame | None = labelData.getFrame(self.frameNumber)
        
        #verify frame exists
        if self.currentFrame == None:
            print("Tried to draw labels, but cannot find requested frame")
        else:
            annotations : dict = self.currentFrame.getFrameAnnotations()
            annotationIds = annotations.keys()
            #check if there are no annotations
            if annotationIds.__len__ == 0:
                print("Frame ", self.currentFrame.getFrameNumber(), " has no assotiated annotations")
            #if there are handle drawing
            else:
                for annotationId in annotationIds:
                    #if its selected render it blue and with handles
                    annotation : Annotation = annotations[annotationId]
                    mask : list = annotation.getMask()
                    if len(mask) < 3:
                        print("less than 3 points in mask, aborting draw")
                        continue
                    for i in range(len(mask)):
                        #if its the last one draw line from here back to the start
                        if i == len(mask):
                            x1, y1 = mask[i]
                            x2, y2 = mask[0]
                            painter.drawLine(x1, y1, x2, y2)
                        #otherwise draw from current line to the next one
                        else:
                            x1, y1 = mask[i]
                            x2, y2 = mask[i + 1]
                            painter.drawLine(x1, y1, x2, y2)
        painter.end()
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
                painter.setPen(QColor(255, 0, 0)) #FIXME let the user choose the color in the future, and maybe the width too.
                self.__drawLabels__(painter)
            else:
                print("error: painter could not initalize. The pixmap: ", self.pixmap, " did not work")
                return
        else:
            print("pixmap == None, aborting update")
            return
    
    ### Handle everything related to the bounding boxes ##
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
    
    
    def deleteBox(self, boxID): #FIXME I pass in boxID here but never use it, either selected item is deleted or I pass it in
        #check if a box is at the point (if so select it)
        
        #check if a box is currently selected
        if self.isFileOpen() == False:
            return  
        elif self.selectedItem == None:
            print("Unable to delete box: Canvas has no box selected")
            return
        else:
            #print("Attempting to delete selected box")
            self.__sendBoxDeleteRequest__(self.selectedItem.get_annotationID(), self.selectedItem.get_frameNumber())
            return
    
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