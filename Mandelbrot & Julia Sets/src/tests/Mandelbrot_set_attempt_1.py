import numpy as np
import matplotlib.pyplot as plt

y_pixels = 300
x_pixels = round((2/3) * y_pixels)
array=np.zeros((x_pixels, y_pixels))
x=np.linspace(-2, 1, y_pixels)
y=np.linspace(-1.2, 1.2, x_pixels)

def mandelbrot_set(Re,Im, max_iter):
    z=complex(Re,Im)
    c = 0
    for i in range(max_iter):
        z=z**2+c
        if abs(z)>=2:
           return i
    return max_iter

for b in y:
   for a in x:
        array[np.where(y==b),np.where(x==a)]=mandelbrot_set(a,b,10)
        
     
fig=plt.figure(dpi=100)
plt.imshow(array,cmap='Reds',extent=[-2,2,-2,2],interpolation='None')
plt.axis("off")
plt.show();

# very slow... how to make it more efficient...?
# iteration shouldn't be used.
# We should use broadcasting.