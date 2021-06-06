# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 13:46:38 2021

@author: BerkeAyevi
"""

import math 


def cm2inc(x):
    
    result = float(x)/2.54
    
    return result

def func(x):
    
    f = (math.exp(-1*(((x-69)**2)/(5.6))))/(2.8*((2*math.pi)**(1/2)))
    
    return f

def Simpson(func,a,b,n):
    
    a = cm2inc(a) # converting to the inch
    b = cm2inc(b) # converting to the inch
    h = (b-a)/float(n) #the width
    I = func(a) #starting with the a
    
    for i in range(1,n):
        
        if (i %2 ==0): # Even Case
            
            I = I + 2* func(a+ i*h)
            
        else: # Odd Case
            
            I = I + 4* func(a+ i*h)
            
    result = (h/3) * I # res* h /3 
                
    
    return result

a= 150
b = 182
n = 1000000



ans = Simpson(func, a, b, n)
print(ans, 'is the probability of Tusrkish male is between 150cm and 182cm')








