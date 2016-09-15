import os
import numpy as np
from skimage.io import imread
from skimage.filters import threshold_otsu

class MachineLearningConfig():
    def __init__(self):
        root_directory = self.get_root_directory()

        training_20X20_dir = os.path.join(root_directory, 'training_data\\train20X20')
        training_10X20_dir = os.path.join(root_directory, 'training_data\\train10X20')

        self.training_data = [training_20X20_dir, training_10X20_dir]

        self.letters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def get_root_directory(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        dir_split = os.path.split(current_dir)
        root_directory = dir_split[0]
        return root_directory

    def read_training_data(self, training_directory):
        image_data = []
        target_data = []
        for each_letter in self.letters:
            for each in range(10):
                #training_data[1] is for 10X20 training data images
                img_details = imread(training_directory+'/'+each_letter+'/'+each_letter+'_'+str(each)+'.jpg', as_grey=True)
                binary_image = img_details < threshold_otsu(img_details)
                flat_bin_image = binary_image.reshape(-1)
                image_data.append(flat_bin_image)
                target_data.append(each_letter)

        return (np.array(image_data), np.array(target_data))


