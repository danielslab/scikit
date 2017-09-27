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
