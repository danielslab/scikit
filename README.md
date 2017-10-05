# Prerequisites: The following packages are needed:
* numpy
* matplotlib
* sklearn - Scikit Learn

## 1.'knn.py', K Nearest Neighbors Classifier
* To find the quadrant of any given x,y coordinates in 2d cartesian system.
### Description:
* A numpy array for angle theta from 0 to 360 degrees is created
* A numpy array for quandrant is created with values 1 to 4.
* A 2d numpy data array with cosine and sine values of theta are created.
* The data array is plotted with quadrant as colormap
* A KNN classifier is created with 6 neighbors.
* The KNN classifier is fit with data array againt quadrant array.
* Accuracy of the predictions are printed.

## 2.'digits_visual.py'
* Scikit learn has a reduced version of the MNIST dataset and it is called digits. Each sample in this dataset is an 8x8 image representing a handwritten digit. Each pixel is represented by an integer in the range 0 to 16, indicating varying levels of black.
### Description:
* To import the digits dataset.
* To print the details of the dataset.
* To plot the 2D array of the image.

## 3.'digits_predict.py'
* Scikit learn has a reduced version of the MNIST dataset and it is called digits. Each sample in this dataset is an 8x8 image representing a handwritten digit. Each pixel is represented by an integer in the range 0 to 16, indicating varying levels of black.
### Description:
* To import the digits dataset.
* To split the dataset into train and test data
* To apply KNN fit on the train data set
* To test the KNN score against the test data set and print the accuracy.