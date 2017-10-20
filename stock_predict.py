#!/usr/bin/env python3
"""
To predict a stock value from the csv data.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from datetime import datetime, timedelta
from sys import argv

def fit(File, Years=2.5, Win=15):
    Date = datetime.now() - timedelta(days=Years*365)
    df = pd.read_csv(File)
    df = df.drop(0)
    df.date = pd.to_datetime(df.date, format="%Y/%m/%d")
    df = df[df.date > Date]
    df['days'] = pd.Series(data=np.arange(1,-len(df),-1))
    #df = df.drop(['close', 'open','high', 'low'], axis=1)
    X, x, Y, y = train_test_split(df[['days']], df.close, test_size=0.1)
    Reg = SVR(kernel = 'rbf', C= 1e3, gamma= 0.1)
    Reg.fit(X, Y)
    print(Reg.score(x,y))
    yp = Reg.predict(df[['days']])
    ppx = [i for i in range(30)]
    ppy = [Reg.predict([[i]]) for i in range(30)]
    plt.figure(figsize=(20,20))
    plt.subplot(2,2,1)
    plt.plot(df.days, df.close, 'r', df.days, yp, 'g', ppx, ppy, 'b')
    plt.legend(['close', 'predicted','future'])
    plt.title('day-close',fontsize='xx-large' )
    plt.subplot(2,2,2)
    plt.plot(df.days, df.volume, 'r')
    plt.title('volume',fontsize='xx-large' )
    plt.subplot(2,2,3)
    plt.plot(df.days, df.close.rolling(Win).mean(), 'r')
    plt.title('rolling mean', fontsize='xx-large')
    plt.subplot(2,2,4)
    plt.plot(df.days, df.close.rolling(Win).std(), 'b')
    plt.title('volatility - rolling std', fontsize='xx-large' )
    plt.show()

if len(argv) > 1:
    fit(argv[1]) # Your csv file in command line
else:
    fit('pdli.csv') # Your csv file in script
