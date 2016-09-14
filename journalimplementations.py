import numpy as np
from skimage.io import imread, imsave
from matplotlib import pyplot as plt
from skimage.filters import threshold_otsu, sobel
from skimage.measure import regionprops
from skimage import measure
from skimage.morphology import binary_erosion, binary_dilation, binary_closing, binary_opening

import matplotlib.patches as mpatches
from skimage.measure import regionprops

fig = plt.figure(figsize=(12, 12))

def showImage(imgArray, i):
    #figImage = plt.figure()
    ax1 = fig.add_subplot(2, 2, i, xticks=[], yticks=[])
    ax1.imshow(imgArray, cmap=plt. cm. gray)
    #writeImageToFile(imgArray)
    
location = 'C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\imgdir\plate16.jpeg'
realimg = imread(location, as_grey=False)
greyimg = imread(location, as_grey=True)
#edges = sobel(greyimg)
binaryimage = greyimg < threshold_otsu(greyimg)
#imsave('C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\imgdir\grey.jpg', greyimg)
#imsave('C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\imgdir\sobeledge.jpg', edges)
#imsave('C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\imgdir\sobeledgev.jpg', sobel_v(greyimg))
#showImage(binaryimage, 0)
#showImage(edges, 1)
#opened = binary_opening(binaryimage)
#imsave('C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\imgdir\opened.jpg', opened)
#closing = binary_closing(binaryimage)
#imsave('C:\Users\Oladeji Femi\Documents\project_stuffs\programs\mine\imgdir\closed.jpg', closing)
#showImage(opened, 1)
#showImage(closing, 2)
#sobelclosed = sobel(closing)
#showImage(sobelclosed < threshold_otsu(sobelclosed), 3)
labelImage = measure.label(binaryimage)
fig2, ax = plt.subplots(ncols=1, nrows=1, figsize=(12, 12))
ax.imshow(binaryimage, cmap=plt.cm.gray)
for eachregion in regionprops(labelImage):
    #if eachregion.area < 10:
    #        continue
            
    minimumRow, minimumCol, maximumRow, maximumCol = eachregion.bbox
    rect = mpatches.Rectangle((minimumCol, minimumRow), maximumCol - minimumCol, maximumRow - minimumRow, fill=False, edgecolor='red', linewidth=5)
    ax.add_patch(rect)
plt.show()