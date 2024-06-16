# -*- coding: utf-8 -*-
"""
Linear interpolation function
Aldo Cervantes Marquez.

It calculates the slope between each pair of consecutive points and then generates
points along a straight line connecting them. The resulting line is plotted
along with the original points for comparison.
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

def linear_interpolation(xa,y,n):
    row=xa.shape
    m=0
    f=0
    for ii in range(row[0]-1):
        m=(y[ii]-y[ii+1])/(xa[ii]-xa[ii+1])
        xn=np.arange(xa[ii],xa[ii+1],((abs(xa[ii+1]-xa[ii]))/n))
        f=(m*(xn-xa[ii]))+y[ii]

        plt.plot(xn,f)
    plt.scatter(xa,y)
    plt.grid()

x=sym.Symbol('x')
sym.init_printing(use_unicode=True)

xi=np.array([0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5.0, 6.0, 7.0, 8.0,9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3])
fi=np.array([1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25])

linear_interpolation(xi,fi,1000)

plt.show()
