import numpy as np
from skimage.io import imread
from skimage import restoration
from skimage import measure
from skimage.measure import regionprops
from skimage.filters import threshold_otsu
class PreProcess():
    
    def __init__(self, imageLocation):
        self.fullCarImg = imread(imageLocation, as_grey=True)
        self.binaryImage = self.threshold(self.denoise(self.fullCarImg))
        
    def denoise(sefl, imgDetails):
        return restoration.denoise_tv_chambolle(imgDetails)
        
    def threshold(self, denoisedImg):
        thresholdValue = threshold_otsu(denoisedImg)
        #plotPreProcessed(denoisedImg > thresholdValue)
        return denoisedImg > thresholdValue
        
    def getPlateLikeObjects(self):
        self.labelImage = measure.label(self.binaryImage)
        threshold = self.binaryImage
        charDimensions = (0.05*threshold.shape[0], 0.3*threshold.shape[0], 0.1*threshold.shape[1], 0.4*threshold.shape[1])
        minHeight, maxHeight, minWidth, maxWidth = charDimensions
        platelikeobjects = []
        for region in regionprops(self.labelImage):
            if region.area < 10:
                continue
        
            minimumRow, minimumCol, maximumRow, maximumCol = region.bbox
            regionHeight = maximumRow - minimumRow
            regionWidth = maximumCol - minimumCol
            if regionHeight >= minHeight and regionHeight <= maxHeight and regionWidth >= minWidth and regionWidth <= maxWidth and regionWidth >= regionHeight:
                platelikeobjects.append(self.fullCarImg[minimumRow:maximumRow, minimumCol:maximumCol])
                
        return platelikeobjects