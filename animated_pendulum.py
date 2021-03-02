#Import modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

#Set constants
length = 5
initial_amp = 150

#Make initial values for line
# x_vals = np.linspace(7.5, 10, length)
# y_vals = np.ones(length)*5.5
x_vals = [7.5, 10]
y_vals = [5.5, 10]


#Plotting the graph
plt.plot(x_vals, y_vals)

#Adding limits to graph
plt.xlim(5, 15)
plt.ylim(4, 11)

plt.plot(x_vals, y_vals)
plt.show()