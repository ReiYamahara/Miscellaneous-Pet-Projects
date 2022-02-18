import random
import numpy as np
import matplotlib.pyplot as plt


# how can I make the diamond_square algorithm faster...?
def diamond_square_algo(iterations = 6, k = 5):
    '''
    returns a 2d numpy array, z, using the diamond square algorithm.
    the dimensions of z have to be (2^n + 1, 2^n + 1) where n in the number of iterations

    parameter:
    iterations: the number of iterations (this determines the size of the numpy array)å
    k: roughness (a higher k value implies a rougher surface)
    '''
    pixels = 2 ** iterations + 1
    array = np.zeros((pixels, pixels))

    def random_uniform(a = -1, b = 1):
        return np.random.uniform(a, b)

    def random_normal(mean = 0, sigma = 1):
        return np.random.normal(mean, sigma)

    # random initialisation of the 4 points
    array[0][0] = np.random.uniform(-1, 1)
    array[-1][0] = np.random.uniform(-1, 1)
    array[0][-1] = np.random.uniform(-1, 1)
    array[-1][-1] = np.random.uniform(-1, 1)

    for iter in range(iterations):
        step = 2 ** (iterations - iter - 1)
        # diamond step:
        # we are going through every single point that is not 0: i represents the x-coordinate; j represents the y-coordinate
        for i in range(0, pixels - 1, step * 2):
            for j in range(0, pixels - 1, step * 2):
                array[i + step][j + step] = (array[i][j] + array[i + step*2][j] + array[i][j + step*2] + array[i + step*2][j + step*2])/4 + k * np.random.uniform(-1, 1)
        # square step:
        for i in range(0, pixels, step):
            for j in range(0, pixels, step):
                # we need a better condition...
                if array[i][j] == 0:
                    # at the edges, there are only three neighbouring points: a bit ugly but it does the job...
                    if i == 0:
                        array[i][j] = (array[i][j - step] + array[i][j + step] + array[i + step][j])/3 + k * np.random.uniform(-1, 1)
                    elif i == pixels - 1:
                        array[i][j] = (array[i][j - step] + array[i][j + step] + array[i - step][j])/3 + k * np.random.uniform(-1, 1)
                    elif j == 0:
                        array[i][j] = (array[i][j + step] + array[i - step][j] + array[i + step][j])/3 + k * np.random.uniform(-1, 1)
                    elif j == pixels - 1:
                        array[i][j] = (array[i][j - step] + array[i - step][j] + array[i + step][j])/3 + k * np.random.uniform(-1, 1)
                    else:
                        array[i][j] = (array[i][j - step] + array[i][j + step] + array[i - step][j] + array[i + step][j])/4 + k * np.random.uniform(-1, 1)
       
        # smaller random offset per iteration
        k /= 2
    return array

def fractal_landscape_plot(array, dpi = 200, background_colour = 'beige', view_init = [40, 30], 
view_dist = 7, cmap = 'Blues', save = False):
    '''
    '''
    pixels = array.shape[0]
    # np.mgrid creates a a coordinate system
    x, y = np.mgrid[0:pixels, 0:pixels]
    
    fig = plt.figure(dpi = dpi)
    ax = plt.axes(projection = '3d')
    ax.set_facecolor(background_colour)
    ax.axis('off')
    ax.view_init(view_init[0], view_init[1])
    ax.plot_surface(x, y, array, cmap = cmap)
    ax.dist = view_dist
    if save == True:
        plt.savefig('fractal_landscape.png')
    plt.show()

def cloud(z):
    plt.figure(dpi = 200)
    plt.imshow(z, cmap=plt.cm.Blues)
    plt.axis('off')
    plt.show()

array= diamond_square_algo(6, k = 10)
fractal_landscape_plot(array)