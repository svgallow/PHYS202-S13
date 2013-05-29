import numpy as np
k = 8.9875518*10**9 #setting k, q, and d values
q = 1*10**-9
d=1
def pointPotential(x,y,q,posx,posy):
    Vyx = (k*q)/(x**2 + y**2)**(1/2.) #insert Vxy function
    return Vyx #return Vxy
x,y = meshgrid(arange(-2.,2.,0.06),arange(-2.,2.,0.06))
Vyx = pointPotential(x,y,1e-9,0.,0.)

def dipolePotential(x,y,q,d):
k = 8.9875518*10**9 #setting k, q, and d values
q = 1*10**-9
d=1
Vxy = (k*q/((x)**2 + (y - d)**2)**(1/2.) - (k*q/(x**2 + (y + d)**2)**(1/2.))) #insert Vxy function
return Vxy #return Vxy
x,y = meshgrid(arange(-2.,2.,0.06),arange(-2.,2.,0.06))
Vxy = dipolePotential(x,y,q,d)
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = fig.gca(projection = '3d')
p = ax.plot_surface(x,y,Vxy, rstride=1, cstride=1, linewidth=0, cmap=cm.spectral)


