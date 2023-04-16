# Prompt:

'''
Write a program in Python that generates 100 random numbers,
arranges them into a 10x10 matrix and generates a viridis heatmap,
without numeric values.
'''


import numpy as np
import matplotlib.pyplot as plt

# Generate 100 random numbers between 0 and 1
data = np.random.rand(100)

# Reshape the data into a 10x10 matrix
data = data.reshape((10, 10))

# Create a figure and axes for the heatmap
fig, ax = plt.subplots()

# Generate the heatmap using the Viridis colormap
im = ax.imshow(data, cmap='viridis')

# Remove the x and y ticks
ax.set_xticks([])
ax.set_yticks([])

# Remove the numeric values on the colorbar
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_yticklabels([])

# Show the heatmap
plt.show()