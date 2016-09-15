import numpy as np
import os
from skimage.io import imread, imsave
from skimage.transform import resize

imgListDir = 'C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\platenumberchars\\train\\'

lettersDict = {'0':10,'1':10,'2':10,'3':10,'4':10,'5':10,'6':10,'7':10,'8':10,'9':10,'A':10,'B':10,'C':10,'D':10,'E':10,'F':10,'G':10,'H':10,'J':10,'K':10,'L':10,'M':10,'N':10,'P':10,'Q':10,'R':10,'S':10,'T':10,'U':10,'V':10,'W':10,'X':10,'Y':10,'Z':10}
letters = list(lettersDict.keys())

count=0;
for each in letters:
    eachGroupDir = imgListDir+each+'\\'
    for aTraining in range(lettersDict[each]):
        eachTrainingImg = eachGroupDir+each+'_'+str(aTraining)+'.jpg'
        
        image = imread(eachGroupDir+each+'_'+str(aTraining)+'.jpg', as_grey=True)

        new_image = resize(image, (20, 10))
        
        directory = 'C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\platenumberchars\\new_training\\'+each+'\\'

        if not os.path.exists(directory):
            os.makedirs(directory)

        imsave('C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\platenumberchars\\new_training\\'+each+'\\'+each+'_'+str(aTraining)+'.jpg', new_image)
        
    count += 1