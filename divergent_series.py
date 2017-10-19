#!/usr/bin/env python3
"""
To predict the divergent series 1+2+3....N given by the formula N(N+1)/2.
First for a given N, try to predict the Sum which is 100% accurate.
Second for a given Sum, try to predict the N which is 99% accurate. Try with different degrees of the polynomial and plot them.
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

def fit_predict(In, Out, Degree=2):
    In = In.reshape(len(In),1)
    X, x, Y, y = train_test_split(In, Out, test_size=0.1)
    Reg = make_pipeline(PolynomialFeatures(Degree), Ridge())
    Reg.fit(X, Y)
    Score = Reg.score(x,y)
    P = Reg.predict(In)
    plt.plot(In, Out, 'b', In, P, 'r')
    plt.title("Score = %f, Degree= %d" %(Score,Degree))
    plt.show()

N = np.arange(0,1000)
Sum = N*(N+1)/2
print("Predict Sum for given N")
fit_predict(N, Sum)
print("\n\nPredict N for given Sum with different degrees of polynomial")
for n in range(2,6):
    fit_predict(Sum, N, Degree=n)

