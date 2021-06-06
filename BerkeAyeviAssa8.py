# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:00:12 2021

@author: BerkeAyevi
"""
import math

def  f(x): #Our function to compute

    func = (math.exp(x)*math.cos(x))

    return func

def GaussianQuadratrue(a,b,func): # Using the equations in pg6

    x1= ((b-a)*0.5)*((-1)/((3)**0.5))+ ((a+b)*0.5)
    x2= ((b-a)*0.5)*((1)/((3)**0.5))+ ((a+b)*0.5)
    c1= ((b-a)*0.5)
    c2= ((b-a)*0.5)

    result = c1*func(x1)+c2*func(x2)

    return result


a = 0.5 # initial
b = 1.5 # final

ans = GaussianQuadratrue(a,b,f)

print(ans)



