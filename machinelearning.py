import numpy as np
from skimage.io import imread, imsave
from skimage.transform import resize
from skimage.morphology import closing, square
from skimage.filters import threshold_otsu
from skimage import restoration
from sklearn.svm import SVC
from sklearn.externals import joblib
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12, 12))

def showImage(imgArray, i, char):
    #figImage = plt.figure()
    ax1 = fig.add_subplot(7, 7, i, xticks=[], yticks=[])
    ax1.text(-3, 8, char, fontsize=16, color='red')
    ax1.imshow(imgArray)
    #writeImageToFile(imgArray)
    
imgListDir = 'C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\platenumberchars\\train\\'

imageData = []
targetData = []

def readandpreprocess(imageDir):
    imageDetails = imread(imageDir, as_grey=True)
    imageDetails = restoration.denoise_tv_chambolle(imageDetails, weight=0.1)
    return imageDetails < threshold_otsu(imageDetails)
    
    #return thresholdImage(imageDetails)
    
def thresholdImage(imageDetails):
    #imageArray = Image.open(location)
    #imageArray = np.array(imageArray)
    imageArray = imageDetails
    balance = 0
    noOfPixels = imageArray.size / 3
    thresholded = []
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = reduce(lambda x, y: x+y, eachPix[:3])/3
            balance += avgNum / noOfPixels
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
    return np.array(thresholded)
    #self.thresholded = closing(np.asarray(self.thresholded), square(2))    


lettersDict = {'0':10,'1':10,'2':10,'3':10,'4':10,'5':10,'6':10,'7':10,'8':10,'9':10,'A':10,'B':10,'C':10,'D':10,'E':10,'F':10,'G':10,'H':10,'J':10,'K':10,'L':10,'M':10,'N':10,'P':10,'Q':10,'R':10,'S':10,'T':10,'U':10,'V':10,'W':10,'X':10,'Y':10,'Z':10}
letters = list(lettersDict.keys())

count=0;
for each in letters:
    eachGroupDir = imgListDir+each+'\\'
    for aTraining in range(lettersDict[each]):
        eachTrainingImg = eachGroupDir+each+'_'+str(aTraining)+'.jpg'
        
        letterDetails = readandpreprocess(eachTrainingImg)
        #if(aTraining == 9):
        #    showImage(letterDetails, count, each)
        #imsave('C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\platenumberchars\\xxx\\'+each+'_'+str(aTraining)+'.jpg', letterDetails)
        binaryImg = np.reshape(letterDetails, -1)
        imageData.append(binaryImg)
        targetData.append(each)
    count += 1

rng = np.random.RandomState(0)

permutation = rng.permutation(len(imageData))
imageData, targetData = imageData[permutation], targetData[permutation]
    
model = SVC()
#model.fit(imageData, targetData)
from sklearn.cross_validation import cross_val_score
scores = cross_val_score(model, imageData, targetData)
print(scores)
print(np.mean(scores))
#joblib.dump(model, 'C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\platenumberchars\model\\nigeriaplatenumbermodel.pkl')
#testDir = 'C:\Users\Oluwafemi\Documents\project_stuffs\programs\mine\imgarray\\2.jpg'
#testImgDet = readandpreprocess(testDir)
#testImgDet = np.reshape(testImgDet, -1)
#print model.predict(testImgDet)