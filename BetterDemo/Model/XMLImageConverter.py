class XMLToImage():
    '''
    convert an xml file holding image data to an image
    '''
    def __init__(self, xmlImageData):
        self.xmlData = xmlImageData
        self.renderableImage = self.convertXMLToImage()
        pass

    def loadImageFromXML(self, xmlFilePath):
        print("converting xml to image is not implemented")
    
    def loadImageFromJSON(self, jsonFilePath):
        print("loading image from json is unimplemented")