import numpy as np
import matplotlib.pyplot as plt

x_pixels = 500
y_pixels = round((2/3) * x_pixels)
x_lower_bound = -2
y_lower_bound = 2/3 * x_lower_bound
x=np.linspace(x_lower_bound, x_lower_bound*(-1), x_pixels) # get 3:2 ratio because it looks good 
y=np.linspace(y_lower_bound, y_lower_bound*(-1), y_pixels) * 1j
complex_num = x + y.reshape(y_pixels, 1)
array=np.zeros((y_pixels, x_pixels))

iteration = 15
z = complex_num
c = 0
'''
values to test out:
c = 0.285, 0.28 + 0.008j, 0.3 - 0.01j
c = -1.476
c = -0.4 + 0.6j, 0.285 + 0.01j, -0.8 + 0.156j, -0.70176 - 0.3842j
'''
for i in range(0, iteration + 1): # from 1 to iteration + 1 because array is a zero array 
    z = z ** 2 + c
    condition = (abs(z) >= 2) & (array == 0) # absolute value of z is greater than 0 and the array value has not been filled
    array[condition] = i
else:
    array[array == 0] = iteration

plt.figure(dpi = 1000)
plt.imshow(array, cmap = 'Blues', interpolation = 'None')
plt.axis("off")
plt.show();