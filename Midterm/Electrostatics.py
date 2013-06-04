def pointField(x,y,q,Xq,Yq):
	"""Takes arguments (x,y) and returns a tuple of the electric field components Ex, Ey"""
	k = 8.8987551*10**9
	Ex = k*q*(x-Xq) / ((x-Xq)**2. + (y - Yq)**2.)**.5
	return Ex
	Ey = k*q*(y-Yq) / ((x - X1)**2. + (y- Y1)**2.)**.5
	return Ey
def pointFieldy(x,y,q,Xq,Yq):
	k = 8.8987551*10**9
	Ey = k*q*(y - Yq)/((x-Xq)**2. +(y-Yq)**2.)**.5
	return Ey
