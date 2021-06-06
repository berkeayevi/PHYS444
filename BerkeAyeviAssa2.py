# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 13:56:04 2021

@author: BerkeAyevi
"""
def func(x):                                                    #Function to be define
    
    f = (x*x) -3
    return f


def bisection(l,u,toll):                                        #Insert Upper, Lower and Tollarance values
    
    if (func(l)*func(u) >=0):                                   #Frist condition to check 
        print("f(u)* f(l) must be <0")
        return
    
    m=l                                                         #Define middle variable
    while((u-l)> toll):                                         #Main loop
        
        m= (u+l)/2.0                                            #Setting m value
        
        y_m= func(m)                                            #Function to be change
        y_a= func(l)                                            #Fixed function at the frist 
        
        if(y_m*y_a<0):                                          #Change upper or lower accordingly
            u=m                                                 #Change upper x value
        else:
            l=m                                                 #Change lower x value
            
    return m


def Fal_Posi(l,u, toll):                                        #Insert Upper, Lower and Tollarance values
    if (func(l)*func(u) >=0):                                   #Frist condition to check 
        print("f(u)* f(l) must be <0")
        return
    x_r = l                                                     #Setting Initial Value
    while(abs(func(x_r))>toll):                                 #Function oscillates - and + values so in order to calculate correctly I added abs to the code
        x_r = ((l*func(u))-(u*func(l)))/(func(u)-func(l))       #Main loop calculation
        if (func(x_r)*func(u)<0.0):
            l= x_r                                              #Change Lower x value
        else:
            u = x_r                                             #Change upper x value
    return x_r

def Perc_Error(x,actual_val):                                   #Percentage Error Function Instert Value and Actual Value
    y = (abs((x-actual_val)/actual_val))*100                    #Main Calculation

    return y

toll= 10**-6                                                    #Our tolarance
actual_val= 3**(1/2)

ans_bi=bisection(1,4,toll)
err_bi=Perc_Error(ans_bi,actual_val)
ans_Fal=Fal_Posi(1,4,toll)
err_Fal=Perc_Error(ans_Fal,actual_val)


print("Answer of Bisectio Method",ans_bi )
print("Percent error of Bisectio Method",'%.6f' % err_bi)       #With 6 significant figure
print("Answer of False-Position Method",ans_Fal)
print("Percent error of False-Position Method",'%.6f' % err_Fal)#With 6 significant figure


