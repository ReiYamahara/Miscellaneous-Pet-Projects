import random
import numpy as np
import matplotlib.pyplot as plt

def random_uniform(): # alter the range of the uniform to change the roughness of the terrain
    return 2 ** (-random.uniform(0.8, 1))

def rand(iter):
    return random.uniform(-0.5, 0.5) * random_uniform() ** iter

# how can I make the diamond_square algorithm faster...?
def diamond_square_algo(iterations = 6):
    '''
    returns a 2d numpy array, z, using the diamond square algorithm.
    the dimensions of z have to be (2^n + 1, 2^n + 1) where n in the number of iterations

    parameter:
    iterations: the number of iterations (this determines the size of the numpy array)å
    '''
    pixels = 2 ** iterations + 1
    z = np.zeros((pixels, pixels))

    # random initialisation of the 4 points
    z[0][0] = rand(0)
    z[pixels - 1][0] = rand(0)
    z[0][pixels - 1] = rand(0)
    z[pixels - 1][pixels - 1] = rand(0)

    for iter in range(iterations):
        step = 2 ** (iterations - iter - 1)
        # diamond step
        for i in range(0, pixels - 1, step * 2):
            for j in range(0, pixels - 1, step * 2):

                z[i + step][j + step] = (z[i][j] + z[i + step*2][j] + z[i][j + step*2] + z[i + step*2][j + step*2])/4 + rand(iter)

        # square step
        for i in range(pixels):
            for j in range(pixels):
                # we need a better condition...
                # if i % step == 0 and j % step == 0
                if z[i][j] == 0 and i % step == 0 and j % step == 0:
                    # at the edges, there are only three neighbouring points
                    if i == 0:
                        z[i][j] = (z[i][j - step] + z[i][j + step] + z[i + step][j])/3 + rand(iter)
                    elif i == pixels - 1:
                        z[i][j] = (z[i][j - step] + z[i][j + step] + z[i - step][j])/3 + rand(iter)
                    elif j == 0:
                        z[i][j] = (z[i][j + step] + z[i - step][j] + z[i + step][j])/3 + rand(iter)
                    elif j == pixels - 1:
                        z[i][j] = (z[i][j - step] + z[i - step][j] + z[i + step][j])/3 + rand(iter)
                    else:
                        z[i][j] = (z[i][j - step] + z[i][j + step] + z[i - step][j] + z[i + step][j])/4 + rand(iter)
    return z, pixels

def fractal_landscape_plot(z, pixels, dpi = 200, background_colour = 'beige', view_init = [40, 30], 
view_dist = 7, cmap = 'Blues', save = False):
    '''
    '''
    # np.mgrid creates a a coordinate system
    x, y = np.mgrid[0:pixels, 0:pixels]
    
    fig = plt.figure(dpi = dpi)
    ax = plt.axes(projection = '3d')
    ax.set_facecolor(background_colour)
    ax.axis('off')
    ax.view_init(view_init[0], view_init[1])
    ax.plot_surface(x, y, z, cmap = cmap)
    ax.dist = view_dist
    if save == True:
        plt.savefig('fractal_landscape.png')
    plt.show()

def cloud(z):
    plt.figure(dpi = 200)
    plt.imshow(z, cmap=plt.cm.Blues)
    plt.axis('off')
    plt.show()

z, pixels = diamond_square_algo(10)
cloud(z)