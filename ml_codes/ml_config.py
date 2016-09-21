import os
import numpy as np
from skimage.io import imread
from skimage.filters import threshold_otsu
from sklearn.externals import joblib
from sklearn.decomposition import PCA

class MachineLearningConfig():
    def __init__(self):
        root_directory = self.get_root_directory()

        training_20X20_dir = os.path.join(root_directory, 'training_data', 'train20X20')
        training_10X20_dir = os.path.join(root_directory, 'training_data', 'train10X20')

        self.training_data = [training_20X20_dir, training_10X20_dir]

        self.letters = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z'
        ]

        self.ascertain_characters = {'2', 'Z', 'B', '8', 'D', '0', '5', 'S'}

    def get_root_directory(self):
        """
        gets the main app root directory
        """
        current_dir = os.path.dirname(os.path.realpath(__file__))
        dir_split = os.path.split(current_dir)
        root_directory = dir_split[0]
        return root_directory

    def read_training_data(self, training_directory):
        """
        Reads each of the training data, thresholds it and appends it
        to a List that is converted to numpy array

        Parameters:
        -----------
        training_directory: str; of the training directory

        Returns:
        --------
        a tuple containing
        0: 2D numpy array of the training data with its features in 1D
        1: 1D numpy array of the labels (classifications)
        """

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


    def save_model(self, model, foldername):
        """
        saves a model for later re-use without running the training 
        process all over again. Similar to how pickle works

        Parameters:
        -----------
        model: the machine learning model object
        foldername: str; of the folder to save the model
        """
        save_directory = os.path.join(self.get_root_directory(), 'ml_models/'+foldername+'/')
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        joblib.dump(model, save_directory+'/'+foldername+'.pkl')

    def dimension_reduction(self, train_data, number_of_components):
        pca = PCA(number_of_components)
        return pca.fit_transform(train_data)