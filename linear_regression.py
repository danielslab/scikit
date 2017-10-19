#!/usr/bin/env python3
"""
This test the linear regression for celcius to fahrenheit conversion:
    fahrenheit = celcius*1.8 + 32
"""
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def fit(In, Out, Title=''):
    In = In.reshape(len(In),1)
    x_train, x_test, y_train, y_test = train_test_split(In, Out, test_size=0.4)    # Split the test and train data
    regr = linear_model.LinearRegression()
    regr.fit(x_train,y_train)
    plt.axvline(0)
    plt.title(Title)
    plt.plot(In, Out, 'r')
    plt.show()
    print('Accuracy = %s, Intercept = %s, Coefficient = %s' %(regr.score(x_test,y_test), regr.intercept_, regr.coef_[0]))

Cel = np.arange(-40,40)    # Celcius Input Data
Fah = Cel*1.8 + 32    # Fahrenheit Output Data
fit(Cel, Fah, Title='Celcius to Fahrenheit')
fit(Fah, Cel, Title='Fahrenheit to Celcius')