# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 17:41:09 2022
@author: aldoa

The lin_reg function implements linear regression with a power law model. 
It transforms the input x values to a logarithmic scale and then calculates 
the corresponding y values using the power law model with parameters alpha and beta.
Finally, it plots the logarithmic data points.
"""
import numpy as np
import matplotlib.pyplot as plt

def lin_reg(x, y, alpha, beta):
    # Transform x to logarithmic scale
    log_x = np.log10(x)
    # Apply power law model to y with parameters alpha and beta
    log_y = alpha * log_x**(beta)
    print(log_x, log_y)
    plt.plot(log_x, log_y)
    
    
x = np.array([1, 2, 3, 4, 5])
y = np.array([0.5, 1.7, 3.4, 5.7, 8.4])

alpha = 0.5
beta = 1.75

lin_reg(x, y, alpha, beta)
