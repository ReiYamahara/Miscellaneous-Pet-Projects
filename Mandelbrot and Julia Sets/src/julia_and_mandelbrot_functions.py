import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def julia_set_frames(c = 0.28 + 0.008j, x_pixels = 1000, iterations = 30):
    '''
    creates a frame for each iteration of the julia set function and stores it in a numpy array
    use c = 0 to get the mandelbrot set

    parameters:
    c: constant - a complex number (dtype = class 'complex')
    x_pixels: number of x-ordinate pixels (dtype = int)
    iterations: number of iterations (dtype = int)

    returns a numpy array within a numpy array with shape (iterations, number of y pixels, number of x pixels)
    '''
    if c == 0:
        y_pixels = round((2/3) * x_pixels)
        x = np.linspace(-2, 1.5, x_pixels) # get 3:2 ratio because it looks good 
        y = np.linspace(-7/6, 7/6, y_pixels) * 1j
        complex_array = x + y.reshape(y_pixels, 1) # broadcasting to create the complex array
        iteration_array = np.full((iterations, y_pixels, x_pixels), iterations)
        c = complex_array
    else:
        y_pixels = round((2/3) * x_pixels)
        x = np.linspace(-2, 2, x_pixels) # get 3:2 ratio because it looks good 
        y = np.linspace(-4/3, 4/3, y_pixels) * 1j
        complex_array = x + y.reshape(y_pixels, 1) # broadcasting to create the complex array
        iteration_array = np.full((iterations, y_pixels, x_pixels), iterations) # creating the numpy array to map the numbers onto

    for i in range(iterations): # from 1 to iteration + 1 because array is a zero array
        if i == 0:
            complex_array = complex_array ** 2 + c
            condition = (abs(complex_array) >= 2)
            iteration_array[i][condition] = i
        else:
            complex_array = complex_array ** 2 + c
            condition = (abs(complex_array) >= 2) & (iteration_array[i - 1] > i) # absolute value of z is greater than 0 and the array value has not been filled
            iteration_array[i] = iteration_array[i - 1]
            iteration_array[i][condition] = i

    return iteration_array

def julia_set_plot_single_frame(iteration_array, frame, dpi = 200, cmap = 'Blues'):
    '''
    plots a specific frame of the julia set

    parameters:
    iteration_array: 3d numpy array holding each frame of the julia set
    frame: the specfic frame that is going to be plotted (dtype = int)
    dpi: dots per inch (dtype = int)
    cmap: colourmap (dtype = str)

    returns a plot of the particular frame of the julia set
    '''
    plt.figure(dpi = dpi)
    plt.axis('off')
    plt.imshow(iteration_array[frame - 1], cmap = cmap, interpolation = 'None')
    plt.show();

def julia_set_save_image(iteration_array, frame, dpi = 300, cmap = 'Blues'):
    '''
    saves a frame of the julia set as an image
    '''
    plt.figure(dpi = dpi)
    plt.axis('off')
    plt.imshow(iteration_array[frame - 1], cmap = cmap, interpolation = 'None')
    file = f'../images/julia_set_{cmap.lower()}_{len(iteration_array)}.gif'
    plt.savefig(file)

# one possible method of animating:
def julia_set_plot_frames(iteration_array, frame, dpi = 200, cmap = 'Blues'):
    '''
    animates the julia set frames within iteration_array
    parameters:
    '''
    for i in range(len(iteration_array)): # from 1 to iteration + 1 because array is a zero array    
        plt.clf() # clears the figure
        plt.figure(1, dpi = dpi)
        plt.imshow(iteration_array[i], cmap = cmap, interpolation = 'None')
        plt.axis("off")
        plt.pause(1/fps)
    plt.show();

# another method of animating:
# # dpi is the main determinant how fast it can go
def julia_set_plot_frames_v2(iteration_array, interval = 20, dpi = 100, cmap = 'Blues', repeat_delay = 200):
    '''
    animates the julia set frames within iteration_array
    parameters:
    '''
    fig, ax = plt.subplots(dpi = dpi)
    ax.axis('off')
    ims = []
    for i in range(len(iteration_array)):
        im = ax.imshow(iteration_array[i], animated = True, cmap = cmap)
        ims.append([im])
    anim = animation.ArtistAnimation(fig, ims, interval = interval, blit = True, repeat_delay = repeat_delay)
    plt.show();

# saving as a gif
def julia_set_save_gif(iteration_array, interval = 50, dpi = 100, cmap = 'Blues', repeat_delay = 200):
    '''
    saves the julia set animation as a gif
    parameters:
    '''
    fig, ax = plt.subplots(dpi = dpi)
    ax.axis('off')
    ims = []
    for i in range(len(iteration_array)):
        im = ax.imshow(iteration_array[i], animated = True, cmap = cmap)
        ims.append([im])
    anim = animation.ArtistAnimation(fig, ims, interval = interval, blit = True, repeat_delay = repeat_delay)
    file = f'../gifs/julia_set_{cmap.lower()}_{len(iteration_array)}.gif'
    anim.save(file, writer = 'pillow')