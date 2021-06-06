# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 13:33:37 2021

@author: BerkeAyevi
"""

import numpy as np


def func(x): #Our Function to be calculated
    
    f = x**(np.cos(x))
    
    return f

def phi(x,h): # The phi function
    
    y = (func(x+h)-func(x-h))*0.5/h
    
    return y


def Dnm(D,n,m): # Main Richardson formula
    
    y = ((4**m)*D[n,m-1] - D[n-1,m-1])/ ((4**m)-1)
    
    return y

h= 0.1
x = 0.6
n= 5
m=5

D = np.array([ [0] * (n+1) ] * (n+1), float) #Creating np array

for i in range(n+1):
    
    D[i,0] = phi(x,h) #Frist Calculation D(n,0)
    
    for j in range(1,i+1):
        
        D[i,j]= Dnm(D, i, j) #adds every time to  the array

    h= h/(2) #end of the loop /2 to change pi



print('D(5,5) Estimated Derivative: ',D[5,5])

    












        