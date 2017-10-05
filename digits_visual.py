# Import necessary modules
from sklearn import datasets
import matplotlib.pyplot as plt

# Load the digits dataset: digits
digits = datasets.load_digits()

# Print the DESCR and Keys of the dataset
print(digits.DESCR)
print(digits.keys())

# Print the shape of the images and data keys
print(digits.images.shape)
print(digits.data.shape)

# Display digit 1010
plt.imshow(digits.images[920], cmap=plt.cm.copper, interpolation='nearest')
plt.show()
