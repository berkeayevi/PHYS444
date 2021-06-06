# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 13:03:17 2021

@author: BerkeAyevi
"""
import math
import matplotlib.pyplot as plt


def equation(x, u):  # The equation to beb solve
    return (x ** 2.0) * math.exp(-1.0 * (u + 1.0))


def RK2(eqn, y_i, x_i, x_f, h, a):  # eqn, y_i&x_i = initial value of y&x, x_f = final position,
    x = [x_i]  # initialization of array for x
    y = [y_i]  # initialization of array for x
    while x[-1] < x_f:  # settings boundaries
        xx = x[-1]  # 0th element of x
        yy = y[-1]  # 0th element of y
        #  calculation of k1 and k2 according to lecture notates
        k1 = h * eqn(xx, yy)
        k2 = h * eqn(xx + (a * h), yy + (a * k1))
        yn = yy + (1.0 - (1.0 / (2.0 * a))) * k1 + (1.0 / (2.0 * a)) * k2

        x.append(xx + (a * h))  # adding calculated values to the array
        y.append(yn)  # adding calculated values to the array

    return x, y


# u(0) = 1, 0 =< x =< 3 , h= 0.01, a = 1
y_i = 1.0  # initial value for y
x_i = 0.0  # initial value for x
x_f = 3.0  # final value for x
h = 0.01
a = 1.0

x, y = RK2(equation, y_i, x_i, x_f, h, a)
plt.xlabel("x")
plt.ylabel("u")
plt.title("RK2")
plt.plot(x, y)

plt.show()
