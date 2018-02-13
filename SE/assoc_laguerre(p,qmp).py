def l00(x):
	return 1

def l01(x):
	return -x+1

def l02(x):
	return x*x-4*x+2

def l10(x):
	return 1

def l11(x):
	return -2*x+4

def l12(x):
	return 3*x*x-18*x+18

def l13(x):
    return -4*x*x*x+48*x*x-144*x+96

def l20(x):
	return 2

def l21(x):
	return -6*x+18

def l23(x):
    return -20*x*x*x+300*x*x-1200*x+1200

def l22(x):
	return 12*x*x-96*x+144

def l03(x):
    return -x*x*x+9*x*x-18*x+6

def l30(x):
	return 6

def l31(x):
	return -24*x+96

def l32(x):
	return 60*x*x-600*x+1200

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