import numpy as np
from skimage.io import imread, imsave
from matplotlib import pyplot as plt
from skimage.filters import threshold_otsu, sobel
from skimage.measure import regionprops
from skimage import measure
from skimage.morphology import binary_opening, binary_closing, binary_erosion, binary_dilation
plategrey = imread('C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\imgdir\plate5.jpg', as_grey=True)

fig = plt.figure(figsize=(12, 12))

def showImage(imgArray, i):
    #figImage = plt.figure()
    ax1 = fig.add_subplot(1, 1, i, xticks=[], yticks=[])
    ax1.imshow(imgArray, cmap=plt.cm.gray)
    
binaryimg = plategrey < threshold_otsu(plategrey)
eroded = binary_erosion(binaryimg, [[1,1,1],[1,1,1],[1,1,1]])
showImage(eroded, 0)


'''xaxis = []
yaxis = []

height, width = binaryimg.shape
for col in range(width):
    xaxis.append(col+1)
    yaxis.append(sum(binaryimg[:, col]))

plt.bar(xaxis, yaxis, 0.5)'''

plt.show()