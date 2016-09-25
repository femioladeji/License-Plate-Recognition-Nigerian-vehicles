import numpy as np
from skimage.transform import resize
from skimage import measure
from skimage.measure import regionprops

class OCROnObjects():
    
    def __init__(self, license_plate):
        character_objects = self.identify_boundary_objects(license_plate)
        self.get_regions(character_objects, license_plate)
        
    def identify_boundary_objects(self, a_license_plate):
        labelImage = measure.label(a_license_plate)
        character_dimensions = (0.4*a_license_plate.shape[0], 0.85*a_license_plate.shape[0], 0.04*a_license_plate.shape[1], 0.15*a_license_plate.shape[1])
        minHeight, maxHeight, minWidth, maxWidth = character_dimensions
        regionLists = regionprops(labelImage)
        return regionLists
    
    def get_regions(self, character_objects, a_license_plate):
        """
        used to map out regions where the license plate charcters are 
        the principle of connected component analysis and labelling
        were used

        Parameters:
        -----------
        a_license_plate: 2D numpy binary image of the license plate

        Returns:
        --------
        a dictionary containing the index
        fullscale: 3D array containig 2D array of each character 
        columnsVal: 1D array the starting column of each character
        coordinates:
        """
        cord = []
        counter=0
        column_list = []
        character_dimensions = (0.35*a_license_plate.shape[0], 0.60*a_license_plate.shape[0], 0.05*a_license_plate.shape[1], 0.15*a_license_plate.shape[1])
        minHeight, maxHeight, minWidth, maxWidth = character_dimensions
        for regions in character_objects:
            minimumRow, minimumCol, maximumRow, maximumCol = regions.bbox
            character_height = maximumRow - minimumRow
            character_width = maximumCol - minimumCol
            roi = a_license_plate[minimumRow:maximumRow, minimumCol:maximumCol]
            if character_height > minHeight and character_height < maxHeight and character_width > minWidth and character_width < maxWidth:
                if counter == 0:
                    samples = resize(roi, (20,20))
                    cord.append(regions.bbox)
                    counter += 1
                elif counter == 1:
                    roismall = resize(roi, (20,20))
                    samples = np.concatenate((samples[None,:,:], roismall[None,:,:]), axis=0)
                    cord.append(regions.bbox)
                    counter+=1
                else:
                    roismall = resize(roi, (20,20))
                    samples = np.concatenate((samples[:,:,:], roismall[None,:,:]), axis=0)
                    cord.append(regions.bbox)
                column_list.append(minimumCol)
        if len(column_list) == 0:
            self.candidates = {}
        else:
            self.candidates = {
                        'fullscale': samples,
                        'coordinates': np.array(cord),
                        'columnsVal': column_list
                        }
        
        return self.candidates