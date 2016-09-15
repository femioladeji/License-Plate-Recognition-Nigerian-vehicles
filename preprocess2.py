import numpy as np
from skimage.io import imread
from skimage.filter import threshold_otsu
from skimage.transform import resize
from matplotlib import pyplot as plt
from skimage.morphology import closing, square
from matplotlib import pyplot as plt
from skimage.measure import regionprops
from skimage import restoration
from skimage import measure
from skimage.color import label2rgb
import matplotlib.patches as mpatches

class PreProcess:
    
    def __init__(self, imgLocation):
        self.imageObj = 'x'
        return self.imageObj
        #writeImageToFile(self.imageObj, 'image')
        #thresholdCalc(histogramGeneration(self.imageObj), len(self.imageObj)*len(self.imageObj[0]))
        #self.denoiseImage()
        #self.thresholdImage()
        #self.threshold()
        
    def denoiseImage(self):
        self.denoisedImg = restoration.denoise_tv_chambolle(self.imageObj, weight=0.1)
    
    #def thresholdImage(self):
        #self.denoisedImg2 = restoration.denoise_tv_chambolle(self.imageObj2, weight=0.1)
        #thresholdValue = threshold_otsu(self.denoisedImg)
        #self.thresholded2 = closing(self.denoisedImg > thresholdValue, square(2))
        #writeImageToFile(self.thresholded, 'threshold')
        #showImage(self.thresholded2)
    
    def threshold(self):
        #imageArray = Image.open(location)
        #imageArray = np.array(imageArray)
        imageArray = self.denoisedImg
        balance = 0
        noOfPixels = imageArray.size / 3;
        self.thresholded = []
        for eachRow in imageArray:
            for eachPix in eachRow:
                avgNum = reduce(lambda x, y: x+y, eachPix[:3])/3
                balance += avgNum / noOfPixels
        balance -= 0.1
        row=0
        for eachRow in imageArray:
            self.thresholded.append([])
            column=0
            for eachPix in eachRow:
                if reduce(lambda x, y: x+y, eachPix[:3])/3 > balance:
                    self.thresholded[row].append(0)
                    '''eachPix[0] = 1
                    eachPix[1] = 1
                    eachPix[2] = 1'''
                else:
                    self.thresholded[row].append(1)
                column += 1
            row += 1
        '''showImage(np.array(self.thresholded))'''
        self.thresholded = np.array(self.thresholded)
        #self.thresholded = closing(np.asarray(self.thresholded), square(2))
        
    def plotPreProcessed(self):
        thresholdCopy = self.thresholded.copy()
        self.labelImage = measure.label(thresholdCopy)
        self.borders = np.logical_xor(self.thresholded, thresholdCopy)
        self.labelImage[self.borders] = -1
        #writeImageToFile(labelImage[borders], 'labelimagewithborders')
        #image_label_overlay = label2rgb(self.labelImage, image=self.denoisedImg)
        #writeImageToFile(image_label_overlay, 'image_label_overlay')

        fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(12, 12))
        ax.imshow(self.thresholded)
        for region in regionprops(self.labelImage):
            if region.area < 10:
                continue
            
            minimumRow, minimumCol, maximumRow, maximumCol = region.bbox
            rect = mpatches.Rectangle((minimumCol, minimumRow), maximumCol - minimumCol, maximumRow - minimumRow, fill=False, edgecolor='red', linewidth=2)
            ax.add_patch(rect)
        
        plt.show()
        
def plotPreProcessed(numPlate):
    thresholdCopy = numPlate.copy()
    labelImage = measure.label(thresholdCopy)
    borders = np.logical_xor(numPlate, thresholdCopy)
    labelImage[borders] = -1
    #writeImageToFile(labelImage[borders], 'labelimagewithborders')
    #image_label_overlay = label2rgb(self.labelImage, image=self.denoisedImg)
    #writeImageToFile(image_label_overlay, 'image_label_overlay')

    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(12, 12))
    ax.imshow(numPlate)
    for region in regionprops(labelImage):
        if region.area < 10:
            continue
            
        minimumRow, minimumCol, maximumRow, maximumCol = region.bbox
        rect = mpatches.Rectangle((minimumCol, minimumRow), maximumCol - minimumCol, maximumRow - minimumRow, fill=False, edgecolor='red', linewidth=2)
        ax.add_patch(rect)
        
    plt.show()   