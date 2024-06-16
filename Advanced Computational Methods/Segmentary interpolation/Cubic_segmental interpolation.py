# -*- coding: utf-8 -*-
"""
Cubic segmental interpolation
@author: aldocema (Aldo Cervantes Marquez)
It calculates the coefficients of cubic polynomials for each segment between 
the given points, ensuring continuity of the function and its first and 
second derivatives. The resulting curve is then plotted along with the 
original points for comparison.
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym


x=sym.Symbol('x')
sym.init_printing(use_unicode=True)

def duck():
    ## Duck's complete shape
    ## Duck's upper part
    xsup_duck=np.array([0.9,1.3,1.9,2.1,2.6,3,3.9,4.4,4.7,5,6,
                        7,8,9.2,10.5,11.3,11.6,12,12.6,13,13.3])
    ysup_duck=np.array([1.3,1.5,1.85,2.1,2.6,2.7,2.4,2.15,2.05,2.1,2.25,2.3,2.25,1.95,1.4,0.9,0.7,
                        0.6,0.5,0.4,0.25])

    ## Duck's lower part
    x_inf_duck=np.array([0.817,0.897,1.022,1.191,1.51,1.834,2.264,2.962,3.624,4.202,4.499,4.779,5.109,5.527])
    y_inf_duck=np.array([1.18,1.065,1.023,1.01,1.032,1.085,1.192,1.115,1.087,1.1,0.83,0.608,0.35,0.106])

    ## Duck's lower wing
    x_inf_wing_duck=np.array([4.659,4.865,5.085,5.261,5.387,5.478,5.527])
    y_inf_wing_duck=np.array([-5.161,-4.741,-3.933,-2.951,-1.97,-0.981,0.106])

    ## Duck's upper wing
    x_sup_wing_duck=np.array([4.659,4.75,4.99,5.289,5.56,5.839,6.113,6.606,6.916,7.305,7.563,7.802,7.983,8.141,8.473,8.832,9.337,9.887,10.572,10.995,11.501
                             ,11.923,12.364,12.763,13.3])
    y_sup_wing_duck=np.array([-5.161,-5.259,-5.284,-5.268,-5.161,-4.982,-4.769,-4.286,-3.911,-3.213,-2.67
                             ,-2.176,-1.655,-1.138,-0.434,-0.514,-0.494,-0.382,-0.005,-0.09,-0.085,-0.03,0.093,0.12,0.25])

    duck_complete_x=np.hstack((np.flip(xsup_duck),x_inf_duck))
    duck_complete_y=np.hstack((np.flip(ysup_duck),y_inf_duck))

    duck_complete_x=np.hstack((duck_complete_x,np.flip(x_inf_wing_duck)))
    duck_complete_y=np.hstack((duck_complete_y,np.flip(y_inf_wing_duck)))

    duck_complete_x=np.hstack((duck_complete_x,x_sup_wing_duck))
    duck_complete_y=np.hstack((duck_complete_y,y_sup_wing_duck))
    return np.vstack((duck_complete_x,duck_complete_y))


def cubic_interpolation(xa,y,n):
    row=xa.shape
    intervals=row[0]-1
    # condition for interior points (equal to function values) and exterior points
    c_ip=(2*row[0])-2 #2n-2
    m_x=np.zeros((4*(intervals),4*(intervals)))
    m_y=np.zeros((4*intervals,1))
    c_tpi=0
    print('number of equations for interior and exterior points: ',c_ip)
    for a in range(intervals):
        #print('a',a)
        m_x[2*a,c_tpi]=xa[a]**3
        m_x[2*a,c_tpi+1]=xa[a]**2
        m_x[2*a,c_tpi+2]=xa[a]
        m_x[2*a,c_tpi+3]=1
        m_y[2*a,0]=y[a]
        
        m_x[(2*a)+1,c_tpi]=xa[a+1]**3
        m_x[(2*a)+1,c_tpi+1]=xa[a+1]**2
        m_x[(2*a)+1,c_tpi+2]=xa[a+1]
        m_x[(2*a)+1,c_tpi+3]=1
        m_y[(2*a)+1,0]=y[a+1]
        c_tpi=c_tpi+4
    
    # Condition for derivative, each derivative should be intervals-1
    # It can also be seen as the number of interior points
    c_d1=intervals-1 # row[0]-2
    print('Number of equations for first derivative: ', c_d1)
    n_d1=0
    for b in range(c_d1):
        m_x[b+c_ip,n_d1]=3*xa[b+1]**2
        m_x[b+c_ip,n_d1+1]=2*xa[b+1]
        m_x[b+c_ip,n_d1+2]=1
        m_x[b+c_ip,n_d1+3]=0
        
        n_d1=n_d1+4
        m_x[b+c_ip,n_d1]=-3*xa[b+1]**2
        m_x[b+c_ip,n_d1+1]=-2*xa[b+1]
        m_x[b+c_ip,n_d1+2]=-1
        m_x[b+c_ip,n_d1+3]=0
        m_y[b+c_ip,0]=0
    
    # Condition for second derivative at interior points should be equal to the next
    c_d2=c_d1 # same
    cont=c_ip+b+1 
    n_d2=0
    print('Equations for second derivative at interior points: ',c_d2)
    for c in range(c_d2):
        m_x[c+cont,n_d2]=6*xa[c+1]
        m_x[c+cont,n_d2+1]=2
        
        n_d2=n_d2+4
        m_x[c+cont,n_d2]=-6*xa[c+1]
        m_x[c+cont,n_d2+1]=-2
        m_y[c+cont,0]=0

    print('Equations for second derivative at exterior points: 2')
    m_x[-2,0]=6*xa[0]
    m_x[-2,1]=2
    m_y[-2,0]=0
    
    m_x[-1,-4]=6*xa[-1]
    m_x[-1,-3]=2
    m_y[-1,0]=0

    print('Total parameters:',(2+c_d1+c_d2+c_ip))

    res=np.linalg.solve(m_x,m_y)

    temp=0
    for p in range(intervals):
        print('Interval',p+1,'from',xa[p],'to',xa[p+1])
        int_p=res[temp]*x**3+res[temp+1]*x**2+res[temp+2]*x+res[temp+3]
        print(int_p)

        rango=np.arange(xa[p],xa[p+1],abs(xa[p+1]-xa[p])/n)
        y_int=res[temp]*rango**3+res[temp+1]*rango**2+res[temp+2]*rango+res[temp+3]
        plt.plot(rango,y_int)
        temp=temp+4
    plt.scatter(xa,y)
    plt.title('Cubic Segmental Interpolation')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()

x=sym.Symbol('x')
sym.init_printing(use_unicode=True)

xi=np.array([0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5.0, 6.0, 7.0, 8.0,9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3])
yi=np.array([1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6,0.5, 0.4, 0.25])

cubic_interpolation(xi,yi,100)

plt.show()
