import scipy.constants as c

def energy_n(n):
    En=-1.0/(n**2)*(13.60569)
    return round(En,5)
import scipy.constants as c

def energy_n(n):
	# returns energy in eV
	# page 149, Eq. 4.7
	y1=c.m_e/(2.0*c.hbar*c.hbar)
	y2=c.e*c.e/(4.0*c.pi*c.epsilon_0)
	return round(-y1*(y2**2)*(1.0/(n*n))/c.e,5)
