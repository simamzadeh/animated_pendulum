# Import modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

# Set constants
length = 5
initial_amp = 150
g = 9.8


# Plot pendulum at 30 degrees

x_length = np.sin(30*(np.pi/180))*5
y_length = np.cos(30*(np.pi/180))*5
gradient = y_length/x_length

x_coord = 10 - x_length
y_coord = 10 - y_length

x_vals = [x_coord, 10]
y_vals = [y_coord, 10]


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

plt.plot(x_vals, y_vals)
plt.show()