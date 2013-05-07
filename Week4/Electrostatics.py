
import numpy as np

def pointPotential(x,y,q,posx,posy):
	k= 8.987551*10**9
	Vyx = (k*q)/(x**2 + y**2)**(1/2.) #insert Vxy function
	return Vyx #return Vxy

def dipolePotential(x,y,q,d):
	k = 8.987551*10**9
	Vxy = (k*q/((x)**2 + (y - d)**2)**(1/2.) - (k*q/(x**2 + (y + d)**2)**(1/2.))) #insert Vxy function
	return Vxy #return Vxy

def pointField(x,y,q,Xq,Yq):
	"""Takes arguments (x,y), q, Xq, Yq, and returns a tuple of the electric field components (Ex, Ey)"""
	k = 8.987551*10**9
	Ex = k*q*(x - Xq) / ((x - Xq)**2 + (y - Yq)**2)**.5
	Ey = k*q*(y - Yq) / ((x - Xq)**2 + (y - Y1)**2)**.5
