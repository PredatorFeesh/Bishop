from matplotlib import pyplot as plt
from math import sin, pi
from random import random
from curveFitting.curve import genCoef, errorRMS, y
from utils.gauss import gauss, mean

def console():
    i = ""
    while str(i) != "q":
        i = input()
        try:
            print(eval(i))
        except Exception as e:
            print("[-] That is not an acceptable request")
    return

def frange(x,y,jump):
    while x < y:
        yield x
        x += jump

                
def Main():
    global w
    plt.figure(1)
    plt.subplot(221)
    
    plt.title("Mapping input to output")
    plt.xlabel("Input")
    plt.ylabel("Values")
    
    xSin = []
    ySin = []

    xMachine= []
    yMachine= []

    xPredict = []
    yPredict = []
    
    xProb = []
    yProb = []

    i=0.00
    end= (pi*2)
    
    #Change this function
    func = lambda x : 10*sin(x)

    while i <= end: # Plots the SIN curve
        xSin.append(i)
        ySin.append(func(i))
        i+=0.01

    for g in frange(0.0,6.5, 0.05): # Random points along the curve generated
        rand = (-1)**int(random()*10) * (random()*2)
        xMachine.append(g) # stores randomness x
        yMachine.append(rand + func(g)) # stores the randomness y

    '''for t in frange(0.0, 6.5, 0.5):
        rand = (-1)**int(random()*10) * int(random()*2)
        xTest.append(g) # stores randomness x
        yTest.append(rand + func(t)) # stores the randomness y
        '''

    #Generate for order M
    N = len(xMachine)
    M = 3
    genCoef(M,N, xMachine, yMachine)

    for i in frange(0.0,xSin[-1], 0.01):
        xPredict.append(i)
        pred = y(M,i)
        yPredict.append( pred )
    #End order M geenrating

    #This is for predicting the best order
    plt.plot(xSin,ySin)
    plt.plot(xPredict, yPredict)
    plt.scatter(xMachine,yMachine)

    miniOrd = -1
    miniErr = 10**15
    for M in range(0,N):
        genCoef(M,N,xMachine,yMachine)
        cur = errorRMS(M,xMachine, yMachine)
        if cur < miniErr:
            miniOrd = M
        miniErr = min(cur, miniErr)
        print("Error of order ",M," is ",cur)
    print("The lowest value of error for M is", miniOrd)
    xMin = []
    yMin = []
    genCoef(miniOrd, N, xMachine, yMachine)
    for i in frange(0.0, 6.3, 0.1):
        xMin.append(i)
        yMin.append(y(miniOrd, i))
    plt.plot(xMin, yMin)
    #END PLOT OF BEST PREDICTED WITH ERROR RMS
        
    
    #Probabiliy of the data
    plt.subplot(222)
    plt.title("Probability of finding a point at output Y")
    plt.xlabel("Y")
    plt.ylabel("Probability")
    for ii in frange(-18.000, 18.000, 0.1):
        yProb.append(ii)
        xProb.append( gauss(ii, yMachine) )
    plt.plot(xProb, yProb)
    print(mean(yMachine))
    #End data probability
    
    

    plt.show()


if __name__ == '__main__':
    Main()
