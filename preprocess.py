import numpy as np
from skimage.io import imread
from skimage import restoration
from skimage import measure
from skimage.measure import regionprops
from skimage.filters import threshold_otsu
from skimage.transform import resize

class PreProcess():
    
    def __init__(self, image_location):
        """
        reads the image in grayscale and thresholds the image

        Parameters:
        -----------

        image_location: str; full image directory path
        """
        self.full_car_image = imread(image_location, as_grey=True)
        
        self.full_car_image = self.resize_if_necessary(self.full_car_image)

        self.binary_image = self.threshold(self.full_car_image)
        
    def denoise(sefl, imgDetails):
        return restoration.denoise_tv_chambolle(imgDetails)
        
    def threshold(self, gray_image):
        """
        uses the otsu threshold method to generate a binary image

        Parameters:
        -----------
        gray_image: 2D array: gray scale image to be thresholded

        Return:
        --------
        2-D array of the binary image each pixel is either 1 or 0
        """
        thresholdValue = threshold_otsu(gray_image)
        return gray_image > thresholdValue
        
    def get_plate_like_objects(self):
        """
        uses principles of connected component analysis and labelling to map 
        out object regions.

        The plate dimensions were based on the following characteristics
        i.  They are rectangular in shape.
        ii. The width is more than the height
        iii. The ratio of the width to height is approximately 2:1
        iv. The proportion of the width of the license plate region to the 
        full image ranges between 15% to 40% depending on how the car image 
        was taken
        v.  The proportion of the height of the license plate region to the 
        full image is between 8% to 20%

        Return:
        --------
        3-D Array of license plate candidates region

        """
        self.label_image = measure.label(self.binary_image)
        self.plate_objects_cordinates = []
        threshold = self.binary_image
        plate_dimensions = (0.08*threshold.shape[0], 0.2*threshold.shape[0], 0.15*threshold.shape[1], 0.4*threshold.shape[1])
        minHeight, maxHeight, minWidth, maxWidth = plate_dimensions
        plate_like_objects = []
        for region in regionprops(self.label_image):
            if region.area < 10:
                continue
        
            minimumRow, minimumCol, maximumRow, maximumCol = region.bbox
            regionHeight = maximumRow - minimumRow
            regionWidth = maximumCol - minimumCol
            if regionHeight >= minHeight and regionHeight <= maxHeight and regionWidth >= minWidth and regionWidth <= maxWidth and regionWidth > regionHeight:
                plate_like_objects.append(self.full_car_image[minimumRow:maximumRow,
                    minimumCol:maximumCol])
                self.plate_objects_cordinates.append((minimumRow, minimumCol,
                    maximumRow, maximumCol))
                
        return plate_like_objects

    def validate_plate(self, candidates):
        """
        validates the candidate plate objects by using the idea
        of vertical projection to calculate the sum of pixels across
        each column and then find the average.

        This method still needs improvement

        Parameters:
        ------------
        candidate: 3D Array containing 2D arrays of objects that looks
        like license plate

        Returns:
        --------
        a 2D array of the likely license plate region

        """
        for each_candidate in candidates:
            height, width = each_candidate.shape
            each_candidate = self.inverted_threshold(each_candidate)
            license_plate = []
            highest_average = 0
            total_white_pixels = 0
            for column in range(width):
                total_white_pixels += sum(each_candidate[:, column])
            
            average = float(total_white_pixels) / width
            if average >= highest_average:
                license_plate = each_candidate

        return license_plate

    def inverted_threshold(self, grayscale_image):
        """
        used to invert the threshold of the candidate regions of the plate
        localization process. The inversion was neccessary
        because the license plate area is white dominated which means
        they have a greater gray scale value than the character region

        Parameters:
        -----------
        grayscale_image: 2D array of the gray scale image of the
        candidate region

        Returns:
        --------
        a 2D binary image
        """
        threshold_value = threshold_otsu(grayscale_image) - 0.05
        return grayscale_image < threshold_value

    def resize_if_necessary(self, image_to_resize):
        """
        function is used to resize the image before further
        processing if the image is too big. The resize is done
        in such a way that the aspect ratio is still maintained

        Parameters:
        ------------
        image_to_resize: 2D-Array of the image to be resized
        3D array image (RGB channel) can also be resized

        Return:
        --------
        resized image or the original image if resize is not
        neccessary
        """
        height, width = image_to_resize.shape
        ratio = float(width) / height
        # if the image is too big, resize
        if width > 600:
            width = 600
            height = round(width / ratio)
            return resize(image_to_resize, (height, width))

        return image_to_resize