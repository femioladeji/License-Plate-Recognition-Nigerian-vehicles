# License Plate Recognition For Vehicles

[![Travis](https://travis-ci.org/femidotexe/License-Plate-Recognition-Nigerian-vehicles.png)](https://travis-ci.org/femidotexe/License-Plate-Recognition-Nigerian-vehicles)
[![circleci](https://circleci.com/gh/femidotexe/License-Plate-Recognition-Nigerian-vehicles.png)](https://circleci.com/gh/femidotexe/License-Plate-Recognition-Nigerian-vehicles)

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
* [Scikit-image](http://scikit-image.org/) Scikit-image is a package for image processing
* [Scikit-learn](http://scikit-learn.org/) Scikit-learn is for all machine learning operations
* [Matplotlib](http://matplotlib.org) Matplotlib is a 2D plotting library for python
* [PyMysql](https://github.com/PyMYSQL/PyMYSQL) A pure-python MYSQL client library
* [wxpython](http//wxpython.org) Python GUI package

## **How to use**
1. Clone the repository or download the zip
```
git clone https://github.com/femidotexe/License-Plate-Recognition-Nigerian-vehicles-
```
2. Change to the cloned directory (or extracted directory)
3. Install all the necessary dependencies by using pip
```
pip install -r requirements.txt
```
4. Start the program
```
python start.py
```

## **Contribute**
Fill free to fork and raise PR
