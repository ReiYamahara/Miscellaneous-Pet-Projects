import numpy as np
import matplotlib.pyplot as plt


y_Pixels = 2000
x_Pixels = round((2/3)*y_Pixels)
array=np.zeros((x_Pixels,y_Pixels))
x=np.linspace(-2,2,y_Pixels)
y=np.linspace(-2,2,x_Pixels)


def mandelbrot_set(Re,Im, max_iter):
    c=complex(Re,Im)
    z=0
    for i in range(max_iter):
        z=z**2+c
        if abs(z)>=2:
           return i
    return max_iter


for b in y:
   for a in x:
        array[np.where(y==b),np.where(x==a)]=mandelbrot_set(a,b,50)

fig=plt.figure(dpi=1000)
plt.imshow(array,cmap='Reds',extent=[-2,2,-2,2],interpolation='None')
plt.axis("off")
plt.show();

# very slow... how to make it more efficient...?
# iteration shouldn't be used.
# We should use broadcasting.