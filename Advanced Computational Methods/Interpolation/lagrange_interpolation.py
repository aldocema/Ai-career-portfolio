# -*- coding: utf-8 -*-
"""

It constructs the Lagrange interpolating polynomial and then uses 
this polynomial to plot the function over a specified range. 
The code also plots the original points and the interpolated function on a graph.
@author: aldoa

Obtained from http://blog.espol.edu.ec/analisisnumerico/interpolacion-de-lagrange/#:~:text=El%20polinomio%20de%20interpolaci%C3%B3n%20de,las%20distancias%20x%20entre%20puntos.
"""

# Lagrange Interpolation
# divisoresL only to show values
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# INPUT, Test Data
#xi = np.array([0, 0.2, 0.3, 0.4])
#fi = np.array([1, 1.6, 1.7, 2.0])

xi = np.array([0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5.0, 6.0, 7.0, 8.0, 9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3])
fi = np.array([1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25])

def lagrange(xa, y):
    rows = xa.shape
    term = 1
    final_function = 0
    for ii in range(rows[0]):  # Application of recursive formula
        for jj in range(rows[0]):
            if jj != ii:
                term = term * ((x - xa[jj]) / (xa[ii] - xa[jj]))
            
        final_function = final_function + (term * y[ii])
        term = 1
    result = final_function
    return result

x = sym.Symbol('x')  # declare the symbolic variable
sym.init_printing(use_unicode=True)

n = 100000
range_vals = np.arange(xi[0], xi[-1], abs(xi[-1] - xi[0]) / n)
ff = lagrange(xi, fi)
ffinal = sym.lambdify(x, ff)

## Print results
plt.plot(range_vals, ffinal(range_vals))
plt.scatter(xi, fi, c='r')
plt.title('Lagrange Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
