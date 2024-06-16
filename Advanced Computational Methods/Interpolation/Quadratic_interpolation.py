# -*- coding: utf-8 -*-
"""
Quadratic Interpolation
 It calculates the coefficients of the quadratic polynomial and then uses 
 this polynomial to predict the value at a specific point. Additionally, 
 it plots the points and the interpolated function, and calculates the error
 of the prediction. It calculates the coefficients of the quadratic polynomial 
 and then uses this polynomial to predict the value at a specific point. 
Page 506
@author: aldocema
"""

import numpy as np
import matplotlib.pyplot as plt
import time

def quadratic_interpolation(x, y, predict):
    t1 = time.time()
    b0 = y[0]
    actual_value = np.log(predict)
    f_x1_x0 = (y[1] - y[0]) / (x[1] - x[0])
    b1 = f_x1_x0
    f_x2_x1 = (y[2] - y[1]) / (x[2] - x[1])
    f_x2_x1_x0 = (f_x2_x1 - f_x1_x0) / (x[2] - x[0])
    b2 = f_x2_x1_x0
    a0 = b0 - (b1 * x[0]) + (b2 * x[1])
    a1 = b1 - (b2 * x[0]) - (b2 * x[1])
    a2 = b2
    x_res = np.arange(x[0], x[2] + 5, 0.1)
    f2_x = a0 + (a1 * x_res) + (a2 * x_res**2)
    t2 = time.time()
    print('Execution Time:', t2 - t1)
    plt.plot(x_res, f2_x, 'c')
    plt.scatter(x, y, c='b')
    
    predicted_value = a0 + (a1 * predict) + (a2 * predict**2)
    error = 100 * (actual_value - predicted_value) / actual_value
    print('Error %: ', error)
    plt.scatter(predict, predicted_value, c='c')
    plt.scatter(predict, actual_value, c='r')

x0 = 1
x1 = 3
x2 = 4
f_x0 = np.log(x0)
f_x1 = np.log(x1)
f_x2 = np.log(x2)
predict = 2
x = np.arange(x0, x2 + 4, 0.1)
y = np.log(x)

plt.plot(x, y)
plt.show()
x_points = np.array([x0, x1, x2])
y_points = np.array([f_x0, f_x1, f_x2])

quadratic_interpolation(x_points, y_points, predict)
