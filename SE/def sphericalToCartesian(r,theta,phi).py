import numpy as np
def sphericalToCartesian(r,theta,phi):
	x=r*np.sin(theta)*np.cos(phi)
	y=r*np.sin(theta)*np.sin(phi)
	z=r*np.cos(theta)

	return round(x,5),round(y,5),round(z,5)

def cartesianToSpherical(x, y, z):
	x=float(x)
	y=float(y)
	z=float(z)
	r=np.sqrt(x**2+y**2+z**2)
	rxy=np.sqrt(x**2+y**2)
	if x!=0:
		phi=np.arctan(y/x)
	else:
		eps=1e-10
		phi=np.arctan(y/eps)
	theta=np.arccos(z/r)
	return round(r,5), round(theta,5), round(phi,5)