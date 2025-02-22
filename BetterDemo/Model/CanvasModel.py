'''
The QGraphics Scene that all drawing takes place
'''
# pylint: disable = no-name-in-module
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage, QColor
from PyQt5.QtCore import QRectF, QPoint, Qt, QSize
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
    
    ### handle pixmap 
    def setSource(self, source : Displayable, projectName : str, projectID : int | None): #FIXME label data is defined here but the way wont work with the folders of images we intent to switch to
        '''
        If the source is type Displayable set it as the file to display and update the pixmap else print a message and return
        '''
        if isinstance(source, Displayable):
            self.sourceToDisplay = source
            totalFrames : int | None = source.getTotalFrames()
            if isinstance(source, SimpleMovie):
                totalFrames = source.getTotalFrames()
            if totalFrames == None:
                print("error total frames was None")
                return
            sourceName = source.getSourceName()
            if sourceName == None:
                print("image source name was not found")
                return
            labelData : LabelData = LabelData(sourceName, totalFrames, projectName, projectID)
            MasterMemory.setLabelData(labelData)
            #labelData : LabelData | None = MasterMemory.getLabelData()
            self.currentFrame = labelData.getFrame(0) #FIXME? setting to 0th frame since both images and videos have one.

            print("image file set, attempting to refresh")
            self.updatePixmap()
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
        labelData : LabelData = MasterMemory.getLabelData() # type: ignore
        #frame : Frame | None = labelData.getFrame(self.frameNumber)
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
                    if(self.__verifyAnnotationType(annotation, "Box")):
                        rectangle : QRectF = self.__convertCornersToQRect__(annotation.getMask())
                        if annotation == self.selectedItem:
                            painter.setPen(QPen(QColor(0, 0, 255), 2))  # Blue pen for selected rectangle
                            painter.drawRect(rectangle)
                            self.__drawResizeHandles__(painter, rectangle)
                            painter.setPen(QColor(255, 0, 0)) #set painter color back to red for the non selected labels
                        #else render it like normal
                        else:
                            painter.drawRect(rectangle)
                    elif(self.__verifyAnnotationType(annotation, "Contour")):
                        print("contour drawing is not implemented")
                    else:
                        print("error annotation type was neither box nor contour cannot draw it")
                    
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
    def addAnnotation(self, maskPoints, annotationType : str, cellType, cellId = None):  
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
        
        imageSource : str = self.currentFrame.getImageSource() #fixme get the image source name
        labelData : LabelData = MasterMemory.getLabelData() # type: ignore
        annotationId = labelData.getNewAnnotationID()
        frameNumber = self.currentFrame.getFrameNumber()
        #dims = rect.getRect()
        if cellId == None:
            cellId = labelData.get

        #self.__sendBoxUpdate__(boxId, frameNumber, dims[0], dims[1], dims[2], dims[3])
        self.__sendAnnotationUpdate__(annotationId, annotationType, frameNumber, cellId, cellType, maskPoints, imageSource)

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
    
    def __sendAnnotationUpdate__(self, annotationID, annotationType, frameNumber, cellId, cellType, maskPoints, imageSource):
        labelData : LabelData = MasterMemory.getLabelData() # type: ignore
        labelData.updateFrameWithAnnotation(annotationID, annotationType, frameNumber, cellId, cellType, maskPoints, imageSource)
    
    def __sendBoxDeleteRequest__(self, boxIdToDelete : int, frameKey : int):
        labelData : LabelData = MasterMemory.getLabelData() # type: ignore
        labelData.deleteAnnotation(boxIdToDelete, frameKey)

    def __updateSelectedBoxPosition__(self, rectangle : QRectF):
        if self.selectedItem == None:
            print("No item selected aborting position update")
            return
        topCorner : QPoint = rectangle.topRight()
        bottomCorner : QPoint = rectangle.bottomLeft()
        boxMask = [[topCorner.x(), topCorner.y()],[bottomCorner.x(), bottomCorner.y()]]

        self.selectedItem.setMask(boxMask)

    def selectBox(self, point):
        if self.isFileOpen() == False:
            print("no file is open, cannot select box")
            return
        
        labelData : LabelData = MasterMemory.getLabelData() # type: ignore
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
            
            if annotation.getAnnotationType() == "Box":
                rectangle = QRectF(*shape[0], *shape[1]) 
                if rectangle == None:
                    print("ERROR: no rectangle assigned to this label")
                    pass
                elif rectangle.contains(point):
                    print("box selected")
                    self.selectedItem = annotation
                    self.updatePixmap()
                    return self.selectedItem
                else:
                    pass
        print("no box selected")
        self.deselectBox()
        return None
    
    def deselectBox(self):
        self.selectedItem = None
        self.updatePixmap()
    
    def moveBox(self, point : QPoint):
        if self.isFileOpen() == False:
            return
        if self.selectedItem == None:
            print("cannot move annotation because the selected annotation is None")
            return
        if self.selectedItem.getAnnotationType() == 'Box':
            maskPoints = self.selectedItem.getMask()
            rectangle : QRectF | None = self.__convertCornersToQRect__(maskPoints)
            if rectangle == None:
                print("warning moving box failed. Failed to define rectangle")
                return
            rectangle.moveCenter(point)
            self.__updateSelectedBoxPosition__(rectangle)
            self.updatePixmap()
        elif self.selectedItem.getAnnotationType() == 'Contour':
            print("contour movement is not yet implemented")
        else:
            print("annotation type is not recognized: ", self.selectedItem.getAnnotationType())

    ### methods on box resizing
    def resizeBox(self, point, corner): 
        if self.isFileOpen() == False:
            return
        if self.selectedItem == None:
            print("cannot resize box. Box is None")
            return
        #grab curr coords as a rectangle
        rectangle : QRectF = self.__convertCornersToQRect__(self.selectedItem.getMask()) #fixme this is inefficient passing data back and forth, theres got to be a better way 
        if rectangle == None:
            print("failed to convert qrect in resize")
            return
        #transform 
        if corner == 0:  # Top-left
            rectangle.setTopLeft(point)
        elif corner == 1:  # Top-right
            rectangle.setTopRight(point)
        elif corner == 2:  # Bottom-left
            rectangle.setBottomLeft(point)
        elif corner == 3:  # Bottom-right
            rectangle.setBottomRight(point)
        #update master
        self.__updateSelectedBoxPosition__(rectangle)
        #self.sendBoxUpdate()#this is maybe unneeded the line above may update label data if it just copies by ref...
        self.updatePixmap()
        
    def __drawResizeHandles__(self, painter : QPainter, rectangle):
        handles = self.__getResizeHandles__(rectangle)
        painter.setBrush(QColor(0, 0, 255)) #blue handle fill
        #draw each handle
        for handle in handles:
            painter.drawRect(handle)
        #remove blue fill for future rectangles
        painter.setBrush(Qt.NoBrush) # type: ignore

    def __getResizeHandles__(self, rect : QRectF):
        return [
            QRectF(rect.topLeft() - QPoint(cornerSize//2, cornerSize//2), QSize(cornerSize, cornerSize)),
            QRectF(rect.topRight() - QPoint(cornerSize//2, cornerSize//2), QSize(cornerSize, cornerSize)),
            QRectF(rect.bottomLeft() - QPoint(cornerSize//2, cornerSize//2), QSize(cornerSize, cornerSize)),
            QRectF(rect.bottomRight() - QPoint(cornerSize//2, cornerSize//2), QSize(cornerSize, cornerSize))
        ]

    def selectResizeCorner(self, point):
        if self.isFileOpen() == False:
            return
        if self.selectedItem == None:
            print("corner cannot be selected: no annotation marked as selected")
            return None
        if self.selectedItem.getAnnotationType() == "Box":
            handles = self.__getResizeHandles__(self.__convertCornersToQRect__(self.selectedItem.getMask()))
            for index in range(len(handles)):
                if handles[index].contains(point):
                    return index
    
    def __verifyAnnotationType(self, annotation : Annotation, expectedType : str) -> bool:
        type = annotation.getAnnotationType()
        if type == expectedType:
            return True
        else:
            return False

    def __convertCornersToQRect__(self, corners) -> QRectF:
        rect = QRectF(*corners[0], *corners[1])
        return rect