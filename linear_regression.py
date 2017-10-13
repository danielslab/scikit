"""
This test the linear regression for celcius to fahrenheit conversion:
    fahrenheit = celcius*1.8 + 32
"""
#!/usr/bin/env python3
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split

data = np.arange(1,21).reshape(20,1)    # Celcius Input Data
target = data*1.8 + 32    # Fahrenheit Output Data
x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.4)    # Split the test and train data
regr = linear_model.LinearRegression()
regr.fit(x_train,y_train)
print('Accuracy =',regr.score(x_test,y_test),'\n'
      'Intercept =', regr.intercept_,'\n'
      'Coefficient =', regr.coef_)
