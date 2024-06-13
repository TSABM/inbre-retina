'''
A class that facilitates "drawing" QGraphicsItems onto a canvas. Needs to detect interaction such as clicking, dragging, erasing, etc.
'''

from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtGui import QPixmap, QPen, QColor, QPainterPath
from PyQt5.QtCore import Qt, QRectF

class Marker():

    #Temp values
    pen = QPen()

    def __init__(self):
        self.pen = QPen(Qt.red, 0) #FIXME color shouldnt default to red
    
    #setters and getters
    def setColor(self, newColor):
        self.color = newColor
    
    def setOpacity(self, newOpacity):
        self.opacity = newOpacity
    
    def setSize(self, newSize):
        self.size = newSize

    def getColor(self):
        return self.color

    def getOpacity(self):
        return self.opacity
    
    def getSize(self):
        return self.size