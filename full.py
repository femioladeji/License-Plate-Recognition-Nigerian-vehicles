#from preprocess import PreProcess
import numpy as np
import os
from preprocess import PreProcess
from deepMachine import DeepMachineLearning
from ocr import OCROnObjects
from textclassification import TextClassification
from datetime import datetime
import plotting
import wx

imagepath = ''
listRow = 0
listResult = ''

def license_plate_extract(plate_like_objects, pre_process):
    number_of_candidates = len(plate_like_objects)

    if number_of_candidates == 0:
        wx.MessageBox("License plate could not be located",
            "Plate Localization" ,wx.OK|wx.ICON_ERROR)
        return []

    if number_of_candidates == 1:
        license_plate = pre_process.inverted_threshold(plate_like_objects[0])
    else:
        license_plate = pre_process.validate_plate(plate_like_objects)

    return license_plate

def execute_ALPR(event):
    """
    runs the full license plate recognition process.
    function is called when user clicks on the execut button on the gui
    """
    root_folder = os.path.dirname(os.path.realpath(__file__))
    models_folder = os.path.join(root_folder, 'ml_models')
    pre_process = PreProcess(imagepath)
    
    plate_like_objects = pre_process.get_plate_like_objects()
    plotting.plot_cca(pre_process.full_car_image,
        pre_process.plate_objects_cordinates)

    license_plate = license_plate_extract(plate_like_objects, pre_process)

    if len(license_plate) == 0:
        return False
            
    ocr_instance = OCROnObjects(license_plate)

    plotting.plot_cca(license_plate, ocr_instance.candidates['coordinates'])

    deep_learn = DeepMachineLearning()
    text_result = deep_learn.learn(ocr_instance.candidates['fullscale'],
        os.path.join(models_folder, 'SVC_model', 'SVC_model.pkl'),
        (20, 20))

    text_phase = TextClassification()
    scattered_plate_text = text_phase.get_text(text_result)
    plateText = text_phase.text_reconstruction(scattered_plate_text,
        ocr_instance.candidates['columnsVal'])
    
    listResult.InsertStringItem(listRow, plateText)
    listResult.SetStringItem(listRow, 1, str(datetime.today()))
