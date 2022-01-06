import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from julia_and_mandelbrot_functions import *
from matplotlib.widgets import Slider
'''
iteration_array = julia_set_frames(x_pixels = 1000, iterations = 100)
fig, ax = plt.subplots(dpi = 100)
ax.axis('off')
iterations = len(iteration_array)
plt.imshow(iteration_array[iterations - 1], cmap = 'Blues')

ax_frames = plt.axes([0.25, 0.1, 0.65, 0.03])

slider_frames = Slider(ax_frames, 'number of iterations', 1, iterations - 1, valinit = iterations, valstep = 1)

def update(frame):
    ax.clear()
    ax.axis('off')
    ax.imshow(iteration_array[frame], cmap = 'Blues') 

slider_frames.on_changed(update)
plt.show();
'''
iteration_array = julia_set_frames(x_pixels = 100, iterations = 100)
fig, ax = plt.subplots(dpi = 100)
ax.axis('off')
iterations = len(iteration_array)
ims = []
for i in range(iterations):
    im = ax.imshow(iteration_array[i], animated = True, cmap = 'Blues')
    ims.append([im])
plt.show(ims[iterations - 1])
ax_frames = plt.axes([0.25, 0.1, 0.65, 0.03])

slider_frames = Slider(ax_frames, 'number of iterations', 1, iterations - 1, valinit = iterations, valstep = 1)

def update(frame):
    ax.clear()
    ax.axis('off')
    plt.show(ims[frame])

slider_frames.on_changed(update)
plt.show();