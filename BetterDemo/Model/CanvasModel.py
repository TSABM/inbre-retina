'''
The QGraphics Scene that all drawing takes place
'''
# pylint: disable = no-name-in-module
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage, QColor
from PyQt5.QtCore import QRect, QPoint, Qt, QSize
from Model.LabelData import LabelData, Annotation, Frame
from Model.AcceptedFormats.Displayable import Displayable
from Model.AcceptedFormats.SimpleMovie import SimpleMovie
from Model.masterMemory import MasterMemory

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

        self.frameNumber = 0 #FIXME
        
        self.pixmap : QPixmap | None = None
        #FIXME need to make compatable with videos (gif videos)
        #self.pixmap = QPixmap(defaultWidth, defaultHeight)
        self.pixmap_item = QGraphicsPixmapItem(self.pixmap)

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
    
    def __getFrameNumber__(self):
        '''returns the current frames number'''
        return self.frameNumber
    
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
            MasterMemory.setLabelData(LabelData(sourceName, totalFrames, projectName, projectID))

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
            if isinstance(self.sourceToDisplay, SimpleMovie):
                self.sourceToDisplay.setFrame(self.frameNumber)
            self.pixmap = self.sourceToDisplay.getPixmap()
            self.pixmap_item.setPixmap(self.pixmap)

    def __drawLabels__(self, painter : QPainter):
        '''
        requests a list of the bounding boxes for the current frame, then renders each one of them (red if not selected, blue if it is)
        '''
        labelData : LabelData = MasterMemory.getLabelData() # type: ignore
        #boundingBoxes : dict = labelData.get("BoundingBoxes") #FIXME ? will this work?
        #boxIds = MasterMemory.getAllBoxIDsForAFrame(MasterMemory.getCurrentFrameNumber())
        frame : Frame | None = labelData.getFrame(self.frameNumber)
        if frame == None:
            print("Tried to draw labels, cannot find requested frame")
        else:
            boxes : dict = frame.getFrameAnnotations()
            boxIds = boxes.keys()
            if boxIds.__len__ == 0:
                print("Frame ", self.frameNumber, " has no assotiated bounding boxes")
            else:
                for boxId in boxIds:
                    #if its selected render it blue and with handles
                    box : Annotation = boxes[boxId]
                    rectangle : QRect = box.get_boundingBox_as_qrect()
                    if box == self.selectedItem:
                        painter.setPen(QPen(QColor(0, 0, 255), 2))  # Blue pen for selected rectangle
                        painter.drawRect(rectangle)
                        self.__drawResizeHandles__(painter, rectangle)
                        painter.setPen(QColor(255, 0, 0)) #set painter color back to red for the non selected labels
                    #else render it like normal
                    else:
                        painter.drawRect(rectangle)
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
    def addBox(self, rect : QRect):  
        '''
        takes a Qrect and creates a new bounding box instance, then sends that box to label data to be recorded, then updates the canvas
        '''
        print("attempting to create new box object and add it to label data")
        if self.isFileOpen() == False:
            print("file is not open, aborting add box operation")
            return  
        
        labelData : LabelData = MasterMemory.getLabelData() # type: ignore
        boxId = labelData.getNewBoxID()
        frameNumber = self.__getFrameNumber__()
        dims = rect.getRect()

        self.__sendBoxUpdate__(boxId, frameNumber, dims[0], dims[1], dims[2], dims[3])

        self.updatePixmap()
        return boxId
    
    
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
    
    def __sendBoxUpdate__(self, boxId, frameNumber, x, y, w, h):
        labelData : LabelData = MasterMemory.getLabelData() # type: ignore
        labelData.updateFrameWithAnnotation(boxId, frameNumber, x, y, w, h)
    
    def __sendBoxDeleteRequest__(self, boxIdToDelete : int, frameKey : int):
        labelData : LabelData = MasterMemory.getLabelData() # type: ignore
        labelData.deleteAnnotation(boxIdToDelete, frameKey)

    def __updateSelectedBoxPosition__(self, rectangle : QRect):
        if self.selectedItem == None:
            print("No item selected aborting position update")
            return
        topCorner : QPoint = rectangle.topRight()
        bottomCorner : QPoint = rectangle.bottomLeft()
        boxMask = [[topCorner.x(), topCorner.y()],[bottomCorner.x(), bottomCorner.y()]]

        self.selectedItem.setMask(boxMask)

    def selectBox(self, point):
        if self.isFileOpen() == False:
            return
        
        labelData : LabelData = MasterMemory.getLabelData() # type: ignore
        #boundingBoxes : dict = labelData.get("BoundingBoxes") #FIXME
        #boxIds = MasterMemory.getAllBoxIDsForAFrame(0) #FIXME this index should update based on the frame looked at
        frame : Frame | None = labelData.getFrame(self.frameNumber) #FIXME?
        if frame == None:
            print("unable to select box, frame ", self.frameNumber, " does not exist")
            return None
        boxes : dict[int, Annotation] = frame.getFrameAnnotations()
        if boxes == {}:
            print("tried to select a box but frame ", self.frameNumber, " box contianer is empty?")
            return None
        for box in boxes.values():
            rectangle : QRect = box.get_boundingBox_as_qrect()
            if rectangle == None:
                print("ERROR: no rectangle assigned to this label")
                pass
            elif rectangle.contains(point):
                print("box selected")
                self.selectedItem = box
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
            print("cannot move box because the selected box is None")
            return
        
        rectangle : QRect | None = self.selectedItem.get_boundingBox_as_qrect()
        if rectangle == None:
            print("warning moving box failed. Failed to define rectangle")
            return
        rectangle.moveCenter(point)
        self.__updateSelectedBoxPosition__(rectangle)
        self.updatePixmap()

    ### methods on box resizing
    def resizeBox(self, point, corner): 
        if self.isFileOpen() == False:
            return
        if self.selectedItem == None:
            print("cannot resize box. Box is None")
            return
        #grab curr coords as a rectangle
        rectangle : QRect = self.selectedItem.get_boundingBox_as_qrect() #fixme this is inefficient passing data back and forth, theres got to be a better way 
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

    def __getResizeHandles__(self, rect : QRect):
        return [
            QRect(rect.topLeft() - QPoint(cornerSize//2, cornerSize//2), QSize(cornerSize, cornerSize)),
            QRect(rect.topRight() - QPoint(cornerSize//2, cornerSize//2), QSize(cornerSize, cornerSize)),
            QRect(rect.bottomLeft() - QPoint(cornerSize//2, cornerSize//2), QSize(cornerSize, cornerSize)),
            QRect(rect.bottomRight() - QPoint(cornerSize//2, cornerSize//2), QSize(cornerSize, cornerSize))
        ]

    def selectResizeCorner(self, point):
        if self.isFileOpen() == False:
            return

        #if no box is selected do nothing
        if self.selectedItem == None:
            print("corner cannot be selected: no label marked as selected")
            return None
        else:
            handles = self.__getResizeHandles__(self.selectedItem.get_boundingBox_as_qrect())
            for index in range(len(handles)):
                if handles[index].contains(point):
                    return index
    
    ### possibly deprocated methods below here. FIXME 
    def getSelectedLabel(self):
        return self.selectedItem