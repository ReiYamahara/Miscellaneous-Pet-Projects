import random
import numpy as np
import matplotlib.pyplot as plt
# using the diamond-square algorithm:
# the dimensions of z have to be (2^n + 1, 2^n + 1)
# n = the number of iterations we will have to do for the 

iterations = 7
pixels = 2 ** iterations + 1
z = np.zeros((pixels, pixels))

# i need to streamline this... so inefficient yuck

def random_uniform(): # alter the range of the uniform to change the roughness of the terrain
    return 2 ** (-random.uniform(0.8, 1))
def rand(iter):
    return random.uniform(-0.5, 0.5) * random_uniform() ** iter

# initialisation - randomised
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

x, y = np.mgrid[0:pixels, 0:pixels]

fig = plt.figure(dpi = 200)
ax = plt.axes(projection = '3d')
ax.set_facecolor('grey')
ax.axis('off')
ax.view_init(40, 30)
ax.plot_surface(x, y, z, cmap = 'pink')
ax.dist = 7
plt.savefig('../images/fractal_landscape.png')
plt.show()
