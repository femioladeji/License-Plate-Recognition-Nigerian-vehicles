from skimage.io import imread
from skimage.filters import threshold_otsu
from skimage.feature import match_template
import numpy as np


template = imread("C:\\Users\\Oladeji Femi\\Documents\\programs\\python\\License-Plate-Recognition-Nigerian-vehicles-\\training_data\\train20X20\\2\\2_0.jpg", as_grey=True)

template = template < threshold_otsu(template)

sum = 0.0
for i in range(1, 10):
    image = imread("C:\\Users\\Oladeji Femi\\Documents\\programs\\python\\License-Plate-Recognition-Nigerian-vehicles-\\training_data\\train20X20\\Z\\Z_"+str(i)+".jpg", as_grey=True)

    image = image < threshold_otsu(image)

    v = match_template(image, template)
    
    sum += v[0, 0]

print sum / 9