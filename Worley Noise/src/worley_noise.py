import numpy as np
import matplotlib.pyplot as plt

def worley_noise(pixels = 400, num_feature_points = 16):
    '''
    returns an array using the worley noise algorithm

    parameters:
    pixels: number of pixels on each coordinate
    num_feature_points: number of feature points
    '''
    x, y = np.mgrid[0:pixels, 0:pixels] / pixels
    z = np.ones((pixels, pixels))

    # we will use some kind of box randomiser (not quite sure what the name is so I gave it one myself)
    # we will create a grid within the frame and each feature point is put inside each grid - its position within the grid is completely random
    # note that because of this, it is desirable to have square number of feature points
    # we have chosen this method of randomisation since we do not want any feature point being too close to another feature point

    # num_of_grids is the number of boxes in each axis
    num_of_grids = int(num_feature_points**(1/2))

    # step is the number of pixels between each grid point
    step = int(pixels / num_of_grids)
    a = np.array([step * x for x in range(num_of_grids)])
    grid_feature_points_x = np.random.randint([a for i in range(num_of_grids)], [a + int(pixels/num_of_grids) for i in range(num_of_grids)]) / pixels
    grid_feature_points_y = (np.random.randint([a for i in range(num_of_grids)], [a + int(pixels/num_of_grids) for i in range(num_of_grids)]) / pixels).T
    grid_feature_points_x = grid_feature_points_x.reshape(num_of_grids**2, 1)
    grid_feature_points_y = grid_feature_points_y.reshape(num_of_grids**2, 1)
    grid_feature_points = np.concatenate((grid_feature_points_x, grid_feature_points_y), axis = 1)

    # the leftover points can go wherever they want - completely randomised
    # preferably, we'd want no leftover points since it could result in feature points being too close together.
    num_leftover_points = num_feature_points - num_of_grids**2
    leftover_feature_points = np.random.randint(pixels, size = (num_leftover_points, 2)) / pixels

    #feature_points include all the feature points
    feature_points = np.concatenate((grid_feature_points, leftover_feature_points))

    # going through each point, calculating the closest feature point to each point and noting that distance.
    for feature_point in feature_points:
        # could define a function that finds the euclidean distance between all the coordinates and the feature point...?
        z = np.fmin(((x - feature_point[0])**2 + (y - feature_point[1])**2)**(1/2), z)
        # what if I use the second closest feature point?
    
    return z

def imshow(array, dpi = 200, cmap = 'gray', save = False, name = 'plt.png'):
    plt.figure(dpi = dpi)
    plt.imshow(array, cmap = cmap)
    plt.axis('off')
    if save == True:
        plt.savefig(name)
    plt.show()

z = worley_noise()
imshow(z)
