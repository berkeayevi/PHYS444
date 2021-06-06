# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 12:44:19 2021

@author: BerkeAyevi
"""

tol = 10**(-6)                                                      #Our tolerance

def func(x):
    f = (x**4)-6.4*(x**3)+ 6.45*(x**2) +20.538*(x)-31.752           #Function to be solve
    return f

def dfunc(x):
    df =  4.0*(x**3)- (6.4*3)*(x**2)+ (6.45*2)*(x)+ 20.538          #Derivative of the Function
    return df


def Newton_Method(x,tol):                                           #Newton Methode Takes Guess and Tolerance Value
    
    for i in range(1000):                                           #Main loop to be exact set high itteration value
                                                                    #Iterration= 1000 RN
        dx = -(func(x)/dfunc(x))                                    #Value of dx
        x= x + dx                                                   #Increase/Decrease Our guess according to dx 
            
        if (abs(dx) < tol):                                         #When we reach our tollerance
            
            return print(x)                                         #Print The solutiton
        
        
        
Newton_Method(2,tol)

    
    
    
    