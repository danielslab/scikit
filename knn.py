#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 1000)  #Create array for theta from 0 to 360 degrees
quadrant = np.ones(1000, dtype=int)    #Create array for four quandrants and fill with 1
quadrant[250:500] = [2]*250            #Assign value for 2nd quadrant
quadrant[500:750] = [3]*250            #Assign value for 3rd quadrant
quadrant[750:] = [4]*250               #Assign value for 4th quadrant
data = np.empty((1000,2))              #Create data array with 2 columns and 1000 rows
data[:,0] = np.cos(theta)              #Assign first column with cosine(theta)
data[:,1] = np.sin(theta)              #Assign second column with sine(theta)
plt.scatter(data[:,0], data[:,1], c=quadrant) #Plot x, y with colormap as quadrant
plt.colorbar()
plt.show()

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data, quadrant, test_size=0.2, stratify=quadrant)
knn = KNeighborsClassifier(n_neighbors=8)
knn.fit(x_train, y_train)
print('Accuracy =',knn.score(x_test,y_test))