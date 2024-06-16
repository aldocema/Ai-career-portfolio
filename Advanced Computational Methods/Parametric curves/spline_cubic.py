# -*- coding: utf-8 -*-
"""

@author: aldo cervantes marquez
Parametric interpolation for closed figures applying cubic spline

The code implements a method to interpolate closed parametric curves using cubic splines.
It first defines a cubic polynomial for each interval between consecutive points,
ensuring that the curve passes through each point. Additionally, it enforces continuity
of the first and second derivatives at each point, which helps in creating a 
smooth curve. Finally, it solves the system of equations to find the coefficients of 
the cubic polynomials, which define the spline curve.
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

def cubic_spline_interpolation(xa, y, n):
    ren = xa.shape
    intervals = ren[0] - 1
    # Condition for interior (equal to function values) and exterior points
    c_pi = (2 * ren[0]) - 2  # 2n-2
    m_x = np.zeros((4 * intervals, 4 * intervals))
    m_y = np.zeros((4 * intervals, 1))
    c_tpi = 0
    print('number of equations for interior and exterior points: ', c_pi)
    for a in range(intervals):
        #print('a',a)
        m_x[2 * a, c_tpi] = xa[a] ** 3
        m_x[2 * a, c_tpi + 1] = xa[a] ** 2
        m_x[2 * a, c_tpi + 2] = xa[a]
        m_x[2 * a, c_tpi + 3] = 1
        m_y[2 * a, 0] = y[a]

        m_x[(2 * a) + 1, c_tpi] = xa[a + 1] ** 3
        m_x[(2 * a) + 1, c_tpi + 1] = xa[a + 1] ** 2
        m_x[(2 * a) + 1, c_tpi + 2] = xa[a + 1]
        m_x[(2 * a) + 1, c_tpi + 3] = 1
        m_y[(2 * a) + 1, 0] = y[a + 1]
        c_tpi = c_tpi + 4
    # Derivative condition, each derivative should be intervals-1
    # It can also be visualized as the number of interior points
    c_d1 = intervals - 1  # ren[0]-2
    n_d1 = 0
    print('Number of equations for first derivative: ', c_d1)
    for b in range(c_d1):
        print(b + c_pi)
        m_x[b + c_pi, n_d1] = 3 * xa[b + 1] ** 2
        m_x[b + c_pi, n_d1 + 1] = 2 * xa[b + 1]
        m_x[b + c_pi, n_d1 + 2] = 1
        m_x[b + c_pi, n_d1 + 3] = 0

        # second part of the equality
        n_d1 = n_d1 + 4
        m_x[b + c_pi, n_d1] = -3 * xa[b + 1] ** 2
        m_x[b + c_pi, n_d1 + 1] = -2 * xa[b + 1]
        m_x[b + c_pi, n_d1 + 2] = -1
        m_x[b + c_pi, n_d1 + 3] = 0
        m_y[b + c_pi, 0] = 0
    # Second derivative condition in interior points should be equal to the next
    c_d2 = c_d1  # equal
    cont = c_pi + b + 1  # to know in which equation we are
    n_d2 = 0
    print('equations of second derivative in interior points: ', c_d2)
    for c in range(c_d2):
        m_x[c + cont, n_d2] = 6 * xa[c + 1]
        m_x[c + cont, n_d2 + 1] = 2
        # Second part of the equality
        n_d2 = n_d2 + 4
        m_x[c + cont, n_d2] = -6 * xa[c + 1]
        m_x[c + cont, n_d2 + 1] = -2
        m_y[c + cont, 0] = 0
    print('Equations of second derivative at end points: 2')
    m_x[-2, 0] = 6 * xa[0]
    m_x[-2, 1] = 2
    m_y[-2, 0] = 0
    m_x[-1, -4] = 6 * xa[-1]
    m_x[-1, -3] = 2
    m_y[-1, 0] = 0
    print('total parameters:', (2 + c_d1 + c_d2 + c_pi))
    #print(m_x)
    #print(m_y)
    res = np.linalg.solve(m_x, m_y)
    #print(res)
    x_res = []
    y_res = []
    temp = 0
    for p in range(intervals):
        print('Interval', p + 1, 'from', xa[p], 'to', xa[p + 1])
        int_p = res[temp] * x ** 3 + res[temp + 1] * x ** 2 + res[temp + 2] * x + res[temp + 3]
        print(int_p)

        rango = np.arange(xa[p], xa[p + 1], abs(xa[p + 1] - xa[p]) / n)
        y_int = res[temp] * rango ** 3 + res[temp + 1] * rango ** 2 + res[temp + 2] * rango + res[temp + 3]
        #plt.plot(rango,y_int)
        x_res.append(rango)
        y_res.append(y_int)
        temp = temp + 4
    #plt.scatter(xa,y)
    #plt.title('Cubic Segment Interpolation')
    #plt.xlabel('x')
    #plt.ylabel('f(x)')
    #plt.grid()
    x_res = np.stack(x_res, axis=0)
    y_res = np.stack(y_res, axis=0)
    g, k = x_res.shape
    x_res = np.reshape(x_res, (1, g * k))
    y_res = np.reshape(y_res, (1, g * k))
    inter = np.vstack((x_res, y_res))
    return inter

x = sym.Symbol('x')
sym.init_printing(use_unicode=True)

xi = np.array([0, 0, 1, 1, 0])
fi = np.array([0, 1, 1, 0, 0])

## Gingerbread man
"""
xi=np.array([0,1.1,2.5,3.5,4,4.2,3.9,3,4,5.4,7.2,8.5,9.3,8.2,6.9,
             5,4,4,4.2,4.9,5.8,6.4,5.5,3,1.8,0.8,-.2,-1.2,-1.7,-2.2,
             -2.6,-3.8,-5.2,-6.4,-6.7,-6.2,-5.2,-4.7,-4.5,-4.5,-4.6,-5.6,-6.7,-8.2,-9.3,
             -9.3,-7.4,-5.4,-3.8,-3.2,-4.4,-4.4,-3.9,-2.5,-1.2,0,1.1])

fi=np.array([11.5,11.4,10.7,9.7,8.2,7,5.5,4.2,3.8,3.5,2.8,2.2,0,-1.2,-1.1,
             -0.8,-0.6,-2.4,-5,-6.6,-8.3,-9.8,-11.7,-11.7,-10.5,-8.3,-7.3,-7.4,-8.5,-9.8,
             -11.2,-12.3,-12.3,-11.4,-9.4,-8.2,-6.8,-5.2,-3.7,-2,-.5,-.4,-1,-1.2,0,
             2.1,2.9,3.5,3.9,4.2,6,8,9.5,10.9,11.3,11.5,11.4])
## /Gingerbread man
"""
leng_1 = xi.shape  # Size of the array
h = np.linspace(0, 1, leng_1[0])  # Step size according to the size of the array (points)

## Cubic evaluation of the step with respect to each axis
coordx = cubic_spline_interpolation(h, xi, 1000)
coordy = cubic_spline_interpolation(h, fi, 1000)

## Print results
plt.figure()  ## Cubic interpolation figure in closed figure
plt.plot(coordx[1, :], coordy[1, :])
plt.scatter(xi, fi, c='r')
plt.title('Parametric interpolation with cubic spline for closed figures')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

plt.figure()  # Figure of x behavior in the steps that were evaluated
plt.plot(coordx[1, :])
plt.title('x(t_i)')
plt.grid()

plt.figure()
plt.plot(coordy[1, :])
plt.title('y(t_i)')
plt.grid()
plt.show()
