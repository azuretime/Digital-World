import numpy as np 

def p00(theta):
	return 1

def p01(theta):
	return np.cos(theta)

def p02(theta):
	return 0.5*(3*np.cos(theta)**2-1)

def p03(theta):
	return 0.5*(5*np.cos(theta)**3-3*np.cos(theta))

def p11(theta):
	return np.sin(theta)

def p12(theta):
	return 3*np.sin(theta)*np.cos(theta)

def p13(theta):
	return 1.5*np.sin(theta)*(5*np.cos(theta)**2-1)

def p22(theta):
	return 3*np.sin(theta)**2

def p23(theta):
	return 15*np.sin(theta)**2*np.cos(theta)

def p33(theta):
	return 15*np.sin(theta)*(1-np.cos(theta)**2)

def assoc_legendre(m,l):
	if m==0 and l==0:
		return p00
	elif m==0 and l==2:
		return p02
	elif m==1 and l==1:
		return p11
	elif m==3 and l==3:
		return p33
	elif m==0 and l==1:
		return p01
	elif m==2 and l==3:
		return p23
	elif m==2 and l==2:
		return p22
	elif m==1 and l==3:
		return p13
	elif m==1 and l==2:
		return p12
	elif m==0 and l==3:
		return p03
	else:
		return None