# -*- coding: utf-8 -*-
"""
Interpolation for n-degree

Newton's interpolation for an n-degree polynomial using given points. 
It calculates the divided differences table and uses it to construct the 
Newton interpolating polynomial. The polynomial is then used to predict values, 
and the code also plots the points and the interpolated function, 
and calculates the error of the prediction.
@author: aldocema
"""
import numpy as np
import matplotlib.pyplot as plt
import time 
import sympy as sym
from sympy import lambdify

def inter_newton(x, y, pred):
    t1 = time.time()
    div_diff = np.zeros([len(x), len(x) + 1], dtype=float)
    div_diff[:, 0] = x
    div_diff[:, 1] = y    
    
    [n_r, n_c] = div_diff.shape
    mm = 1  # check value
    for col in range(2, n_c):  # column
        for row in range(0, n_r - mm):  # row
            div_diff[row, col] = ((div_diff[row + 1, col - 1] - div_diff[row, col - 1]) / (div_diff[row + col - 1, 0] - div_diff[row, 0]))  # important: row + col - 1
        mm += 1
    div_diff[0, n_c - 1] = ((div_diff[1, -2] - div_diff[0, -2]) / (div_diff[-1, 0] - div_diff[0, 0]))
    print(div_diff)
    X = sym.Symbol('X')
    term = 1
    polynomial = 0
    o = 1
    for order in range(1, n_r):
        for mult in range(0, o):
            term = term * (X - div_diff[mult, 0])
        term = term * div_diff[0, 1 + o]
        polynomial = polynomial + term
        term = 1
        o += 1
    polynomial = polynomial + div_diff[0, 1]
    t2 = time.time()
    print('Execution Time:', t2 - t1)
    print(sym.expand(polynomial))
    plt.plot(x, y, c='r')
    plt.scatter(x, y, c='r')
    lam_x = lambdify(X, polynomial, modules=['numpy'])
    x_vals = np.linspace(x[0] - 1, x[-1] + 2, 2000)
    y_vals = lam_x(x_vals)
    plt.plot(x_vals, y_vals)
    plt.grid()
    plt.show()
    actual_value = np.log(pred)
    error = 100 * (actual_value - polynomial.subs(X, pred)) / actual_value
    print('Error %:', error)
    return polynomial

x = np.array([0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5.0, 6.0, 7.0, 8.0, 9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3])

f_x = np.array([1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3,
    2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25])

x0 = 1
x1 = 4
x2 = 5
x3 = 6
f_x0 = np.log(x0)
f_x1 = np.log(x1)
f_x2 = np.log(x2)
f_x3 = np.log(x3)
x_c = np.array([x0, x1, x2, x3])
y_c = np.array([f_x0, f_x1, f_x2, f_x3])

predict = 2
x_t = np.arange(x0, x2 + 4, 0.1)
y_t = np.log(x)
pred = 2
X = sym.Symbol('X')
function = inter_newton(x_c, y_c, pred)
