print(__doc__)

# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# License: BSD 3 clause
import numpy as np
from skimage.io import imread
from PIL import Image
from skimage.transform import resize
from skimage.feature import hog
from skimage.filters import threshold_otsu
# Standard scientific Python imports
import matplotlib.pyplot as plt

# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics

# The digits dataset
digits = datasets.load_digits()

# The data that we are interested in is made of 8x8 images of digits, let's
# have a look at the first 3 images, stored in the `images` attribute of the
# dataset.  If we were working from image files, we could load them using
# pylab.imread.  Note that each image must have the same size. For these
# images, we know which digit they represent: it is given in the 'target' of
# the dataset.
images_and_labels = list(zip(digits.images, digits.target))
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)

# To apply a classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:
n_samples = len(digits.images)
print digits.images[0]
data = digits.images.reshape((n_samples, -1))
# Create a classifier: a support vector classifier
classifier = svm.SVC(gamma=0.001)

# We learn the digits on the first half of the digits
classifier.fit(data[:n_samples / 2], digits.target[:n_samples / 2])

# Now predict the value of the digit on the second half:
expected = digits.target[n_samples / 2:]
predicted = classifier.predict(data[n_samples / 2:])

print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

images_and_predictions = list(zip(digits.images[n_samples / 2:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)

plt.show()


#img1 = imread("C:\Users\Oluwafemi\Documents\project_stuffs\programs\mine\imgdir\8.jpg", as_grey=True)
img2 = imread("C:\Users\Oluwafemi\Documents\project_stuffs\programs\mine\imgdir\\4.jpg", as_grey=True)

img1 = imread("C:\Users\Oluwafemi\Documents\project_stuffs\programs\mine\imgdir\\1_.jpg", as_grey=True)
image1 = imread("C:\Users\Oluwafemi\Documents\project_stuffs\programs\mine\imgdir\\5.jpg", as_grey=True)
#img1 = img1.resize(8, 8)
#thresh = threshold_otsu(image1)
#binary = image > thresh

binary = resize(image1, (8,8))
binary = binary.reshape(1, -1)
#toPredictImg = hog(binary, orientations=9, pixels_per_cell=(4, 4), cells_per_block=(1, 1), visualise=False)
print binary
nbr = classifier.predict(binary)
print nbr
print digits.target_names[nbr]