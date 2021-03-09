# EETG 3024 Advanced Embedded Systems
# Instructor: Ricardo Bautista Quintero
# Corey Biluk | W0425561
# Lab 10 | Part 2
# March 8, 2021

# Import Modules
import numpy as np
import matplotlib.pyplot as plt

# This function takes a number as input and returns the result of the equation
def math_fun(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

# Arange returns values from 0.0 - 5.0 at 0.1 increments
t1 = np.arange(0.0, 5.0, 0.1)
# Arange returns values from 0.0 - 5.0 at 0.02 increments
t2 = np.arange(0.0, 5.0, 0.02)

# Creates a new figure/window
plt.figure(1)

# This creates a subplot (row 2, column 1, index 1)
plt.subplot(211)
# plot values (x1 value, y1 value, format - red plus marker, x2 value, y2 value, format - black) 
plt.plot(t1, math_fun(t1), 'r+', t2, math_fun(t2), 'k')
# Configures the grid lines
plt.grid()

# This creates a subplot (row 2, column 1, index 2)
plt.subplot(212)
# Plot values (x1 value, y2 value, format - blue dashed line)
plt.plot(t2, np.cos(2*np.pi*t2), 'b--')
# Configures the grid lines
plt.grid()
# Show graph on screen
plt.show()