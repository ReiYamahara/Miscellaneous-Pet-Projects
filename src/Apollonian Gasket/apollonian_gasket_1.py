import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from cmath import *

fig, ax = plt.subplots(dpi = 100)
plt.axis('equal')

# parameter: angle and radius
theta = np.linspace(0, 2*np.pi, 100)
r_1 = 1

# Creating pandas dataframe
df = pd.DataFrame({'Radius':[-1], 'Centre':[[0, 0]], 
                'radius_1':[0], 'centre_1':[0], 
                'radius_2':[0], 'centre_2':[0],
                'radius_3':[0], 'centre_3':[0]})

df.loc[len(df)] = [1/2, [-1/2, 0], 0, 0, 0, 0, 0, 0]
df.loc[len(df)] = [1/2, [1/2, 0], 0, 0, 0, 0, 0, 0]

## Initial Conditions:
# Outer circle:
x_1 = r_1*np.cos(theta)
y_1 = r_1*np.sin(theta)
ax.plot(x_1, y_1)

# Second circle:
r_2 = r_1 / 2
x_2 = r_2 * np.cos(theta) - 0.5
y_2 = r_2 * np.sin(theta)
ax.plot(x_2, y_2)

# Third circle:
r_3 = r_1 / 2
x_3 = r_3 * np.cos(theta) + 0.5
y_3 = r_3 * np.sin(theta)
ax.plot(x_3, y_3)

# maybe make a pandas dataframe for each circle: for each new circle, there'll be the radius and the centre of the three other circles
# a tree is more optimal but this will have to do - we will put another parameter - the size of the radius.

# Each circle will have a centre, a radius and a curvature and a 

def radius_and_centre(r_1, centre_1, r_2, centre_2, r_3, centre_3): # it should take in the dataframe... and also a limit parameter (curvature value)
    '''
    Parameters:
    r_1, r_2, r_3: float
    centre_1, centre_2, centre_3: list of 2 floats

    returns the radius and centres of the 4th circle
    ''' # what if there are multiple solutions...?

    # curvature of the three cirles
    curve_1 = 1/r_1
    curve_2 = 1/r_2
    curve_3 = 1/r_3

    # radius of the 4th circle # we could get two different radii
    curve_4 = curve_1 + curve_2 + curve_3 + 2*sqrt(curve_1*curve_2 + curve_2*curve_3 + curve_3*curve_1)
    r_4 = (1/curve_4).real # converting from complex to real

    # complex number form of the three circles
    complex_1 = centre_1[0] + centre_1[1]* 1j
    complex_2 = centre_2[0] + centre_2[1]* 1j
    complex_3 = centre_3[0] + centre_3[1]* 1j

    # complex number multiplied by curvature
    compcurve_1 = curve_1 * complex_1 
    compcurve_2 = curve_2 * complex_2
    compcurve_3 = curve_3 * complex_3

    # centres of the 4th circle
    # maybe we need to verify if there is 1 or 2 solutions...?
    first_centre = (compcurve_1 + compcurve_2 + compcurve_3 + 2*sqrt(compcurve_1*compcurve_2 + compcurve_2*compcurve_3 + compcurve_3*compcurve_1))/curve_4 
    first_centre_list = [first_centre.real, first_centre.imag]

    second_centre = (compcurve_1 + compcurve_2 + compcurve_3 - 2*sqrt(compcurve_1*compcurve_2 + compcurve_2*compcurve_3 + compcurve_3*compcurve_1))/curve_4
    second_centre_list = [second_centre.real, second_centre.imag]

    # we need to keep a record of the three circles for each new circle plotted...
    # not happy that the main dataframe is coming from a global variable... we can fix this later
    df.loc[len(df)] = [r_4, first_centre_list, r_1, centre_1, r_2, centre_2, r_3, centre_3]
    df.loc[len(df)] = [r_4, second_centre_list, r_1, centre_1, r_2, centre_2, r_3, centre_3]

def plotter(df):
    for i in range(2, len(df)):
        radius = df.iloc[i, 0]
        centre = df.iloc[i, 1]
        x = radius*np.cos(theta) - centre[0]
        y = radius*np.sin(theta) - centre[1]
        ax.plot(x, y)

radius_and_centre(-1, [0,0], 1/2, [-1/2, 0], 1/2, [1/2, 0])
plotter(df)

plt.show()
print(df);


# we need to create a tree of some sorts...?