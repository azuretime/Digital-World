import scipy.constants as c

def degToRad(deg):
	return round(deg/180.0*c.pi,5)

def radToDeg(rad):
	return round(rad*180.0/c.pi,5)

    
print degToRad(180)
print radToDeg(3.14/2.0)