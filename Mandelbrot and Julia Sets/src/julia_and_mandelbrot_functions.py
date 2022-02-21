import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

# version 1 of making julia set frames: this one is more clunky...
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

# version 2 of making julia set frames: much cleaner + use of meshgrid
def julia_set_frames_v2(c = 0.28 + 0.008j, x_pixels = 1000, limits = [-2, 2, -4/3, 4/3], iterations = 30):
    '''
    '''
    if c == 0:
        limits = [-2, 1.5, -7/6, 7/6]
    y_pixels = round(x_pixels * ((limits[3] - limits[2])/(limits[1 ]- limits[0])))
    x = np.linspace(limits[0], limits[1], x_pixels, dtype= 'float64')
    y = np.linspace(limits[2], limits[3], y_pixels, dtype = 'float64')
    X, Y = np.meshgrid(x, y)

    iteration_array = np.full((iterations, y_pixels, x_pixels), iterations, dtype = 'float64')

    Z = X + Y * 1j
    if c == 0:
        c = Z
    for i in range(iterations):
        if i == 0:
            Z = Z ** 2 + c
            condition = (abs(Z) >= 2)
            iteration_array[i][condition] = i
        else:
            Z = Z ** 2 + c
            condition = (abs(Z) >= 2) # absolute value of z is greater than 0 and the array value has not been filled
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

    parameters:
    iteration_array: 3d numpy array holding each frame of the julia set
    frame: the specfic frame that is going to be plotted (dtype = int)
    dpi: dots per inch (dtype = int)
    cmap: colourmap (dtype = str)

    returns an image which is put in the image folder
    '''
    plt.figure(dpi = dpi)
    plt.axis('off')
    plt.imshow(iteration_array[frame - 1], cmap = cmap, interpolation = 'None')
    file = f'../images/julia_set_{cmap.lower()}_{len(iteration_array)}.png'
    plt.savefig(file)


# one possible method of animating:
def julia_set_plot_frames(iteration_array, fps = 25, dpi = 200, cmap = 'Blues'):
    '''
    animates the julia set frames within iteration_array

    parameters:
    iteration_array: 3d numpy array holding each frame of the julia set
    fps = frames per second (dtype = int)
    dpi: dots per inch (dtype = int)
    cmap: colourmap (dtype = str)

    returns an animated plot of the julia set
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
    iteration_array: 3d numpy array holding each frame of the julia set
    interval: milliseconds per frame (dtpe = int)
    dpi: dots per inch (dtype = int)
    cmap: colourmap (dtype = str)
    repeat_delay: the delay in milliseconds between consecutive animation runs (dtype = int)

    returns an animated plot of the julia set which is saved in the gif folder
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
    iteration_array: 3d numpy array holding each frame of the julia set
    interval: milliseconds per frame (dtpe = int)
    dpi: dots per inch (dtype = int)
    cmap: colourmap (dtype = str)
    repeat_delay: the delay in milliseconds between consecutive animation runs (dtype = int)

    returns an animated plot of the julia set
    '''
    fig, ax = plt.subplots(dpi = dpi)
    ax.axis('off')
    ims = []
    for i in range(len(iteration_array)):
        im = ax.imshow(iteration_array[i], animated = True, cmap = cmap)
        ims.append([im])
    anim = animation.ArtistAnimation(fig, ims, interval = interval, blit = True, repeat_delay = repeat_delay)
    file = f'julia_set_{cmap.lower()}_{len(iteration_array)}.gif'
    anim.save(file, writer = 'pillow')


# slider for the animation between frames
def julia_set_slider_frames(iteration_array, dpi = 200, cmap = 'Blues'):
    '''
    creates a plot of the julia set that can be altered using the slider

    parameters:
    iteration_array: 3d numpy array holding each frame of the julia set
    dpi:  dots per inch (dtype = int)
    cmap: colourmap (dtype = str)

    returns a plot that can be altered using a slider
    '''
    fig, ax = plt.subplots(dpi = dpi) # defining the figure and axes
    ax.axis('off') 
    # initial plot
    iterations = len(iteration_array)
    plt.imshow(iteration_array[iterations - 1], cmap = 'Blues')

    # defining the location of the slider: [left, bottom, width, height]
    slider_loc = plt.axes([0.3, 0.1, 0.4, 0.025])
    # defining the slider itself:
    # parameters: axes reference; label of the slider; min value of the slider; max value of the slider;
    # valinit: starting point on the slider
    # valstep: the steps of the slider
    slider_frames = Slider(slider_loc, 'Number of Iterations: ', 1, iterations - 1, valinit = iterations - 1, valstep = 1)
    # we will define update as the callback function for the slider. It receives the current value of the slider, 
    # clears the previous plot on the axis, and plots the graph with the new value
    def update(frame, cmap = 'Blues'):
        ax.clear()
        ax.axis('off')
        ax.imshow(iteration_array[frame], cmap = cmap)
    # this captures the on_canged event on the slider and then calls the callback function, update
    slider_frames.on_changed(update)

    # defining the location of the reset button
    reset_loc = plt.axes([0.8, 0.1, 0.1, 0.03])
    button = Button(reset_loc, 'Reset', hovercolor='0.975')
    # defining the reset button: resets to the initial farme
    def reset(event):
        slider_frames.reset()
    # when the reset button is clicked, it calls the callback function, reset
    button.on_clicked(reset)

    # defining the location of the quit button
    quit_loc = plt.axes([0.5, 0.03, 0.1, 0.03])
    exit = Button(quit_loc, 'Quit')
    # defining the quit button: quits the figure
    def quit(event):
        plt.close('all')
    # when the quit button is clicked, it calls the quit function
    exit.on_clicked(quit)

    plt.show();

iteration_array = julia_set_frames_v2(c = 0, x_pixels = 1000, iterations = 80)
julia_set_plot_frames_v2(iteration_array, cmap = 'RdBu')
# error to correct...
'''
/Users/reiyamahara/GitHub/Miscellaneous-Pet-Projects/Mandelbrot and Julia Sets/src/julia_and_mandelbrot_functions.py:69: RuntimeWarning: overflow encountered in absolute
  condition = (abs(Z) >= 2) # absolute value of z is greater than 0 and the array value has not been filled
/Users/reiyamahara/GitHub/Miscellaneous-Pet-Projects/Mandelbrot and Julia Sets/src/julia_and_mandelbrot_functions.py:68: RuntimeWarning: overflow encountered in square
  Z = Z ** 2 + c
/Users/reiyamahara/GitHub/Miscellaneous-Pet-Projects/Mandelbrot and Julia Sets/src/julia_and_mandelbrot_functions.py:68: RuntimeWarning: invalid value encountered in square
  Z = Z ** 2 + c
  '''

  # the invalid value is most likely due to it exceeding 64 bits.

## Slider modifications to do:
# Attempt at changing colours... probably going to need classes...
'''   
 colour_1_loc = plt.axes([0.2, 0.05, 0.1, 0.025])
    colour_1 = Button(colour_1_loc, 'RdBu')
    def change_colour_1(frame, cmap = 'RdBu'):
        slider_frames = Slider(slider_loc, 'Number of Iterations: ', 1, iterations - 1, valinit = iterations - 1, valstep = 1)
        ax.clear()
        ax.axis('off')
        update(frame, cmap)
        slider_frames.on_changed(update)
    colour_1.on_clicked(change_colour_1)
'''
# size, location and quality of the slider, especially relative to the plot: it only works for when the dpi is around 200: otherwise it looks weird.

# Can we do print from the list of images...? or is that not possible...?
# animation that zooms in of the mandelbrot set and gets updated
# slider for zooming in and out
# add background colour: ax.set_facecolour([0, 0, 0])