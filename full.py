#from preprocess import PreProcess
import numpy as np
from skimage.io import imread
from skimage import restoration
from skimage import measure
from skimage.measure import regionprops
from skimage.filters import threshold_otsu
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import wx
import os
from preprocess import PreProcess
from deepMachine import DeepMachineLearning
from ocr import OCROnObjects
from textclassification import TextClassification
from dbAspect import connectToPhp
from datetime import datetime

imagepath = ''
listRow = 0
listResult = ''
    

def execute_ALPR(event):
    """
    runs the full license plate recognition process.
    function is called when user clicks on the execut button on the gui
    """
    root_folder = os.path.join(os.path.realpath(__file__))
    models_folder = os.path.join(root_folder, 'ml_models')
    pre_process = PreProcess(imagepath)
    
    plate_like_objects = pre_process.get_plate_like_objects()
    
    number_of_candidates = len(plate_like_objects)

    if number_of_candidates == 0:
        return False
    elif number_of_candidates == 1:
        license_plate = pre_process.inverted_threshold(plate_like_objects[0])
    else:
        license_plate = pre_process.validate_plate(plate_like_objects)

            
    ocr_instance = OCROnObjects(license_plate)    

    deep_learn = DeepMachineLearning()
    text_result = deep_learn.learn(ocr_instance.candidates['fullscale'],
        os.path.join(models_folder, 'svm_model'), (20, 20))

    text_phase = TextClassification()
    scattered_plate_text = text_phase.get_text(text_result)
    plateText = text_phase.text_reconstruction(scattered_plate_text,
        ocr_instance.candidates['columnsVal'])
    
    listResult.InsertStringItem(listRow, plateText)
    listResult.SetStringItem(listRow, 1, str(datetime.today()))
    #dbObj = connectToPhp(plateText)
    #print dbObj.response
