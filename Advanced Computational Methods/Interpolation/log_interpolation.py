# -*- coding: utf-8 -*-
"""
linear interpolation of the natural logarithm function (ln(x)) using two 
given points. It plots the logarithmic function over a specified range, 
along with the points and the linear interpolations within the range. 
It also marks the interpolated values on the graph.
@author: aldocema
"""

import numpy as np
import matplotlib.pyplot as plt
import time

def evaluate(x1, x0, x):
    actual_value = np.log(x)
    x_graph = np.arange(x0, x1 + 1, 0.5)
    y_graph = np.log(x_graph)

    plt.plot(x_graph, y_graph, linewidth=3.7)
    plt.scatter(x, actual_value, c='k', linewidth=5)
    fx0 = np.log(x0)
    plt.scatter(x0, fx0, c='red', linewidth=5)
    
    for xx in range(x0, x1 + 1):
        fx1 = np.log(xx)
        f1x = fx0 + (((fx1 - fx0) / (xx - x0)) * (x - x0))
        plt.scatter(x, f1x, linewidth=2)
        plt.scatter(xx, fx1, linewidth=5)
        
        plt.plot([x0, xx], [fx0, fx1])
        # ev = 100 * ((np.log(x) - f1x) / (np.log(x)))
        # print('True Error', ev)
    
    plt.ylim(fx0 - 0.5, fx1 + 0.5)
    plt.xlim(x0 - 0.5, xx + 0.5)
    plt.title('Interpolation of ln(x) Function')
    plt.grid()
    return [xx, f1x]

evaluate(6, 1, 2)
