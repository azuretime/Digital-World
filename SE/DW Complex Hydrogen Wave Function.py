# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 12:00:13 2017

@author: XUAN
"""

import numpy as np
import scipy.constants as c

#------------------------------------------1-----------------------------------------------#
def energy_n(n):
    a=(c.m_e)/(2*c.hbar**2)
    b=(c.e**4)/((4*c.pi*c.epsilon_0)**2)
    d=1/(float(n**2))
    energy=-(a*b*d/c.e)
    return round(energy,5)
    
#------------------------------------------2-----------------------------------------------#
def degToRad(deg):
    x=deg*c.pi/180.0
    return round(x,5)
    
def radToDeg(rad):
    x=rad*180.0/c.pi
    return round(x,5)
    
#------------------------------------------3-----------------------------------------------#
def sphericalToCartesian(r,theta,phi):
    x=float(r*np.sin(theta)*np.cos(phi))
    y=float(r*np.sin(theta)*np.sin(phi))
    z=float(r*np.cos(theta))
    x=round(x,5)
    y=round(y,5)
    z=round(z,5)
    return (x,y,z)
    
def cartesianToSpherical(x,y,z):
    r=np.sqrt(x**2+y**2+z**2)
    theta=np.arccos(z/r) if r!=0 else 0
    phi=np.arctan2(y,x)
            
    return (round(r,5),round(theta,5),round(phi,5))
    
#------------------------------------------4-----------------------------------------------#
def fact(n):
    i=n
    j=1
    while i>0:
        j=j*i
        i-=1
    return j
    
#------------------------------------------5-----------------------------------------------#
def p00(theta):
    return 1

def p01(theta):
    return np.cos(theta)
    
def p02(theta):
    return 0.5*(3*(np.cos(theta))**2-1)
    
def p03(theta):
    return 0.5*(5*(np.cos(theta))**3-3*np.cos(theta))
    
def p11(theta):
    return np.sin(theta)
    
def p12(theta):
    return 3*np.sin(theta)*np.cos(theta)
    
def p13(theta):
    return 1.5*np.sin(theta)*(5*(np.cos(theta))**2-1)
    
def p22(theta):
    return 3*(np.sin(theta))**2

def p23(theta):
    return 15*(np.sin(theta))**2*np.cos(theta)
    
def p33(theta):
    return 15*np.sin(theta)*(1-(np.cos(theta))**2)
    
def assoc_legendre(m,l):
    m=abs(m)
    if m==0 and l==0:
        return p00
    elif m==0 and l==1:
        return p01
    elif m==0 and l==2:
        return p02
    elif m==0 and l==3:
        return p03
    elif m==1 and l==1:
        return p11
    elif m==1 and l==2:
        return p12
    elif m==1 and l==3:
        return p13
    elif m==2 and l==2:
        return p22
    elif m==2 and l==3:
        return p23
    elif m==3 and l==3:
        return p33
    else:
        return None
        
#------------------------------------------6-----------------------------------------------#
def l00(x):
    return 1

def l01(x):
    return (-x+1)
    
def l02(x):
    return (x**2-4*x+2)
    
def l03(x):
    return (-x**3+9*x**2-18*x+6)
    
def l10(x):
    return 1

def l11(x):
    return (-2*x+4)
    
def l12(x):
    return (3*x**2-18*x+18)

def l13(x):
    return (-4*x**3+48*x**2-144*x+96)
    
def l20(x):
    return 2
    
def l21(x):
    return (-6*x+18)
    
def l22(x):
    return (12*x**2-96*x+144)
    
def l23(x):
    return (-20*x**3+300*x**2-1200*x+1200)
    
def l30(x):
    return 6
    
def l31(x):
    return (-24*x+96)
    
def l32(x):
    return (60*x**2-600*x+1200)
    
def l33(x):
    return (-120*x**3+2160*x**2-10800*x+14400)
    
def assoc_laguerre(p,qmp):
    if p==0 and qmp==0:
        return l00
    elif p==0 and qmp==1:
        return l01
    elif p==0 and qmp==2:
        return l02
    elif p==0 and qmp==3:
        return l03
    elif p==1 and qmp==0:
        return l10
    elif p==1 and qmp==1:
        return l11
    elif p==1 and qmp==2:
        return l12
    elif p==1 and qmp==3:
        return l13
    elif p==2 and qmp==0:
        return l20
    elif p==2 and qmp==1:
        return l21
    elif p==2 and qmp==2:
        return l22
    elif p==2 and qmp==3:
        return l23
    elif p==3 and qmp==0:
        return l30
    elif p==3 and qmp==1:
        return l31
    elif p==3 and qmp==2:
        return l32
    elif p==3 and qmp==3:
        return l33
    else:
        return None
        
#------------------------------------------7-----------------------------------------------# 
def angular_wave_func(m,l,theta,phi):
    if m>0:
        eps=(-1.0)**m
    elif m<=0:
        eps=1
    left=np.sqrt((2.0*l+1.0)*fact(l-abs(m))/(4.0*c.pi*fact(l+abs(m))))
    center=eps*np.exp(1j*m*phi)
    pfunc=assoc_legendre(m,l)
    right=pfunc(theta)
    ans=left*center*right
    return np.round(ans,5)
    
#------------------------------------------8-----------------------------------------------#
def radial_wave_func(n,l,r):
    a=c.physical_constants['Bohr radius'][0]
    p=2.0*l+1.0
    qmp=n-l-1.0
    left=np.sqrt((2.0/(n*a))**3*fact(qmp)/(2.0*n*(fact(n+l))**3))
    center=np.exp(-r/(n*a))*(2.0*r/(n*a))**l
    lfunc=assoc_laguerre(p,qmp)
    right=lfunc(2.0*r/(n*a))
    ans=(left*center*right)/(a**(-1.50))
    return np.round(ans,5)
    
#------------------------------------------9-----------------------------------------------#
def hydrogen_wave_func(n,m,l,roa,Nx,Ny,Nz):
    a=c.physical_constants['Bohr radius'][0]
    x=np.linspace(-roa,roa,Nx)
    y=np.linspace(-roa,roa,Ny)
    z=np.linspace(-roa,roa,Nz)
    xx,yy,zz=np.meshgrid(x,y,z)
    fvec=np.vectorize(cartesianToSpherical)
    roa,theta,phi=fvec(xx,yy,zz)
    r=roa*a
    R=radial_wave_func(n,l,r)
    Y=angular_wave_func(m,l,theta,phi)
    density=np.absolute(R*Y)**2
    return np.round(xx,5),np.round(yy,5),np.round(zz,5),np.round(density,5)