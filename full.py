#from preprocess import PreProcess
import numpy as np
from skimage.io import imread
from skimage import restoration
from skimage import measure
from skimage.measure import regionprops
from skimage.filters import threshold_otsu
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import wx

from preprocess import PreProcess
from deepMachine import DeepMachineLearning
from ocr import OCROnObjects
from textclassification import TextClassification
from dbAspect import connectToPhp
from datetime import datetime

imagepath = ''
listRow = 0
listResult = ''
def showImage(imgArray):
    #figImage = plt.figure()
    ax1 = plt.subplot2grid((8,8), (0,0), rowspan=8, colspan=8)
    ax1.imshow(imgArray)
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
    
def executeALPR(event):
    rootfolder = 'C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\\'
    preProObj = PreProcess(imagepath)

    #plotPreProcessed(preProObj.binaryImage)
    
    platelikeObjects = preProObj.getPlateLikeObjects()
    
    deepLearn = DeepMachineLearning()
    
    result = deepLearn.learn(platelikeObjects, rootfolder+'platenumberchars\platemodel\\plates.pkl', (100, 50))
    
    possiblyNumPlate = []
    
    
    for count in range(len(result)):
        if result[count][0] == 1:
            threshValue = threshold_otsu(platelikeObjects[count]) - 0.05
            possiblyNumPlate.append(platelikeObjects[count] < threshValue)
            
    ocrObject = OCROnObjects(possiblyNumPlate)
    
    textPhase = TextClassification()
    textResult = deepLearn.learn(ocrObject.candidates['fullscale'], rootfolder+'platenumberchars\model\\nigeriaplatenumbermodel.pkl', (20, 20))
    scatteredplateText = textPhase.getText(textResult)
    plateText = textPhase.textReconstruction(scatteredplateText, ocrObject.candidates['columnsVal'])
    
    listResult.InsertStringItem(listRow, plateText)
    listResult.SetStringItem(listRow, 1, str(datetime.today()))
    #dbObj = connectToPhp(plateText)
    #print dbObj.response
