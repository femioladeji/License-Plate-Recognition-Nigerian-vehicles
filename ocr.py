import numpy as np
from skimage.transform import resize
from skimage import measure
from skimage.measure import regionprops

class OCROnObjects():
    
    def __init__(self, plateObject):
        for eachObj in plateObject:
            totalThings = self.identifyBoundaryOnObject(eachObj)
            #the next line was just a way to clearly identify a plate number, its still a dumb idea for now
            if len(totalThings) >= 20:
                #plotPreProcessed(eachObj)
                self.getRegions(totalThings, eachObj)
        
    def identifyBoundaryOnObject(self, aNumPlate):
        labelImage = measure.label(aNumPlate)
        charDimensions = (0.4*aNumPlate.shape[0], 0.85*aNumPlate.shape[0], 0.04*aNumPlate.shape[1], 0.15*aNumPlate.shape[1])
        minHeight, maxHeight, minWidth, maxWidth = charDimensions
        regionLists = regionprops(labelImage)
        return regionLists
    
    def getRegions(self, totalThings, aNumPlate):

        cord = []
        counter=0
        colList = []
        charDimensions = (0.4*aNumPlate.shape[0], 0.85*aNumPlate.shape[0], 0.04*aNumPlate.shape[1], 0.2*aNumPlate.shape[1])
        minHeight, maxHeight, minWidth, maxWidth = charDimensions
        for regions in totalThings:
            if regions.area > 10:
                minimumRow, minimumCol, maximumRow, maximumCol = regions.bbox
                charHeight = maximumRow - minimumRow
                charWidth = maximumCol - minimumCol
                roi = aNumPlate[minimumRow:maximumRow, minimumCol:maximumCol]
                if roi.shape[0]*roi.shape[1] == 0:
                    continue
                elif charHeight < minHeight or charHeight > maxHeight or charWidth < minWidth or charWidth > maxWidth:
                    continue
                else:
                    if counter==0:
                        samples = resize(roi, (20,20))
                        cord.append(regions.bbox)
                        counter+=1
                    elif counter==1:
                        roismall = resize(roi, (20,20))
                        samples = np.concatenate((samples[None,:,:], roismall[None,:,:]), axis=0)
                        cord.append(regions.bbox)
                        counter+=1
                    else:
                        roismall = resize(roi, (20,20))
                        samples = np.concatenate((samples[:,:,:], roismall[None,:,:]), axis=0)
                        cord.append(regions.bbox)
                    colList.append(minimumCol)
        self.candidates = {
                    'fullscale': samples,
                    'coordinates': np.array(cord),
                    'columnsVal': colList
                    }
        
        return self.candidates