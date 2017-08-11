# -*- coding: utf-8 -*-
#BEGIN GAUSS FUNCTIONS
#Working
from mathextended import bigSum
from math import pi, exp

def mean(x):
	n = len(x)
	return (1/n)*bigSum(0,n-1,lambda i: x[i]  )
def variance(x):
	n = len(x)
	return ((1/(n-1))*bigSum(0,n-1, lambda i: (x[i]-mean(x))**2))
def gauss(x, t):
	sig = variance(t)
	return (1/(2*pi*sig)**0.5)*exp(-(1/(2*sig**2)*(x-mean(t))**2))
#END GAUSS