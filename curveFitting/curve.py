# -*- coding: utf-8 -*-
#from utils.gauss import gauss
from utils.mathextended import bigSum
from utils.gauss import *
import numpy

w = []
def y(M, x):
	global w
	if not w:
		return False
	return bigSum(0,M, lambda j: w[j]*x**j)

def error(M,x, t):
	return bigSum(0, len(x)-1, lambda n: (y(M,x[n]) - t[n])**2 )

def errorRMS(M,x, t):
	return ( 2*error(M, x, t) / len(x) )**0.5

def genCoef(M, N, x, y): # M is the order, N is number of points, t = training Y, x = training X
		# N = number of points
		# General formula is: bigSum(0,M, lambda j: w[j]*bigSum(1, N, lambda n: x[n]**(i+j))) = bigSum(t[n]*x[n]**i)
		# Or, if set vars to:
		# A[i][j] = bigSum(1,N lambda n: w[j]*x[n]**(i+j) )
		# T[i] = bigSum(1,N, lambda n: t[n]*x**i)

		# THIS IS A PURE LINEAR REGRESSION STYLE OF LEARNING. NO BAYSEIAN OR FREQUENTIST APPROACH
		global w
		w = [0 for i in range(M+1)]
		s = lambda k: bigSum(0, N-1, lambda i:x[i]**k)
		S = numpy.array( [ s(ii) for ii in range(0, 2*M+1)] )

		sA = []
		for i in range(0, M+1):
			sA.append([ S[ii] for ii in range(i,M+i+1) ])
		sA = numpy.array(sA)
			  
		t = lambda k: bigSum(0, N-1, lambda i: y[i]*x[i]**k)
		T = numpy.array([ t(ii) for ii in range(0,M+1) ])
		
		results = numpy.linalg.solve(sA,T)
		for i in range(0,len(w)):
			w[i] = results[i]