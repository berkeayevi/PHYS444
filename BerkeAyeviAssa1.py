# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 13:15:32 2021

Assaigmnet #1


@author: BerkeAyevi
"""
import numpy as np
import matplotlib.pyplot as plt


t=  np.linspace(0,100,100)          #0 to 100 increase by 1  
v0= 5                               #initial speed (m/s)
g=  10                              #g (m/(s^2))


y = v0 + (1/2)* g * (t**2)           #initial function
m,n,b = np.polyfit(t,y,2)            #coefficents for fitting m is 2nd, n is 1st , b 0th order


line1, = plt.plot(t,y, '.' )         # Ploting values t in x, y in y axis
line2, = plt.plot(t,m*(t**2)+n*t+b)  # ploting fit line (2nd order)
plt.legend((line1,line2),('t vs y', 'fit line'))
plt.xlabel('Time (s)')
plt.ylabel('y (m)')
plt.title('y vs t graph')


plt.show()                           #Plot show

