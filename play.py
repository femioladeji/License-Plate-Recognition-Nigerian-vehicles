import numpy as np
from skimage.io import imread, imsave
from skimage.filters import threshold_otsu
from skimage.measure import regionprops
from skimage import measure
import matplotlib.pyplot as plt
from skimage.morphology import binary_erosion
import matplotlib.patches as mpatches

def vertical_projection(image):
    xaxis = []
    yaxis = []

    height, width = image.shape
    summation = 0
    for col in range(width):
        #xaxis.append(col+1)
        summation += (height - sum(image[:, col]))

    print summation / width
    #plt.bar(xaxis, yaxis, 0.5)



location = 'C:/Users/Oladeji Femi/documents/project_stuffs/programs/mine/imgdir/car6.jpg'

img_details = imread(location, as_grey=True)


thresh = threshold_otsu(img_details) * 255

img_details = img_details * 255
grey_img = img_details
img_details = img_details > thresh
img_details = binary_erosion(img_details)
thresholdCopy = img_details.copy()
labelImage = measure.label(thresholdCopy)
borders = np.logical_xor(img_details, thresholdCopy)
labelImage[borders] = -1
charDimensions = (0.08*img_details.shape[0], 0.2*img_details.shape[0], 0.15*img_details.shape[1], 0.4*img_details.shape[1])
minHeight, maxHeight, minWidth, maxWidth = charDimensions
#writeImageToFile(labelImage[borders], 'labelimagewithborders')
#image_label_overlay = label2rgb(self.labelImage, image=self.denoisedImg)
#writeImageToFile(image_label_overlay, 'image_label_overlay')

fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(12, 12))
#ax.imshow(img_details, cmap=plt.cm.gray)
counter = 1
for region in regionprops(labelImage):
    if region.area < 10:
        continue
            
    minimumRow, minimumCol, maximumRow, maximumCol = region.bbox
    regionHeight = maximumRow - minimumRow
    regionWidth = maximumCol - minimumCol
    if regionHeight >= minHeight and regionHeight <= maxHeight and regionWidth >= minWidth and regionWidth <= maxWidth and regionWidth >= regionHeight:
        rect = mpatches.Rectangle((minimumCol, minimumRow), maximumCol - minimumCol, maximumRow - minimumRow, fill=False, edgecolor='red', linewidth=4)
        #imsave('C:/Users/Oladeji Femi/documents/project_stuffs/programs/mine/imgdir/'+str(counter)+'.jpeg', img_details[minimumRow:maximumRow, minimumCol:maximumCol])
        #ax.imshow(img_details[minimumRow:maximumRow, minimumCol:maximumCol], cmap = plt.cm.gray)
        #vertical_projection(img_details[minimumRow:maximumRow, minimumCol:maximumCol])
        if counter == 3:
            
            plate_threshold = threshold_otsu(grey_img[minimumRow:maximumRow, minimumCol:maximumCol]) - 5
            print plate_threshold
            plate_image = grey_img[minimumRow:maximumRow, minimumCol:maximumCol] < plate_threshold
            labeled = measure.label(plate_image)
            ax.imshow(plate_image, cmap=plt.cm.gray)
            charDimensions = (0.4*plate_image.shape[0], 0.85*plate_image.shape[0], 0.05*plate_image.shape[1], 0.15*plate_image.shape[1])
            minHeight, maxHeight, minWidth, maxWidth = charDimensions

            for region in regionprops(labeled):
                minimumRow, minimumCol, maximumRow, maximumCol = region.bbox
                charHeight = maximumRow - minimumRow
                charWidth = maximumCol - minimumCol
                if charHeight >= minHeight and charHeight <= maxHeight and charWidth >= minWidth and charWidth <= maxWidth and charHeight > charWidth:
                    print (charWidth, charHeight)
                    rect = mpatches.Rectangle((minimumCol, minimumRow), maximumCol - minimumCol, maximumRow - minimumRow, fill=False, edgecolor='red', linewidth=4)
                    ax.add_patch(rect)
        counter += 1

        #ax.add_patch(rect)
        
plt.show()