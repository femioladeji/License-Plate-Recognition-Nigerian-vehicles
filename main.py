#from matplotlib import pyplot as plt
#from preprocess import PreProcess

#from ObjectsId import ObjectIdentification  

import numpy as np
from skimage.io import imread, imsave
from skimage.filter import threshold_otsu
from skimage.transform import resize
import cPickle
from matplotlib import pyplot as plt
from skimage.morphology import binary_closing, square
from skimage.measure import regionprops
from skimage import restoration
from skimage import measure
from skimage.color import label2rgb
import matplotlib.patches as mpatches
from sklearn.externals import joblib

class PreProcess:
    
    def __init__(self, imgLocation):
        self.imageObj = imread(imgLocation, as_grey=False)
        #writeImageToFile(self.imageObj, 'image')
        #thresholdCalc(histogramGeneration(self.imageObj), len(self.imageObj)*len(self.imageObj[0]))
        self.denoiseImage()
        #self.thresholdImage()
        self.threshold()
        
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

class ObjectIdentification:
    
    def getAllObjects(self, labelImage, borders, image):
        labelImage[borders] = -1
        cord = []
        counter=0
        colList = []
        charDimensions = (0.4*image.shape[0], 0.85*image.shape[0], 0.04*image.shape[1], 0.15*image.shape[1])
        minHeight, maxHeight, minWidth, maxWidth = charDimensions
        for regions in regionprops(labelImage):
            if regions.area > 10:
                minimumRow, minimumCol, maximumRow, maximumCol = regions.bbox
                charHeight = maximumRow - minimumRow
                charWidth = maximumCol - minimumCol
                roi = image[minimumRow:maximumRow, minimumCol:maximumCol]
                if roi.shape[0]*roi.shape[1] == 0:
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
                    'flattened': samples.reshape((samples.shape[0], -1)),
                    'coordinates': np.array(cord),
                    'columnsVal': colList
                    }
                    
        '''print 'Images After Contour Detection'
        print 'Fullscale: ', self.candidates['fullscale'].shape
        print 'Flattened: ', self.candidates['flattened'].shape
        print 'Contour Coordinates: ', self.candidates['coordinates'].shape
        print '============================================================'''
        
        return self.candidates
    
    def plot_to_check(self, what_to_plot, title):
        """
        plots images at several steps of the whole pipeline, just to check output.
        what_to_plot is the name of the dictionary to be plotted
        """
        n_images = what_to_plot['fullscale'].shape[0]
        c=1
        for each in range(n_images):
            #eachBinaryImg = threshold(restoration.denoise_tv_chambolle(what_to_plot['fullscale'][each]))
            #print what_to_plot['fullscale'][each]
            #showImage(what_to_plot['fullscale'][each])
            imsave('C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\imgarray\\'+str(c)+'.jpg', what_to_plot['fullscale'][each])
            c+=1
        fig = plt.figure(figsize=(12, 12))
        
        '''if n_images <=100:
            if n_images < 100:
                total = range(n_images)
            elif n_images == 100:
                total = range(100)
           
            for i in total:
                ax = fig.add_subplot(10, 10, i + 1, xticks=[], yticks=[])
                ax.imshow(what_to_plot['fullscale'][i], cmap="Greys_r")  
                if 'predicted_char' in what_to_plot:
                    ax.text(-6, 8, str(what_to_plot['predicted_char'][i]), fontsize=22, color='red')
            plt.suptitle(title, fontsize=20)
            plt.show()  
        else:
            total = list(np.random.choice(n_images, 100)) 
            for i, j in enumerate(total):
                ax = fig.add_subplot(10, 10, i + 1, xticks=[], yticks=[])
                ax.imshow(what_to_plot['fullscale'][j], cmap="Greys_r")  
                if 'predicted_char' in what_to_plot:
                    ax.text(-6, 8, str(what_to_plot['predicted_char'][j]), fontsize=22, color='red')
            plt.suptitle(title, fontsize=20)
            plt.show()'''

class TextClassification:
    
    def classifyText(self, objects, modelfile):
        model = joblib.load(modelfile)
        plateString = ''
        for eachObject in objects:
            eachObject = binary_closing(threshold(eachObject))
            eachObject = np.reshape(eachObject, -1)
            aCharacter = model.predict(eachObject)
            plateString += aCharacter[0]
        
        return plateString
        
        
    def textReconstruction(self, plateString, positionList):
        posListCopy = positionList[:]
        positionList.sort()
        rightPlateString = ''
        for each in positionList:
            rightPlateString += plateString[posListCopy.index(each)]
            
        return rightPlateString

def showImage(imgArray):
    #figImage = plt.figure()
    ax1 = plt.subplot2grid((8,8), (0,0), rowspan=8, colspan=8)
    ax1.imshow(imgArray)
    plt.show()
    #writeImageToFile(imgArray)

def writeImageToFile(imgList, filename):
    textFile = open('C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\\'+str(filename)+'.txt', 'w')
    textFile.write(str(imgList))

def threshold(imageArray):
    balance = 0
    noOfPixels = imageArray.size / 3;
    thresholded = []
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = reduce(lambda x, y: x+y, eachPix[:3])/3
            balance += avgNum / noOfPixels
    balance -= 0.1
    row=0
    for eachRow in imageArray:
        thresholded.append([])
        column=0
        for eachPix in eachRow:
            if reduce(lambda x, y: x+y, eachPix[:3])/3 > balance:
                thresholded[row].append(0)
                '''eachPix[0] = 1
                eachPix[1] = 1
                eachPix[2] = 1'''
            else:
                thresholded[row].append(1)
            column += 1
        row += 1
        '''showImage(np.array(self.thresholded))'''
    return np.array(thresholded)
        #self.thresholded = closing(np.asarray(self.thresholded), square(2))

imageFile = 'C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\imgdir\\plate48.jpg'


preProcessed = PreProcess(imageFile)
#showImage(preProcessed.thresholded)
preProcessed.plotPreProcessed()

objectId = ObjectIdentification()
allObjects = objectId.getAllObjects(preProcessed.labelImage, preProcessed.borders, preProcessed.denoisedImg)
#allObjects = objectId.getAllObjects(preProcessed.thresholded, preProcessed.borders, preProcessed.imageObj)
objectId.plot_to_check(allObjects, 'objects identified')

textPhase = TextClassification()
scatteredplateText = textPhase.classifyText(allObjects['fullscale'], 'C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\platenumberchars\model\\nigeriaplatenumbermodel.pkl')
plateText = textPhase.textReconstruction(scatteredplateText, allObjects['columnsVal'])
print plateText