#!/usr/bin/env python3
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Split into training and test set
digits = datasets.load_digits()
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size =0.2, random_state=42, stratify=digits.target)

# Create a k-NN classifier with 7 neighbors:
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train, y_train)

# Print the accuracy
print('Accuracy =', knn.score(x_test, y_test))