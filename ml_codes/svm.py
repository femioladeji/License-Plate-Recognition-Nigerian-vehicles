import numpy as np
from skimage.io import imread
from skimage.filters import threshold_otsu
import os
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split, cross_val_score

training_20X20_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'platenumberchars\\train')
training_10X20_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'platenumberchars\\new_train')

letters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#each letter has 10 samples

image_data = []
target_data = []



for each_letter in letters:
    for each in range(10):
        img_details = imread(training_20X20_dir+'/'+each_letter+'/'+each_letter+'_'+str(each)+'.jpg', as_grey=True)
        #img_details = imread(training_10X20_dir+'/'+each_letter+'/'+each_letter+'_'+str(each)+'.jpg', as_grey=True)
        binary_image = img_details < threshold_otsu(img_details)
        flat_bin_image = binary_image.reshape(-1)
        image_data.append(flat_bin_image)
        target_data.append(each_letter)

image_data = np.array(image_data)
target_data = np.array(target_data)

sv_classifier = SVC(kernel='rbf')

print cross_val_score(sv_classifier, image_data, target_data, cv = 5)