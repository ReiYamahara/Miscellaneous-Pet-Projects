import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

def julia_set_frames_3d(c = 0.28 + 0.008j, x_pixels = 1000, limits = [-2, 2, -4/3, 4/3], iterations = 30):
    '''
    '''
    if c == 0:
        limits = [-2, 1.5, -7/6, 7/6]
    y_pixels = round(x_pixels * ((limits[3] - limits[2])/(limits[1 ]- limits[0])))
    x = np.linspace(limits[0], limits[1], x_pixels, dtype = np.float128)
    y = np.linspace(limits[2], limits[3], y_pixels, dtype = np.float128)
    X, Y = np.meshgrid(x, y)

    iteration_array = np.zeros((iterations, y_pixels, x_pixels), dtype = np.float128) # np.zeros allows floats

    Z = X + Y * 1j
    if c == 0:
        c = Z
    def f(Z): # scaling for each recursion (reduces deviation between output values)
        return np.e **(-np.abs(Z))

    for i in range(iterations):
        Z = Z ** 2 + c
        iteration_array[i] = f(Z)

    return X, Y, iteration_array

def julia_set_3d_landscape(X, Y, iteration_array, frame = 20,  dpi = 200, view = [35, 72], distance = 5, mountain = True, 
plot_type = 'meshplot', face_colour = [0.1, 0, 0], cmap = 'pink'):
    '''
    '''
    fig = plt.figure(dpi = dpi) # set 3D figure environment
    ax = plt.axes(projection = '3d')
    ax.set_zlim(-2, 2)
    ax.view_init(view[0], view[1]) # view orientation (elevation angle, horizontal angle)
    ax.dist = distance # viewpoint distance
    ax.set_facecolor(face_colour) # background colour
    ax.axis("off")
    if mountain == False:
        iteration_array = - iteration_array

    if plot_type == 'meshplot':
            ax.plot_surface(X, Y, iteration_array[frame - 1], rstride = 1, cstride = 1, cmap = cmap)
    elif plot_type == 'contourplot':
        ax.contourf3D(X, Y, iteration_array[frame - 1], 2*frame, cmap = cmap)
        
    plt.show();

def julia_set_3d_landscape_animation(X, Y, iteration_array, dpi = 200, view = [35, 72], distance = 5, mountain = True, 
plot_type = 'meshplot', face_colour = [0.1, 0, 0], cmap = 'pink', interval = 300, repeat_delay = 0):
    '''
    '''
    fig = plt.figure(dpi = dpi) # set 3D figure environment
    ax = plt.axes(projection = '3d')
    ax.set_zlim(-2, 2)
    ax.view_init(view[0], view[1]) # view orientation (elevation angle, horizontal angle)
    ax.dist = distance # viewpoint distance
    ax.set_facecolor(face_colour) # background colour
    ax.axis('off')
    ims = []
    for i in range(len(iteration_array)):
        im = ax.plot_surface(X, Y, iteration_array[i], animated = True, cmap = cmap)
        ims.append([im])
    anim = animation.ArtistAnimation(fig, ims, interval = interval, blit = True, repeat_delay = repeat_delay)
    plt.show();

X, Y, iteration_array = julia_set_frames_3d(c = 0, x_pixels = 1000, iterations =30)
julia_set_3d_landscape_animation(X, Y, iteration_array)

