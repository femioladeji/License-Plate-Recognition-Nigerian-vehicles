import numpy as np
from skimage.io import imread
from skimage import restoration
from skimage.filters import threshold_otsu
from sklearn.svm import SVC
from sklearn.externals import joblib
from skimage.transform import resize

imgData = []
labelData = []
plateDir = 'C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\platenumberchars\platetrain\\';

def readandpreprocess(imageDir):
    imageDetails = imread(imageDir, as_grey=True)
    imageDetails = restoration.denoise_tv_chambolle(imageDetails, weight=0.1)
    threshValue = threshold_otsu(imageDetails)
    return imageDetails > threshValue
    
for i in range(50):
    imgDir = plateDir+str(i)+'.jpg'
    imgDet = readandpreprocess(imgDir)
    imgDet = resize(imgDet, (100, 50))
    imgDet = np.reshape(imgDet,  -1)
    imgData.append(imgDet)
    labelData.append(1)
    
for i in range(50, 100):
    imgDir = plateDir+str(i)+'.jpg'
    imgDet = readandpreprocess(imgDir)
    imgDet = resize(imgDet, (100, 50))
    imgDet= np.reshape(imgDet, -1)
    imgData.append(imgDet)
    labelData.append(0)
    
myModel = SVC(probability = True)
myModel.fit(imgData, labelData)

joblib.dump(myModel, 'C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\platenumberchars\platemodel\\plates.pkl')

'''testImage = readandpreprocess('C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\platenumberchars\\test\\1.jpg')
testImage = resize(testImage, (100, 50))
testImage = np.reshape(testImage, -1)
result = myModel.predict(testImage)
print result
result = myModel.predict_proba(testImage)
print result'''