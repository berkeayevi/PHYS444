"""
Created on Thu Apr  15 12:56:00 2021

@author: BerkeAyevi
"""


def heatflux(x): # heat flux calculation function takes derivative as a input
    k = 3.5 * (10 ** -7)  # coefficient of thermal diffusivity in soil (m^2/s)
    p = 1800  # soil density (kg/m^3)
    C = 840  # soil specific heat (J/(kg*C))
    dTdz = x # Derivative

    result = -1 * k * p * C * dTdz #Calculation

    return result # returns result


def FD(data): # FD caluclation function takes the data and returns result
    fz = data[0][1] # f(z)   => f(0)= 13.5
    fzh= data[1][1] # f(z+h) => f(0+1.25)= 12
    h= 1.25 #h
    df = (fzh-fz)/h # FD formula taken from slayts pg 18

    result = heatflux(df) #heat flux calculation

    return  print('FD = ',result) #prints result


def MFD(data): # MFD caluclation function takes the data and returns result
    fz   = data[0][1]# f(z)    => f(0)= 13.5
    fzh  = data[1][1]# f(z+h)  => f(0+1.25)= 12
    fz2h = data[2][1]# f(z+2h) => f(0+2.5)= 10
    h = 1.25 # h
    df = (-fz2h+ 4 * fzh - 3* fz) / (2*h) # Modified FD formula taken from slayts pg 32

    result = heatflux(df) #heat flux calculation

    return  print('MFD = ',result) #prints result




data = [[0,13.5],[1.25,12],[2.5,10]]

FD(data)
MFD(data)
