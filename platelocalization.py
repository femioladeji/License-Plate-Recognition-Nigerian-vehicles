import numpy as np
from skimage.io import imread, imsave
from skimage import restoration
from matplotlib import pyplot as plt
from skimage.filters import threshold_otsu, sobel
from skimage import measure

import matplotlib.patches as mpatches
from skimage.measure import regionprops


fig = plt.figure(figsize=(12, 12))

def showImage(imgArray, i):
    #figImage = plt.figure()
    ax1 = fig.add_subplot(2, 2, i, xticks=[], yticks=[])
    ax1.imshow(imgArray, cmap=plt.cm.gray)
    #writeImageToFile(imgArray)
def threshold(imageArray):
    balance = 0
    noOfPixels = imageArray.size / 3;
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = reduce(lambda x, y: x+y, eachPix[:3])/3
            balance += avgNum / noOfPixels
    balance -= 0.1
    row=0
    for eachRow in imageArray:
        column=0
        for eachPix in eachRow:
            if reduce(lambda x, y: x+y, eachPix[:3])/3 < balance:
                imageArray[row][column][0] = 0
                imageArray[row][column][1] = 0
                imageArray[row][column][2] = 0
                '''eachPix[0] = 1
                eachPix[1] = 1
                eachPix[2] = 1'''
            else:
                imageArray[row][column][0] = 1
                imageArray[row][column][1] = 1
                imageArray[row][column][2] = 1
            column += 1
        row += 1
        '''showImage(np.array(self.thresholded))'''
    return imageArray


def plotPreProcessed(threshold):
    thresholdCopy = threshold.copy()
    labelImage = measure.label(thresholdCopy)
    borders = np.logical_xor(threshold, thresholdCopy)
    labelImage[borders] = -1
    #writeImageToFile(labelImage[borders], 'labelimagewithborders')
    #image_label_overlay = label2rgb(self.labelImage, image=self.denoisedImg)
    #writeImageToFile(image_label_overlay, 'image_label_overlay')
    charDimensions = (0.05*threshold.shape[0], 0.3*threshold.shape[0], 0.1*threshold.shape[1], 0.4*threshold.shape[1])
    minHeight, maxHeight, minWidth, maxWidth = charDimensions
    counter=0
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(12, 12))
    ax.imshow(threshold, cmap=plt.cm.gray)
    for region in regionprops(labelImage):
        if region.area < 10:
            continue
        
        minimumRow, minimumCol, maximumRow, maximumCol = region.bbox
        regionHeight = maximumRow - minimumRow
        regionWidth = maximumCol - minimumCol
        rect = mpatches.Rectangle((minimumCol, minimumRow), maximumCol - minimumCol, maximumRow - minimumRow, fill=False, edgecolor='red', linewidth=5)
        #if regionHeight > minHeight and regionHeight < maxHeight and regionWidth > minWidth and regionWidth < maxWidth and regionWidth > regionHeight:
            #showImage(threshold[minimumRow:maximumRow, minimumCol:maximumCol], counter)
            #pixelsum = 0
            
            #for col in range(regionWidth):
            #    pixelsum += regionHeight - sum(threshold[minimumRow:maximumRow, minimumCol+col])
                
            #print pixelsum
            #plt.bar(xaxis, yaxis, 0.5)
        #imsave('C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\imgarray\\'+str(counter)+'.png', car[minimumRow:maximumRow, minimumCol:maximumCol])
            #counter+=1
            
        ax.add_patch(rect)
    
    plt.show()
car = imread('C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\imgdir\car6.jpg', as_grey=True);
#showImage(sobel(car))
#car = restoration.denoise_tv_chambolle(car)
thresholdValue=threshold_otsu(car)
binaryImage = car > thresholdValue
plotPreProcessed(car > threshold_otsu(car))
#showImage(sobel(binaryImage))