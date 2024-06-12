# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 16:45:47 2022

@author: aldoa
This code performs polynomial regression, fitting a polynomial of degree n 
to the data points x and y. It calculates the coefficients of the polynomial 
and evaluates the coefficient of correlation (r). Finally, it plots the original
 data points and the regression curve.
"""
import numpy as np
import math
import matplotlib.pyplot as plt
import time


def polynomial_regression(x, y, n):
    A = np.zeros((n+1, n+1))
    mean_y = y.mean()
    b = np.zeros((n+1, 1))
    counter = 0
    for col in range(0, n+1):
        for row in range(0, n+1):
            if col == 0 and row == 0:
                A[row, col] = len(x)
            else:
                A[row, col] = sum(x**(counter+row))
        counter += 1
    
    for o in range(n+1):
        b[o, 0] = sum(x**(o)*y)
    
    res = np.linalg.inv(A).dot(b)
    print(x.shape)
    s_t = 0
    s_r = 0
    predicted_y = []
    eval_temp = 0
    for ll in range(len(x)):
        for sust in range(len(res)):
            eval_temp = eval_temp + (res[sust, 0]*(x[ll,]**(sust)))
        predicted_y.append(eval_temp)
        eval_temp = 0
        s_r = s_r + (y[ll,]-predicted_y[-1])**2
        s_t = s_t + (y[ll,]-mean_y)**2
    r = math.sqrt((s_t-s_r)/(s_t))
    print('Result:', res)
    print('Coefficient of correlation: ', r)
    plt.scatter(x, y)
    plt.plot(x, predicted_y, color='red')
    plt.grid()
    plt.title('Polynomial Regression')
    return [res, r]

x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([0.5, 2.5, 2, 4, 3.5, 6, 5.5])

t1 = time.time()
[res, r] = polynomial_regression(x, y, 4)
t2 = time.time()
print('Execution time: ', t2-t1, 'seconds')
