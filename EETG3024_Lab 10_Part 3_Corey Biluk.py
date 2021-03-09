# EETG 3024 Advanced Embedded Systems
# Instructor: Ricardo Bautista Quintero
# Corey Biluk | W0425561
# Lab 10 | Part 3
# March 8, 2021

# Import Modules
import numpy as np
import matplotlib.pyplot as plt

# Create a figure object
fig = plt.figure()
# Create an object and configure for 3 axes graph
ax = plt.axes(projection="3d")
# returns evenly spaced values over a specified range (0 - 15, 1000 smaples generated in range)
z_line = np.linspace(0, 15, 1000)
# This takes z_line values and creates x_line values based on formula
x_line = np.exp(-0.1*z_line) * np.cos(z_line)
# This takes z_line values and creates y_line values based on formula
y_line = np.exp(-0.1*z_line) * np.sin(z_line)
# Creat a 3D graph for values of xlinf, yline, zline in red
ax.plot3D(x_line, y_line, z_line, 'red')
# Create label for X axis
ax.set_xlabel("x")
# Create label for Y axis
ax.set_ylabel("y")
# Create label for Z axis
ax.set_zlabel("z")
# Show graph on screen
plt.show()