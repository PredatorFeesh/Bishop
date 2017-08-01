from matplotlib import pyplot as plt
from math import sin, pi, ceil
from random import random
import numpy
from scipy import linalg

def console():
	i = ""
	while str(i) != "q":
		i = input()
		try:
			print(eval(i))
		except Exception as e:
			print("[-] That is not an acceptable request")
	return
def bigSum(start, end, f): # f passed as lambda
	s=0
	if start > end:
		return s
	for i in range(start, end+1):
		s+= f(i)
	return s
def bigProduct(start, end, f):
	p = 1
	if start > end:
		return 0
	for i in range(start, end+1):
		p*= f(i)
	return p

def frange(x,y,jump):
	while x < y:
		yield x
		x += jump




w = []

def genCoef(M, N, x, y): # M is the order, N is number of points, t = training Y, x = training X
		# N = number of points
		# General formula is: bigSum(0,M, lambda j: w[j]*bigSum(1, N, lambda n: x[n]**(i+j))) = bigSum(t[n]*x[n]**i)
		# Or, if set vars to:
		# A[i][j] = bigSum(1,N lambda n: w[j]*x[n]**(i+j) )
		# T[i] = bigSum(1,N, lambda n: t[n]*x**i)
		
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
				
def Main():
	xSin = []
	ySin = []

	xMachine= []
	yMachine= []
	
	xPredict = []
	yPredict = []

	i=0.00
	end= (pi*2)

	func = lambda x : sin(x)

	while i <= end: # Plots the SIN curve
		xSin.append(i)
		ySin.append(func(i))
		i+=0.01

	for g in frange(0.0,6.5, 0.6): # Random points along the curve generated
		rand = (-1)**int(random()*10) * int(random()*2)
		xMachine.append(g) # stores randomness x
		yMachine.append(rand + func(g)) # stores the randomness y


	N = len(xMachine)
	M = N
	genCoef(M,N, xMachine, yMachine)

	for i in frange(0.0,xSin[-1], 0.01):
		xPredict.append(i)
		pred = bigSum(0,M, lambda j: w[j]*i**j)
		yPredict.append( pred )

		
	#print(w)
	
	plt.axis([-0.5,end+0.5,-4,4])
	plt.plot(xSin,ySin)
	plt.plot(xPredict, yPredict)
	plt.scatter(xMachine,yMachine)

	plt.show()


if __name__ == '__main__':
	Main()
