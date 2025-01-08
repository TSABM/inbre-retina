'''
The QGraphics Scene that all drawing takes place
'''
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage, QColor
from PyQt5.QtCore import QRect, QPoint, Qt, QSize
from Model.LabelData import LabelData, BoundingBox, Frame
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
        self.sourceToDisplay : Displayable = None
        self.scene : QGraphicsScene = QGraphicsScene()

        self.frameNumber = 0 #FIXME
        
        self.pixmap : QPixmap = None
        #FIXME need to make compatable with videos (gif videos)
        #self.pixmap = QPixmap(defaultWidth, defaultHeight)
        self.pixmap_item = QGraphicsPixmapItem(self.pixmap)

        self.selectedItem : BoundingBox = None
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
    def setSource(self, source : Displayable): #FIXME label data is defined here but the way wont work with the folders of images we intent to switch to
        '''
        If the source is type Displayable set it as the file to display and update the pixmap else print a message and return
        '''
        if isinstance(source, Displayable):
            self.sourceToDisplay = source
            #FIXME probably should create LabelData here not elsehwere.
            totalFrames : int = 0
            if isinstance(source, SimpleMovie):
                totalFrames = source.getTotalFrames()
            MasterMemory.setLabelData(LabelData(source.getSourceName(), totalFrames))

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
        labelData : LabelData = MasterMemory.getLabelData()
        #boundingBoxes : dict = labelData.get("BoundingBoxes") #FIXME ? will this work?
        #boxIds = MasterMemory.getAllBoxIDsForAFrame(MasterMemory.getCurrentFrameNumber())
        frame : Frame = labelData.getFrame(self.frameNumber)
        if frame == None:
            print("cannot find requested frame")
        else:
            boxes : dict = frame.getBoundingBoxes()
            boxIds = boxes.keys()
            if boxIds.__len__ == 0:
                print("Frame ", self.frameNumber, " has no assotiated bounding boxes")
            else:
                for boxId in boxIds:
                    #if its selected render it blue and with handles
                    box : BoundingBox = boxes.get(boxId)
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
        
        labelData : LabelData = MasterMemory.getLabelData()
        boxId = labelData.getNewBoxID()
        frameNumber = self.__getFrameNumber__()
        dims = rect.getRect()

        self.__sendBoxUpdate__(boxId, frameNumber, dims[0], dims[1], dims[2], dims[3])

        self.updatePixmap()
        return boxId
    
    def selectAndDelete(self, point):
        #handle selection
        clickedBox = self.selectBox()
        if clickedBox == None:
            print("could not delete, no box found at clicked location")
            return
        #handle deletion
        #FIXME
        self.deleteBox()
        self.deselectBox()
    
    def deleteBox(self, boxID):
        #check if a box is at the point (if so select it)
        
        #check if a box is currently selected
        if self.isFileOpen() == False:
            return  
        elif self.selectedItem == None:
            print("Unable to delete box: Canvas has no box selected")
            return
        else:
            #print("Attempting to delete selected box")
            self.__sendBoxDeleteRequest__(self.selectedItem.get_boxID())
            return
    
    def __sendBoxUpdate__(self, boxId, frameNumber, x, y, w, h):
        labelData : LabelData = MasterMemory.getLabelData()
        labelData.updateBoundingBox(boxId, frameNumber, x, y, w, h)
    
    def __sendBoxDeleteRequest__(self, boxIdToDelete : str):
        labelData : LabelData = MasterMemory.getLabelData()
        labelData.deleteBoundingBox(boxIdToDelete)

    def __updateSelectedBoxPosition__(self, rectangle : QRect):
        dims = rectangle.getRect()
        self.selectedItem.setDimensions(dims[0], dims[1], dims[2], dims[3])

    def selectBox(self, point):
        if self.isFileOpen() == False:
            return
        
        labelData : LabelData = MasterMemory.getLabelData()
        #boundingBoxes : dict = labelData.get("BoundingBoxes") #FIXME
        #boxIds = MasterMemory.getAllBoxIDsForAFrame(0) #FIXME this index should update based on the frame looked at
        frame : Frame = labelData.getFrame(self.frameNumber) #FIXME?
        if frame == None:
            print("unable to select box, frame ", self.frameNumber, " does not exist")
            return None
        boxes : dict[BoundingBox] = frame.getBoundingBoxes()
        if boxes == {}:
            print("tried to select a box but frame ", self.frameNumber, " box contianer is empty?")
            return None
        for box in boxes:
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
    
    def moveBox(self, point):
        if self.isFileOpen() == False:
            return
        
        rectangle : QRect = self.selectedItem.get_boundingBox_as_qrect()
        rectangle.moveCenter(point)
        self.__updateSelectedBoxPosition__(rectangle)
        self.updatePixmap()

    ### methods on box resizing
    def resizeBox(self, point, corner): 
        if self.isFileOpen() == False:
            return
        
        #grab curr coords as a rectangle
        rectangle : QRect = self.selectedItem.get_boundingBox_as_qrect() #fixme this is inefficient passing data back and forth, theres got to be a better way 
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
        painter.setBrush(Qt.NoBrush)

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