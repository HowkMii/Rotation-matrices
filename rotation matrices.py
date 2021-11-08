import numpy as np                     # Import numpy for array manipulation
import matplotlib.pyplot as plt        # Import matplotlib for charts
from utils_nb import plot_vectors      # Function to plot vectors (arrows)

R = np.array([[2, 0],
              [0, -2]])

x = np.array([[1, 1]])

y = np.dot(x, R) 
y

plot_vectors([x], axes=[4, 4], fname='transform_x.svg')	

plot_vectors([x, y], axes=[4, 4], fname='transformx_and_y.svg')