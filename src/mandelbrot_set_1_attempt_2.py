import numpy as np
import matplotlib.pyplot as plt

x_pixels = 4000
y_pixels = round((2/3) * x_pixels)
x=np.linspace(-2, 1, x_pixels)
y=np.linspace(-1.2, 1.2, y_pixels) * 1j
complex_num = x + y.reshape(y_pixels, 1)
array=np.zeros((y_pixels, x_pixels))

iteration = 10
z = 0
for i in range(iteration, 0, -1):
    z = z ** 2 + complex_num
    array[abs(z) < 2] = i
else:
    array[abs(z) >= 2] = iteration

# few issues: it is essential for the code to go through all the iterations...
# we also have that the curved shape when the number of iteration increases
# doesn't look clean as we go in...
# it's the right idea but it could definitely be cleaner...
# for example, at iteration = 10, there are only two colours...

fig=plt.figure(dpi=200)
plt.imshow(array,cmap='magma',extent=[-2,2,-2,2],interpolation='None')
plt.axis("off")
plt.show();