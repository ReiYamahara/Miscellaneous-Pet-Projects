import numpy as np
import matplotlib.pyplot as plt

x_pixels = 1000
y_pixels = round((2/3) * x_pixels)
x=np.linspace(-2.1, 1.2, x_pixels) # get 3:2 ratio because it looks good 
y=np.linspace(-1.2, 1.2, y_pixels) * 1j
complex_num = x + y.reshape(y_pixels, 1)
array=np.zeros((y_pixels, x_pixels))

iteration = 4
z = 0

for i in range(1, iteration + 1): # from 1 to iteration + 1 because array is a zero array
    z = z ** 2 + complex_num
    condition = (abs(z) >= 2) & (array == 0) # absolute value of z is greater than 0 and the array value has not been filled
    array[condition] = i
else:
    array[array == 0] = iteration

plt.figure(dpi = 100)
plt.imshow(array, cmap = 'RdBu', interpolation = 'None')
plt.axis("off")
plt.show();