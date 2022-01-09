import numpy as np
import matplotlib.pyplot as plt

def julia_set_frames_3d(c = 0.28 + 0.008j, x_pixels = 1000, limits = [-2, 2, -4/3, 4/3], iterations = 30):
    '''
    '''
    if c == 0:
        limits = [-2, 1.5, -7/6, 7/6]
    y_pixels = round(x_pixels * ((limits[3] - limits[2])/(limits[1 ]- limits[0])))
    x = np.linspace(limits[0], limits[1], x_pixels)
    y = np.linspace(limits[2], limits[3], y_pixels)
    X, Y = np.meshgrid(x, y)

    iteration_array = np.zeros((iterations, y_pixels, x_pixels)) # np.zeros allows floats

    Z = X + Y * 1j
    if c == 0:
        c = Z
    def f(Z): # scaling for each recursion (reduces deviation between output values)
        return np.e**(-np.abs(Z))

    for i in range(iterations):
        Z = Z ** 2 + c
        iteration_array[i] = f(Z)

    return X, Y, iteration_array

def plot_3d_julia_frame(X, Y, iteration_array, frame = 20,  dpi = 200, view = [35, 72], mountain = True, plot_type = 'meshplot', face_colour = [0.1, 0, 0], cmap = 'pink'):
    '''
    '''
    fig = plt.figure(dpi = dpi) # set 3D figure environment
    ax = plt.axes(projection = '3d')
    ax.set_zlim(-2, 2)
    ax.view_init(view[0], view[1]) # view orientation (elevation angle, horizontal angle)
    ax.dist = 5 # viewpoint distance
    ax.set_facecolor(face_colour) # background colour
    ax.axis("off")
    if mountain == False:
        iteration_array = - iteration_array

    if plot_type == 'meshplot':
            ax.plot_surface(X, Y, iteration_array[frame - 1], rstride = 1, cstride = 1, cmap = cmap)
    elif plot_type == 'contourplot':
        ax.contourf3D(X, Y, iteration_array[frame - 1], 2*frame, cmap = cmap)
        
    plt.show();
