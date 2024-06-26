
class OpenScenes():
    sceneContainer = []
    def __init__(self):
        pass

    def setSceneContainer(self, newSceneContainer):
        self.sceneContainer = newSceneContainer

    def getAllScenes(self):
        return self.sceneContainer

    def addScene(self, sceneToAdd):
        self.sceneContainer.append(sceneToAdd)

    def getSceneByIndex(self, index):
        return self.sceneContainer[index]
    
    def updateExistingScene(self, index, sceneToUpdate):
        self.sceneContainer[index] = sceneToUpdate