# -*- coding: utf-8 -*-
"""
Parametric curves with Lagrange interpolation.

This script demonstrates the generation of parametric curves using Lagrange interpolation.
@author: aldoa
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

x=sym.Symbol('x')
sym.init_printing(use_unicode=True)


def lagrange(xa,y):
    """
    Lagrange interpolation.

    Args:
    - xa: Array of x values.
    - y: Array of y values.

    Returns:
    - Lagrange interpolation polynomial.
    """
    x=sym.Symbol('x')
    sym.init_printing(use_unicode=True)
    row=xa.shape
    fun=1
    f_final=0
    for ii in range(row[0]):
        for jj in range(row[0]):
            if jj != ii:
                fun=fun*((x-xa[jj])/(xa[ii]-xa[jj]))
            
        f_final=f_final+(fun*y[ii])
        fun=1
    res=f_final
    return res


def curve_parametric(fx,fy,n,xa,y):
    """
    Plot parametric curve.

    Args:
    - fx: Parametric function for x.
    - fy: Parametric function for y.
    - n: Array of parameter values.
    - xa: Array of x values.
    - y: Array of y values.
    """
    fxf=sym.lambdify(x,fx,'numpy')
    fyf=sym.lambdify(x,fy,'numpy')
    xx=fxf(n)
    yy=fyf(n)
    plt.figure()
    plt.scatter(xa,y,c='r')
    plt.plot(xx,yy)
    plt.title('Parametric Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()

    plt.figure()
    plt.plot(xx)
    plt.title('x(t)')
    plt.grid()

    plt.figure()
    plt.plot(yy)
    plt.title('y(t)')
    plt.grid()

#xi =np.array([-1, 0, 1, 0, 1])
#fi =np.array([0, 1, 0.5, 0, -1])

xi=np.array([0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5.0, 6.0, 7.0, 8.0,9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3])
fi=np.array([1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25])
lagrange_x=lagrange(np.linspace(0,1,xi.shape[0]),xi)
lagrange_y=lagrange(np.linspace(0,1,fi.shape[0]),fi)
parameter=np.linspace(0,1,xi.shape[0])

curve_parametric(lagrange_x,lagrange_y,parameter,xi,fi)

plt.show()
