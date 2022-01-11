import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# a and b are parameters
# c and d are constants
theta = np.linspace(0, 2*np.pi, 100)
theta, phi = np.meshgrid(theta, theta)
c, d = 2, 1
num_points = len(theta)

# x, y, z are 2d matrices of shape theta * theta. (x[0][0], y[0][0], z[0][0]) is one coordinate of the torus.
x = (c + d * np.cos(theta)) * np.cos(phi)
y = (c + d * np.cos(theta)) * np.sin(phi)
z = d * np.sin(theta)

# define a rotation matrix around an axis
a = 0.5
rotation_matrix_x = np.array([[1.0, 0, 0], 
                    [0, np.cos(a), np.sin(a)], 
                    [0, np.sin(a), np.cos(a)]])

# mesh_array is a (3, num_points, num_points) matrix
mesh_array = np.array([x, y, z])
# converting into coordinates: a  matrix of shape (num_points**2, 3)
coordinate_array = mesh_array.T.reshape(-1, 3)
# applying the rotation_matrix onto the coordinate_array: rotated_array is of shape (num_points**2, 3)
rotated_array = np.dot(coordinate_array, rotation_matrix_x) # nor sure how this works actually...
# converting it back into a matrix of shape 
rotated_mesh_array = rotated_array.T.reshape(3, num_points, num_points)
# then apply multiply with the rotation matrix (3, num_points, num_points) so that we can plot it using plot_surface

fig = plt.figure(figsize = (5,5), dpi = 200)
ax = plt.axes(projection = '3d')
ax.view_init(36, 26)
ax.set_facecolor([0.2, 0, 0]) # background colour
ax.set_zlim(-3,3)
ax.set_ylim(-3,3)
ax.dist = 10
ax.axis('off')
plots = []
for i in range(5):
        # mesh_array is a (3, num_points, num_points) matrix
    mesh_array = np.array([x, y, z])
    # converting into coordinates: a  matrix of shape (num_points**2, 3)
    coordinate_array = mesh_array.T.reshape(-1, 3)
    # applying the rotation_matrix onto the coordinate_array: rotated_array is of shape (num_points**2, 3)
    rotated_array = np.dot(coordinate_array, rotation_matrix_x) # nor sure how this works actually...
    # converting it back into a matrix of shape 
    rotated_mesh_array = rotated_array.T.reshape(3, num_points, num_points)
    # then apply multiply with the rotation matrix (3, num_points, num_points) so that we can plot it using plot_surface

    plot = ax.plot_surface(rotated_mesh_array[0], rotated_mesh_array[1], rotated_mesh_array[2], animated = True, rstride = 3, cstride = 2, cmap = 'pink')
    plots.append([plot])
    
anim = animation.ArtistAnimation(fig, plots, interval = 10, blit = True, repeat_delay = 10)

plt.show();