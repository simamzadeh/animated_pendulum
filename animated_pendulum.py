# Import modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

# Set constants
length = 5
amplitude = 150
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


# Defining a function to take the angle and return the x and y coordinates

def find_coordinates(angle):
    x_length = np.sin(angle * (np.pi / 180)) * 5
    y_length = np.cos(angle * (np.pi / 180)) * 5

    # gradient = y_length / x_length

    x_coord = 10 - x_length
    y_coord = 10 - y_length

    x_vals = [x_coord, 10]
    y_vals = [y_coord, 10]

    return x_vals, y_vals

# Plotting function

def plot_pendulum(angle):
    x_vals, y_vals = find_coordinates(angle)
    return plt.plot(x_vals, y_vals)


# Making time values

angles = []
displacements = []

timepoints = np.arange(0, 25, 0.25)
for t in timepoints:
    displacement = amplitude * np.cos((np.sqrt(g/length)) * t)

    # Reducing the amplitude by 5% each time
    # displacement = (amplitude * 0.95) * np.cos(np.sqrt(g/length) * t)
    # displacements.append(displacement)

    # angle = (np.sqrt(g/length)) * t
    angle = displacement/length
    angles.append(angle)


# Plot the pendulum
pendulum_line, = plot_pendulum(angle)


# Animation function

# angles = [30, 20, 10, 0, -10, -20, -30] # <<<< dummy list

def animate_pendulum(frame):
    x_vals, y_vals = find_coordinates(frame)
    pendulum_line.set_data(x_vals, y_vals)


# Adding limits to graph

plt.xlim(5, 15)
plt.ylim(4, 11)


# Calling the animation function

animation = FuncAnimation(plt.gcf(), animate_pendulum, frames = len(angles), repeat = True)

# Plotting the centre and end of the pendulum

plt.plot(10, 10, color = "y", marker = "*")
# plt.plot()

# Initial pendulum plot tests

# plt.plot(x_vals1, y_vals1)
# plt.plot(x_vals2, y_vals2)


plt.show()