# License Plate Recognition For Vehicles

[![Travis](https://travis-ci.org/femioladeji/License-Plate-Recognition-Nigerian-vehicles.png)](https://travis-ci.org/femioladeji/License-Plate-Recognition-Nigerian-vehicles)
[![circleci](https://circleci.com/gh/femioladeji/License-Plate-Recognition-Nigerian-vehicles.png)](https://circleci.com/gh/femioladeji/License-Plate-Recognition-Nigerian-vehicles)

## **About**
A python program that uses concepts of image processing and OCR to identify the characters on a Nigerian license plate. The OCR aspect was done with machine learning.

## **Functionality**
1. A GUI interface that makes image selection easier
2. Performs all the stages of Automatic License plate recognition (ALPR); plate localization, character segmentation and character recognition
3. Saves the license plate characters in the database
4. You can generate your model that will be used by the ALPR
5. You can compare the performance of supervised learning classifiers
6. You can use your own training data
7. Easy visualization for debugging purposes

## **Dependencies**
The program was written with python 2.7 and the following python packages are required
* [Numpy](http://docs.scipy.org/doc/numpy-1.10.0) Numpy is a python package that helps in handling n-dimensional arrays and matrices
* [Scipy](http://scipy.org) Scipy for scientific python
* [Scikit-image](http://scikit-image.org/) Scikit-image is a package for image processing
* [Scikit-learn](http://scikit-learn.org/) Scikit-learn is for all machine learning operations
* [Matplotlib](http://matplotlib.org) Matplotlib is a 2D plotting library for python
* [PyMysql](https://github.com/PyMYSQL/PyMYSQL) A pure-python MYSQL client library
* [wxpython](http//wxpython.org) Python GUI package

## **How to use**
1. Clone the repository or download the zip `git clone https://github.com/femioladeji/License-Plate-Recognition-Nigerian-vehicles`
2. Change to the cloned directory (or extracted directory)
3. Create a virtual environment with virtualenv or virtualenvwrapper
4. Install all the necessary dependencies by using pip `pip install -r requirements.txt`
5. Install wxpython with `pip install wxpython`
6. Start the program `python ALPR.py`

## **Other Information**
- For Mac users, follow this [wiki](https://wiki.wxpython.org/wxPythonVirtualenvOnMac) before you can use wxpython
- For windows users, you may need to install BLAS/LAPACK before you can install `scipy`
- The script that retrieves plate number information was written by [@othreecodes](https://github.com/othreecodes)