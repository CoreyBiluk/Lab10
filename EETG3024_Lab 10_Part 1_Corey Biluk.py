# EETG 3024 Advanced Embedded Systems
# Instructor: Ricardo Bautista Quintero
# Corey Biluk | W0425561
# Lab 10 | Part 1
# March 8, 2021

# Import module
import matplotlib.pyplot as plt
# Create graph for [X values], [Y Values]
plt.plot ([0,1,2,3,4], [0,1,4,9,16]) 
# Label y axis
plt.ylabel ('Volts')
# Label X axis
plt.xlabel('Current')
# [Xmin, Xmax, Ymin, Ymax] for Axes
plt.axis([0, 4, 0, 16])
# Show graph on screen
plt.show()