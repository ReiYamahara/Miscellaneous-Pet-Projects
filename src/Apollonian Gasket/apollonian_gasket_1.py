import matplotlib.pyplot as plt
import numpy as np
import cmath

fig=plt.figure(dpi=100)
plt.axis('equal')
plt.axis('off')

#simplifications
sin=np.sin
cos=np.cos
sqrt=np.sqrt

#setting parameters
theta = np.linspace(0, 2*np.pi, 100)
r=1

#Initial conditions:
a = r*cos(theta) + 0
b = r*sin(theta)

c = r/2*cos(theta) - 0.5
d = r/2*sin(theta)

e = r/2*cos(theta) + 0.5
f = r/2*sin(theta)

plt.plot(a,b,linewidth=1)
plt.plot(c,d,linewidth=1)
plt.plot(e,f,linewidth=1)


#defining each formula that computes the new radius and the new centre
# x y z are the radius
# a b c are the centres
def g(x,y,z):
    C1=1/x
    C2=1/y
    C3=1/z
    C4=C1+C2+C3+2*sqrt(C1*C2+C2*C3+C3*C1)
    new_rad = 1/C4
    return new_rad

def h(x,y,z,a,b,c):
    C1=1/x
    C2=1/y
    C3=1/z
    C4=C1+C2+C3+2*sqrt(C1*C2+C2*C3+C3*C1)
    D1 = C1*a
    D2 = C2*b
    D3 = C3*c
    D4= D1+D2+D3+2*cmath.sqrt(D1*D2+D2*D3+D3*D1)
    new_centre=D4/C4
    return new_centre

radius=np.array([-1,1/2,1/2])
centres=np.array([0,1/2,-1/2])
#try without using arrays...
for i in range(10):
    radius=np.append(radius,g(-1,1/2,radius[2+i]))
    centres=np.append(centres, h(-1,1/2,radius[2+i],0,1/2,centres[2+i]))
    a = radius[2+i]*cos(theta)+centres[2+i].real
    b = radius[2+i]*sin(theta)+centres[2+i].imag
    plt.plot(a,b,linewidth=1)

    
#Trouble problem here...   
for i in range(3):
    radius[5+i]=g(-1,1/3,radius[4+i])
    centres[5+i]=h(-1,1/3,radius[4+i],0,2/3j,centres[4+i])
    
    c = radius[5+i]*cos(theta)+centres[5+i].real
    d = radius[5+i]*sin(theta)+centres[5+i].imag
    plt.plot(c,d,linewidth=1)


print(radius)
print(centres)
plt.scatter(0.5,2/3)
plt.scatter(0.6428571428571428,0)

print(radius[4],centres[4])
print(h(-1,1/3,radius[4],0,2/3j,centres[4]))   
print(h(-1,1/3,1/6,0,2/3j,1/2+2/3j))
plt.show();

