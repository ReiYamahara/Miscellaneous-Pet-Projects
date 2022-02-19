import random
import numpy as np
import matplotlib.pyplot as plt

def diamond_square_algo(iterations = 6, k = 2, m = 2, a = -1, b = 1, mean = 0, sigma = 1, random_distribution = 'uniform'):
    '''
    returns a 2d numpy array, array, using the diamond square algorithm.
    the dimensions of array have to be (2^n + 1, 2^n + 1) where n in the number of iterations

    parameter:
    iterations: the number of iterations (this determines the size of the numpy array)å
    k: initial roughness (a higher k value implies a rougher initial surface)
    m: roughness (a lower a value implies a rougher surface)
    '''
    pixels = 2 ** iterations + 1
    array = np.zeros((pixels, pixels))

    def randomiser(random_distribution = random_distribution, a = a, b = b, mean = mean, sigma = sigma):
        if random_distribution == 'uniform':
            return np.random.uniform(a, b)
        elif random_distribution == 'normal':
            return np.random.normal(mean, sigma)

    # random initialisation of the 4 points
    array[0][0] = randomiser()
    array[-1][0] = randomiser()
    array[0][-1] = randomiser()
    array[-1][-1] = randomiser()

    for iter in range(iterations):
        step = 2 ** (iterations - iter - 1)

        # diamond step:

        # vectorised version: z00, z10, z01, z11 represent the 4 surrounding points
        z00 = array[:pixels - step * 2:step * 2, :pixels - step * 2:step * 2]
        z10 = array[:pixels - step * 2:step * 2, step * 2::step * 2]
        z01 = array[step * 2::step * 2, :pixels - step * 2:step * 2]
        z11 = array[step * 2::step * 2, step * 2::step * 2]
        array[step::step * 2, step::step * 2] = (z00 + z10 + z01 + z11)/4 + k * randomiser()

        # sqaure step: vectorised version:

        # tackling the edges: each starting variable represents the edge: left edge, right edge, top edge, bottom edge
        array[0, step::step * 2] = (array[0, :- step * 2:step * 2] + array[0, step * 2::step * 2] + array[step, step::step * 2])/3 + k * randomiser()
        array[-1, step::step * 2] = (array[-1, :- step * 2:step * 2] + array[-1, step * 2::step * 2] + array[-step, step::step * 2])/3 + k * randomiser()
        array[step::step * 2, 0] = (array[:-step * 2: step * 2, 0] + array[step * 2:: step * 2, 0] + array[step::step * 2, step])/3 + k * randomiser()
        array[step::step * 2, -1] = (array[:-step * 2: step * 2, -1] + array[step * 2:: step * 2, -1] + array[step::step * 2, -step])/3 + k * randomiser()

        # tackling the non-edges: split into the odd row values and the odd column values
        # there are no non-edge points on the first iteration
        if iter != 0:
            # the 4 points surrounding the odd row values that is not the edge
            pr0 = array[:-step * 2: step * 2, step * 2:-step * 2:step * 2]
            pr1 = array[step * 2:: step * 2, step * 2:-step * 2:step * 2]
            pr2 = array[step::step * 2, step: - step * 3:step * 2]
            pr3 = array[step::step * 2, step * 3: - step:step * 2]

            # the variable represents the odd row values that needs to be filled that is not the edge
            array[step::step * 2, ::step * 2][:,1:-1] = (pr0 + pr1 + pr2 + pr3)/4 + k * randomiser()

            # the 4 points surrounding the odd column values that is not the edge
            pz0 = array[step: - step * 3:step * 2, step::step * 2]
            pz1 = array[step * 3:- step:step * 2, step::step * 2]
            pz2 = array[step * 2:-step * 2:step * 2, : -step * 2:step * 2]
            pz3 = array[step * 2:-step * 2:step * 2, step * 2::step * 2]

            # the variable represents the odd columns values that needs to be filled that is not the edge
            array[::step * 2, step::step * 2][1:-1] = (pz0 + pz1 + pz2 + pz3)/4 + k * randomiser()

        # the offset becomes smaller for every iteration
        k = k / m
    return array


def classic_noise(x_integers = 3, y_integers = 3, num_pixels_per_integer = 20, seed = 0):
    '''
    returns a 2d numpy array, array, using the classic noise algorithm (also known as Perlin noise)
    the dimensions of the array is x_pixels * y_pixels

    parameters:
    x_integers: the number of x coordinate integers
    y_integers: the number of y coordinate integers
    num_pixels_per_integer: the number of pixels per integer
    seed: seed
    '''
    np.random.seed(seed)

    def blending_function(x):
        return 6 * x**5 - 15 * x**4 + 10 * x**3

    def linear_interpolation(a, b, x):
        return a + x * (b - a)

    x_pixels = x_integers * num_pixels_per_integer
    y_pixels = y_integers * num_pixels_per_integer
    x, y = np.mgrid[0:x_pixels, 0:y_pixels] / num_pixels_per_integer

    # needs to be int not float!!!
    i = x.astype(int) # equivalent to flooring and then changing to int
    j = y.astype(int)
    u, v = x - i, y - j

    # randomising the vectors:
    vector_array = np.random.uniform(-1, 1, (x_integers * y_integers, 2))
    length_array = ((vector_array[:, 0] ** 2 + vector_array[:, 1] ** 2) ** (1/2)).reshape(x_integers * y_integers, 1)
    # all the vectors randomised
    v_standard = (vector_array / length_array)
    random_nums = np.arange(x_pixels * y_pixels, dtype = int)
    np.random.shuffle(random_nums)

    # calculating the vectors of each integer coordinate
    g00 = v_standard[random_nums[random_nums[i] + j] % (x_integers * y_integers)]
    g10 = v_standard[random_nums[random_nums[i + 1] + j] % (x_integers * y_integers)]
    g01 = v_standard[random_nums[random_nums[i] + j + 1] % (x_integers * y_integers)]
    g11 = v_standard[random_nums[random_nums[i + 1] + j + 1] % (x_integers * y_integers)]

    n00 = g00[:, :, 0] * u + g00[:, :, 1] * v
    n10 = g10[:, :, 0] * (u - 1) + g10[:, :, 1] * v
    n01 = g01[:, :, 0] * u + g01[:, :, 1] * (v - 1)
    n11 = g11[:, :, 0] * (u - 1) + g11[:, :, 1] * (v - 1)

    f_u, f_v = blending_function(u), blending_function(v)

    x1 = linear_interpolation(n00, n10, f_u)
    x2 = linear_interpolation(n01, n11, f_u)
    array = linear_interpolation(x1, x2, f_v)
    return array


def fractal_landscape_plot(array, dpi = 200, background_colour = 'grey', view_init = [40, 30], 
view_dist = 7, cmap = 'Blues', save = False):
    '''
    plots 3d landscape
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
        plt.savefig('classic_noise.png')
    plt.show()

def cloud(array):
    plt.figure(dpi = 200)
    plt.imshow(array, cmap=plt.cm.Blues)
    plt.axis('off')
    plt.show()

# array = diamond_square_algo(6, m = 2.5)
array = classic_noise(num_pixels_per_integer = 50)
fractal_landscape_plot(array)