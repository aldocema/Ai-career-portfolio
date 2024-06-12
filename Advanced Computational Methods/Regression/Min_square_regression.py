# Linear Regression using Least Squares Method

"""
@author: aldocema
This program performs linear regression using the method of least squares, 
as outlined in Chapter 5 of Chapra's book.

The method of least squares is a technique used to find the best-fitting 
line to a set of data points. It minimizes the sum of the squares of the 
differences between the observed values and the values predicted by the line, 
allowing determination of the coefficients of the regression line equation
"""

import numpy as np
import math
import matplotlib.pyplot as plt

def linear_regression(x, y):
    """
    Performs linear regression using the method of least squares.

    Parameters:
    x (array-like): The independent variable data.
    y (array-like): The dependent variable data.

    Returns:
    array-like: The predicted values of the dependent variable.
    """

    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x * y)
    sum_x2 = sum(x**2)
    sum_y2 = sum(y**2)
    promx = x.mean()
    promy = y.mean()

    A = np.array([[n, sum_x], [sum_x, sum_x2]])
    b = np.array([[sum_y], [sum_xy]])

    res = np.linalg.inv(A).dot(b)
    a0 = res[0]
    a1 = res[1]

    x_aux = np.linspace(x[0], x[-1])
    y_aux = a0 + (a1 * x_aux)

    s_r = sum((y - a0 - (a1 * x))**2)  # Eq. 17.8
    s_t = sum((y - promy)**2)  # Eq. 17.10

    s_xy = math.sqrt(s_r / (n - 2))  # Eq. 17.9
    r = ((n * sum_xy) - (sum_x * sum_y)) / (math.sqrt((n * sum_x2) - (sum_x)**2) * math.sqrt((n * sum_y2) - (sum_y)**2))  # Eq. 17.11
    r2 = (s_t - s_r) / s_t

    print('r^2:', float(r2))
    print('r:', float(r))
    print('S_xy:', s_xy)
    print('s_r:', float(s_r))
    print('s_t:', float(s_t))

    plt.plot(x_aux, y_aux, 'r')
    plt.scatter(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Linear Regression')
    plt.legend(['Fitted Line', 'Data Points'])
    plt.grid()

    return y_aux

x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([0.5, 2.5, 2, 4, 3.5, 6, 5.5])

predicted_values = linear_regression(x, y)
