# Import modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

# Set constants
length = 5
initial_amp = 150
g = 9.8


# Plot pendulum at 30 degrees - LINE 1

x_length1 = np.sin(30*(np.pi/180))*5
y_length1 = np.cos(30*(np.pi/180))*5
gradient1 = y_length1/x_length1

x_coord1 = 10 - x_length1
y_coord1 = 10 - y_length1

x_vals1 = [x_coord1, 10]
y_vals1 = [y_coord1, 10]

# Plot pendulum at 15 degrees - LINE 2

x_length2 = np.sin(15*(np.pi/180))*5
y_length2 = np.cos(15*(np.pi/180))*5
gradient2 = y_length2/x_length2

x_coord2 = 10 - x_length2
y_coord2 = 10 - y_length2

x_vals2 = [x_coord2, 10]
y_vals2 = [y_coord2, 10]


# # Defining a function to take the angle and return the x and y coordinates
#
# def find_coordinates(angle):
#

# timepoints = np.arange(x5, 15, 2)
# for t in timepoints:
#     displacement = 150*np.cos(np.sqrt(9.8/5))
#
#
# def time(angle):
#     x_vals = np.linspace(7.5, 10, data_points)
#     y_vals = (np.sqrt(g/length)) * (1/angle)
#     return x_vals, y_vals
#
#
# print(time(30))

# def length(angle):
#     return (9.8/(angle)**2) * 1/timepoints


#Plotting the graph
# plt.plot(x_vals, y_vals)

#Adding limits to graph
plt.xlim(5, 15)
plt.ylim(4, 11)

plt.plot(x_vals1, y_vals1)
plt.plot(x_vals2, y_vals2)
plt.show()