import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt

pixels = 1000
num_feature_points = 4
x, y = np.mgrid[0:pixels, 0:pixels] / pixels
z = np.ones((pixels, pixels))
np.random.seed(3)
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

# k represents how much the feature point moves
k = 5
random_vectors_possibilities = np.array([[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]])

# where we store each final z
test = []

ims = []
fig, ax = plt.subplots(dpi = 200)
ax.axis('off')

for i in range(100):
    # going through each point, calculating the closest feature point to each point and noting that distance.
    for feature_point in feature_points:
        # could define a function that finds the euclidean distance between all the coordinates and the feature point...?
        z = np.fmin(((x - feature_point[0])**2 + (y - feature_point[1])**2)**(1/2), z)

    # adding the finished distance values to ims  
    test.append(z)

    # changing the value of the feature points - using brownian motion
    a = np.random.choice(8, feature_points.shape[0])
    random_vectors = random_vectors_possibilities[a]
    feature_points = (feature_points + random_vectors / pixels)* k
    # possible issue: the feature point may not be within the frame

for i in range(100): # from 1 to iteration + 1 because array is a zero array    
    plt.clf() # clears the figure
    plt.figure(1, dpi = 100)
    plt.imshow(test[i], cmap = 'gray', interpolation = 'None')
    plt.axis("off")
    plt.pause(1/2)
plt.show();
# binary, gray
# plt.scatter(feature_points[:, 1] * pixels, feature_points[:, 0] * pixels, linewidths = 1)

'''anim = animation.ArtistAnimation(fig, ims, interval = 50, blit = True, repeat_delay = 100)
plt.show();'''