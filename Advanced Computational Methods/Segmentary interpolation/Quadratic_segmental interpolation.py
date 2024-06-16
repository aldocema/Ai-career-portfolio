# -*- coding: utf-8 -*-
"""
Quadratic segmental interpolation
@author: aldocema (Aldo Cervantes Marquez)
Taking formulas from Chapra's book chapter 18.6.2
formulas 18.28-.33
The interpolation is done between specified points (xa, ya) and aims 
to find a quadratic function that passes through these points. 
The function then plots the interpolated curve along with the original points for comparison.
"""

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def quadratic_interpolation(xa, y, n):
    row=xa.shape
    if row[0]<=0:
        return 'error'
    interval=row[0]-1
    variables=3*interval
    conditions=(2*interval)-2
    ends=2
    continuity=interval-1
    variables=variables-1
    m_values=np.zeros((variables,variables+1))
    # Filling conditions matrix
    a=0
    b=0
    c=0
    m_results=np.zeros((conditions+ends+continuity,1))
    for ii in range(int(conditions/2)): #conditions
       #cond1
       a=xa[ii+1]**2
       m_values[(ii*2),ii*3]=a # for a
       b=xa[ii+1]
       m_values[(ii*2),(ii*3)+1]=b # for b  eq,variables
       c=1
       m_values[ii*2,(ii*3)+2]=c
       m_results[(ii*2),0]=y[ii+1]
       #cond2 
       a=xa[ii+1]**2
       m_values[(ii*2)+1,(ii+1)*3]=a # for a
       b=xa[ii+1]
       m_values[(ii*2)+1,((ii+1)*3)+1]=b # for b  eq,variables
       c=1
       m_values[(ii*2)+1,((ii+1)*3)+2]=c
       m_results[(ii*2)+1,0]=y[ii+1]
       
    #Ends
    ii=(ii*2)+1
    a=xa[0]**2
    m_values[ii+1,0]=a
    b=xa[0]
    m_values[ii+1,1]=b
    c=1
    m_values[ii+1,2]=c
    m_results[ii+1,0]=y[0]
    ii=ii+1        
    a=xa[-1]**2
    m_values[ii+1,-3]=a
    b=xa[-1]
    m_values[ii+1,-2]=b
    c=1
    m_values[ii+1,-1]=c
    m_results[ii+1,0]=y[-1]
    ii=ii+1
    # Continuity
    for jj in range(continuity):
        a=2*xa[jj+1]
        m_values[jj+ii+1,jj*3]=a
        b=1
        m_values[jj+ii+1,(jj*3)+1]=b
        a=-2*xa[jj+1] ## equality
        m_values[jj+ii+1,(jj+1)*3]=a
        b=-1
        m_values[jj+ii+1,((jj+1)*3)+1]=b
        #print((jj*3)+1)

    m_values=np.delete(m_values,0,1) #elimination of auxiliary value
    m_const=np.linalg.solve(m_values,m_results) # Equation solution
    m_const=np.insert(m_const,0,0) # a1 equalization to 0
    ## Graphing results
    step=0
    for h in range(row[0]-1):
        step=np.arange(xa[h],xa[h+1],abs(xa[h+1]-xa[h])/n)
        print('Interval',h+1,'from',xa[h],'to',xa[h+1])
        int_p=(m_const[h*3,]*(x**2))+(m_const[(h*3)+1,]*x)+m_const[(h*3)+2,]
        print(int_p)

        y_res=(m_const[h*3,]*(step**2))+(m_const[(h*3)+1,]*step)+m_const[(h*3)+2,]
        plt.plot(step,y_res,linewidth=2) ## Color change
        
    plt.scatter(xa,y,linewidths=4)
    plt.title('Quadratic Segmental Interpolation')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.show()

x=sym.Symbol('x')
sym.init_printing(use_unicode=True)

xi=np.array([3, 4.5, 7, 9])
fi=np.array([2.5, 1, 2.5, 0.5])

#xi=np.array([0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5.0, 6.0, 7.0, 8.0,9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3])
#fi=np.array([1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25])
#x_infa_pato=np.array([0.817,0.897,1.022,1.191,1.51,1.834,2.264,2.962,3.624,4.202,4.499,4.779,5.109,5.527])
#y_infa_pato=np.array([1.18,1.065,1.023,1.01,1.032,1.085,1.192,1.115,1.087,1.1,0.83,0.608,0.35,0.106])
#xy=np.transpose(pato())

quadratic_interpolation(xi, fi, 10000)
