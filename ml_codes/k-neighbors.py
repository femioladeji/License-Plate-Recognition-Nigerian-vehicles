import numpy as np
from skimage.io import imread
from skimage.filters import threshold_otsu
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import os
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score

training_20X20_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'platenumberchars\\train')
training_10X20_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'platenumberchars\\new_train')

letters_dict = {'0':10,'1':10,'2':10,'3':10,'4':10,'5':10,'6':10,'7':10,'8':10,'9':10,'A':10,'B':10,'C':10,'D':10,'E':10,'F':10,'G':10,'H':10,'J':10,'K':10,'L':10,'M':10,'N':10,'P':10,'Q':10,'R':10,'S':10,'T':10,'U':10,'V':10,'W':10,'X':10,'Y':10,'Z':10}
letters = list(letters_dict.keys())

image_data = []
target_data = []

for each_letter in letters:
    for each in range(letters_dict[each_letter]):
        img_details = imread(training_20X20_dir+'/'+each_letter+'/'+each_letter+'_'+str(each)+'.jpg', as_grey=True)
        #img_details = imread(training_10X20_dir+'/'+each_letter+'/'+each_letter+'_'+str(each)+'.jpg', as_grey=True)
        binary_image = img_details < threshold_otsu(img_details)
        flat_bin_image = binary_image.reshape(-1)
        image_data.append(flat_bin_image)
        target_data.append(each_letter)

image_data = np.array(image_data)
target_data = np.array(target_data)

# img_train, img_test, target_train, target_test = train_test_split(image_data, target_data)
# print img_train.shape
# print img_test.shape

for number_of_neighbors in range(3, 8):
    neighbor_model = KNeighborsClassifier(n_neighbors = number_of_neighbors)

    print cross_val_score(neighbor_model, image_data, target_data)
    # neighbor_model.fit(img_train, target_train)

    # prediction = neighbor_model.predict(img_test)

    # for i in range(len(prediction)):
    #     if prediction[i] != target_test[i]:
    #         print prediction[i], target_test[i]

    # print neighbor_model.score(img_test, target_test)
    # print (float(np.sum(prediction == target_test)) / len(target_test)) * 100
    # perc_accuracy = accuracy_score(img_test, prediction)

    # print perc_accuracy