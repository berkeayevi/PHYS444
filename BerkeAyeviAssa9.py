# -*- coding: utf-8 -*-
"""
Created on Thu May 27 12:46:38 2021

@author: BerkeAyevi
"""

import numpy as np
import matplotlib.pyplot as plt

# limits
a = 0.0
b = 1.0

N = 100  # steps

h = (b-a)/N  # step size

IV = (0.0, 1.0)  # initial value v(0)=1


def f(t, v):  # Diff Equation
    return 1 - 2.0*v**2 - t

# making arrays to hold t and v

t = np.arange(a,b+h,h)
w = np.zeros((N+1,))

t[0], w[0] = IV
# Euler's Methode

for i in range(1, N+1):

    w[i] = w[i-1] + h * f(t[i-1], w[i-1])


plt.xlabel("t")
plt.ylabel("v(t)")
plt.plot(t, w, label="Approximation")
plt.title("Euler's Methode")

plt.legend()
plt.show()

