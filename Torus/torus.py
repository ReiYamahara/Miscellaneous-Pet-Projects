import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# a and b are parameters
# c and d are constants
def donut_shape(num_points = 100, donut_radius = 3, hole_radius = 1):
    '''
    calculates the coordinates of a donut (also known as a torus)

    parameters:
    num_points: the number of points for theta
    donut_radius: the radius of the entire donut
    hole_radius: the radius of the hole of the donut

    returns a meshgrid, a 2d numpy array for the x, y and z coordinates
    '''
    c = donut_radius
    d = hole_radius
    theta = np.linspace(0, 2*np.pi, num_points)
    theta, phi = np.meshgrid(theta, theta)

    # x, y, z are 2d matrices of shape theta * theta. (x[0][0], y[0][0], z[0][0]) is one coordinate of the torus.
    x = (c + d * np.cos(theta)) * np.cos(phi)
    y = (c + d * np.cos(theta)) * np.sin(phi)
    z = d * np.sin(theta)
    return x, y, z

def rotation_matrix(num_points = 100, axis = 'x'):
    '''
    gives the rotation matrix around a certain an axis over a certain number of degrees (angle)
    
    parameters:
    num_points: number of points for theta
    axis: rotation matrix around a certain axis in 3D (can take values of 'x', 'y' or 'z')

    returns a rotation matrix around an axis (dtype = 3 by 3 numpy array)
    '''
    a = (2 * np.pi)/100
    rotation_matrix_x = np.array([[1.0, 0, 0], 
                                [0, np.cos(a), -np.sin(a)], 
                                [0, np.sin(a), np.cos(a)]])

    rotation_matrix_y = np.array([[np.cos(a), 0, np.sin(a)], 
                                [0, 1, 0], 
                                [-np.sin(a), 0, np.cos(a)]])

    rotation_matrix_z = np.array([[np.cos(a), -np.sin(a), 0], 
                                [np.sin(a), np.cos(a), 0], 
                                [0, 0, 1]])
    if axis == 'x':
        return rotation_matrix_x
    elif axis == 'y':
        return rotation_matrix_y
    elif axis == 'z':
        return rotation_matrix_z

def rotate_3d_shape_animation(x, y, z, rotation_matrix, dpi = 200, view_position = [36, 26], 
background_colour = [0.2, 0, 0], ax_dist = 10, rstride = 3, cstride = 3, cmap = 'pink',
interval = 10, repeat_delay = 0, plot_type = 'meshplot'):
    '''
    gives an animation of the rotation of a 3d shape (e.g. torus/donut)

    parameters:
    x, y, z: each is a 2d numpy array from the function donut_shape 
    rotation_matrix: the rotation matrix around a certain axis over a certain number of degrees
    dpi: dots per inches
    view_position: camera position: [elevation angle, horizontal angle] (dtype: list)
    background_colour: background colour of the animation (recommended: [0, 0, 0], 'beige', 'grey', 'darkblue', 'maroon')
    ax_dist: distance between the camera and the plot
    rstride: if this is too high, the plot becomes slower...
    cstride:
    cmap: colour map (recommended: 'pink')
    interval: milliseconds per frame (dtpe = int)
    repeat_delay: the delay in milliseconds between consecutive animation runs (dtype = int)
    plot_type: choose between 'meshplot', 'wireplot' and 'contourplot' (which is in progress...) 

    returns an animated plot of the rotation of the 3D object
    '''
    num_points = x.shape[0]
    fig = plt.figure(figsize = (5,5), dpi = dpi)
    ax = plt.axes(projection = '3d')
    ax.view_init(view_position[0], view_position[1])
    ax.set_facecolor(background_colour) # background colour
    ax.set_zlim(-3,3)
    ax.set_ylim(-3,3)
    ax.dist = 10
    ax.axis('off')
    plots = []

    # mesh_array is a (3, num_points, num_points) matrix
    mesh_array = np.array([x, y, z])
    for i in range(50):
        # converting into coordinates: a  matrix of shape (num_points**2, 3)
        coordinate_array = mesh_array.T.reshape(-1, 3)
        # applying the rotation_matrix onto the coordinate_array: rotated_array is of shape (num_points**2, 3)
        rotated_array = np.dot(coordinate_array, rotation_matrix) # nor sure how this works actually...
        # converting it back into a matrix of shape 
        mesh_array = rotated_array.T.reshape(3, num_points, num_points)
        # then apply multiply with the rotation matrix (3, num_points, num_points) so that we can plot it using plot_surface
        if plot_type == 'meshplot':
            plot = ax.plot_surface(mesh_array[0], mesh_array[1], mesh_array[2], animated = True, 
            rstride = rstride, cstride = cstride, cmap = cmap, shade = True, lightsource = False)
        elif plot_type == 'wireplot':
            plot = ax.plot_wireframe(mesh_array[0], mesh_array[1], mesh_array[2], animated = True, 
            rstride = rstride, cstride = cstride, cmap = cmap)
        elif plot_type == 'contourplot':
            plot = ax.contourf3D(mesh_array[0], mesh_array[1], mesh_array[2])
            # AttributeError: 'QuadContourSet' object has no attribute 'set_visible'...????

        plots.append([plot])
    
    anim = animation.ArtistAnimation(fig, plots, interval = interval, blit = True, repeat_delay = repeat_delay)
    plt.show();

# make into gif
# different plot style: try and get contourf3D to work...
# try different shapes (klein bottle? mobius strip...?)

x, y, z = donut_shape()
rotate_3d_shape_animation(x, y, z, rotation_matrix(), plot_type = 'wireplot')