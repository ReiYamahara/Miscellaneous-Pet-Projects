import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def julia_set(c = 0.28 + 0.008j, x_pixels = 1000, iterations = 30):
    '''
    creates a frame for each iteration of the julia set function and stores it in a numpy array

    parameters:

    returns a numpy array within a numpy array
    '''
    y_pixels = round((2/3) * x_pixels)
    x_lower_bound = -2
    y_lower_bound = 2/3 * x_lower_bound
    x = np.linspace(x_lower_bound, x_lower_bound*(-1), x_pixels) # get 3:2 ratio because it looks good 
    y = np.linspace(y_lower_bound, y_lower_bound*(-1), y_pixels) * 1j
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

# one possible method:
def julia_set_plot(iteration_array, fps = 10, dpi = 100, cmap = 'Blues'):
    '''
    plots the julia set frames which are within a numpy array
    
    parameters:
    '''
    for i in range(len(iteration_array)): # from 1 to iteration + 1 because array is a zero array    
        plt.clf() # clears the figure
        plt.figure(1, dpi = dpi)
        plt.imshow(iteration_array[i], cmap = cmap, interpolation = 'None')
        plt.axis("off")
        plt.pause(1/fps)
    plt.show();

# another method: # dpi is the main determinant how fast it can go
def julia_set_plot_v2(iteration_array, interval = 20, dpi = 100, cmap = 'Blues', repeat_delay = 200):
    '''
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
def julia_set_save(iteration_array, interval = 20, dpi = 100, cmap = 'Blues', repeat_delay = 200):
    '''
    saves the julia set animation as a gif
    '''
    fig, ax = plt.subplots(dpi = dpi)
    ax.axis('off')
    ims = []
    for i in range(len(iteration_array)):
        im = ax.imshow(iteration_array[i], animated = True, cmap = cmap)
        ims.append([im])
    anim = animation.ArtistAnimation(fig, ims, interval = interval, blit = True, repeat_delay = repeat_delay)

    anim.save(f'julia_set_{cmap.lower()}_{len(iteration_array)}.gif', writer = 'pillow')

# save as a gif without having to plot it...
iteration_array = julia_set(x_pixels = 2000, iterations = 100)
julia_set_save(iteration_array, interval = 50, dpi = 300)