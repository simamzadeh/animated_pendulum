# Import modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

# Set constants
length1 = 5
amplitude = 150
g = 9.8
length2 = 3

# Plot pendulum at 30 degrees - LINE 1

x_length1 = np.sin(30 * (np.pi / 180)) * 5
y_length1 = np.cos(30 * (np.pi / 180)) * 5
gradient1 = y_length1 / x_length1

x_coord1 = 10 - x_length1
y_coord1 = 10 - y_length1

x_vals1 = [x_coord1, 10]
y_vals1 = [y_coord1, 10]

# Plot pendulum at 15 degrees - LINE 2

x_length2 = np.sin(15 * (np.pi / 180)) * 5
y_length2 = np.cos(15 * (np.pi / 180)) * 5
gradient2 = y_length2 / x_length2

x_coord2 = 10 - x_length2
y_coord2 = 10 - y_length2

x_vals2 = [x_coord2, 10]
y_vals2 = [y_coord2, 10]


# Defining a function to take the angle and return the x and y coordinates

def find_coordinates(angle, length):
    x_length = np.sin(angle * (np.pi / 180)) * length
    y_length = np.cos(angle * (np.pi / 180)) * length

    # gradient = y_length / x_length # realised this was unnecessary

    x_coord = 10 - x_length
    y_coord = 10 - y_length

    x_vals = [x_coord, 10]
    y_vals = [y_coord, 10]

    return x_vals, y_vals, x_coord, y_coord

# Making time values

angles1 = []
angles2 = []

timepoints = np.arange(0, 25, 0.25)
for t in timepoints:
    # displacement = amplitude * np.cos((np.sqrt(g / length)) * t)

    # Reducing the amplitude by 5% each time
    amplitude = amplitude * 0.95
    displacement1 = amplitude * np.cos(np.sqrt(g / length1) * t)
    displacement2 = amplitude * np.cos(np.sqrt(g / length2) * t)

    angle1 = displacement1 / length1
    angles1.append(angle1)

    # PENDULUM 2
    angle2 = displacement2 / length2
    angles2.append(angle2)

# Plot the pendulum and endpoint
x_vals, y_vals, x_coord, y_coord = find_coordinates(angle1, length1)
pendulum1, = plt.plot(x_vals, y_vals)
endpoint1, = plt.plot(x_coord, y_coord, color="g", marker=".")

x_vals, y_vals, x_coord, y_coord = find_coordinates(angle2, length2)
pendulum2, = plt.plot(x_vals, y_vals)
endpoint2, = plt.plot(x_coord, y_coord, color="r", marker=".")

# Animation function for pendulum and endpoint

frames = len(angles1)

def animate_pendulum(frame, local_angles1, local_angles2):
    current_angle1 = local_angles1[frame]
    current_angle2 = local_angles2[frame]

    x_vals1, y_vals1, x_coord1, y_coord1 = find_coordinates(current_angle1, length1)
    x_vals2, y_vals2, x_coord2, y_coord2 = find_coordinates(current_angle2, length2)

    pendulum1.set_data(x_vals1, y_vals1)
    pendulum2.set_data(x_vals2, y_vals2)

    endpoint1.set_data(x_coord1, y_coord1)
    endpoint2.set_data(x_coord2, y_coord2)


# Adding limits to graph
plt.xlim(5, 15)
plt.ylim(4, 11)

# Calling the animation functions
pendulum_anim = FuncAnimation(plt.gcf(), animate_pendulum, frames=frames, repeat=True, fargs= [angles1, angles2])


# Plotting the centre and end of the pendulum
plt.plot(10, 10, color="y", marker="*")

# Showing our animation!
plt.show()
