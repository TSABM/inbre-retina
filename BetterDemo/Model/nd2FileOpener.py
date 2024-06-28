import nd2

class nd2FileOpener():
    def __init__(self):
        pass
    
    def openNd2(self, fileToOpen):
        #nd2Array = nd2.imread(fileToOpen, xarray= True, dask= True)
        #code below will need to be altered to accept different amounts of frames
        with nd2.ND2File(fileToOpen) as myfile:
            print(myfile.metadata)
            
            tempFrame = myfile.read_frame(0)

            print("Frame shape: %f", tempFrame.shape)
        
        return None