# Prerequisites: The following packages are needed:
* numpy
* matplotlib
* pandas
* sklearn - Scikit Learn

## 1.'linear_regression.py', Linear Regression Model
* The celcius to fahrenheit conversion formula is tested with linear regression:
### Description:
* Data array is created with values from 1 to 20 for celcius.
* Target array is created for Fahrenheit = Celcius*1.8 + 32
* Data and Target array are split to train and test set.
* linear regression fit is applied on train set.
* Score is calculated for the regression by applying predict on test set.
* Also the intercept (32) and coefficient (1.8) is printed.

## 2.'divergent_series.py', Ridge Regression Model with Polynomial
* The divergent series 1+2+3....N is given by the formula N(N+1)/2.
### Description:
* First for a given N, try to predict the Sum which is 100% accurate.
* Second for a given Sum, try to predict the N which is 99% accurate. Try with different degrees of the polynomial and plot them.

## 3. "stock_prediction.py", Support Vector Method
* To predict a stock or share value from csv data
### Description:
* First download the historical data from Nasdaq or other exchanges for a period of 5 or 3 years.
* For example, for google stock with symbol 'GOOG', the Nasdaq link is 'http://www.nasdaq.com/symbol/goog/historical'. Select the number of years to 3 or 5 and go to the end of the page and click the link 'Download this file in Excel Format'. Download and save the file as goog.csv
* Run the script followed by file name i.e. "stock_prediction.py goog.csv" and see the charts for price prediction, volume, rolling mean, rolling standard deviation or volatility.

## 4.'knn.py', K Nearest Neighbors Classifier
* To find the quadrant of any given x,y coordinates in 2d cartesian system.
### Description:
* A numpy array for angle theta from 0 to 360 degrees is created
* A numpy array for quandrant is created with values 1 to 4.
* A 2d numpy data array with cosine and sine values of theta are created.
* The data array is plotted with quadrant as colormap
* A KNN classifier is created with 6 neighbors.
* The KNN classifier is fit with data array againt quadrant array.
* Accuracy of the predictions are printed.

## 5.'digits_predict.py', MNIST prediction using KNN Classifier
* Scikit learn has a reduced version of the MNIST dataset and it is called digits. Each sample in this dataset is an 8x8 image representing a handwritten digit. Each pixel is represented by an integer in the range 0 to 16, indicating varying levels of black.
### Description:
* To import the digits dataset.
* To split the dataset into train and test data
* To apply KNN fit on the train data set
* To test the KNN score against the test data set and print the accuracy.
* Print the details of the dataset.
* Plot the 2D array of one image.



