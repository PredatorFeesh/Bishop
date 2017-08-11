# -*- coding: utf-8 -*-
#BEGIN GAUSS FUNCTIONS
#Working
from utils.mathextended import bigSum
from math import pi, exp

def mean(x):
	n = len(x)
	return (1/n)*bigSum(0,n-1,lambda i: x[i]  )
def variance(x):
	n = len(x)
	return ((1/(n-1))*bigSum(0,n-1, lambda i: (x[i]-mean(x))**2))
def gauss(n, t):
	sig = variance(t)
	return (1/(2*pi*sig)**0.5)*exp(-(1/(2*sig**2)*(n-mean(t))**2))

