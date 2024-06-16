# -*- coding: utf-8 -*-
"""
Runge-Kutta Method 3
Obtained from Chapra's Numerical Methods book.
Using formula 25.39 from chapter 25.3.2
@author: Aldo Cervantes Marquez
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import time
import pandas as pd

# Symbolic variables definition
x=sym.Symbol('x')
y=sym.Symbol('y')
sym.init_printing(use_unicode=True)

def rk3(f,vv,start,end,h):
    r1=[]
    r1.append(vv[0])
    y1=0
    for a in np.arange(start+h,end+h,h):
        # Calculation of coefficients k for summation
        a2=a-h
        k1=float(f.subs({x:a2,y:r1[-1]})) # Formula 25.39a
        k2=float(f.subs({x:(a2+(0.5*h)),y:(r1[-1]+(0.5*k1*h))})) # Formula 25.39b
        k3=float(f.subs({x:(a2+h),y:(r1[-1]-(k1*h)+(2*k2*h))})) # Formula 25.39c
        y1=r1[-1]+((h/6)*(k1+(4*k2)+(k3)))
        r1.append(y1)
    r1=np.around(r1,7)
    r1=np.stack(r1,axis=0) # Convert from list to np.array
    return r1

# Function to evaluate
f1=4*sym.exp(0.8*x)-0.5*y

# Evaluation boundaries
xi=0
xf=4
h=abs(-xi+xf)/4 # Step size plus initial condition
# Solution
fsol=(4/1.3)*(sym.exp(0.8*x)-sym.exp(-0.5*x))+(2*sym.exp(-0.5*x))
v_v=[]
xit=[]
for a in np.arange(xi,xf+h,h):
    xit.append(a)
    sol=fsol.subs(x,a)
    v_v.append(float(sol))
## Initial conditions
x0=0
y0=2

t1=time.time()
res=rk3(f1,v_v,xi,xf,h)
t2=time.time()
print('Execution time:',t2-t1)
error=(res-v_v)/v_v # Error calculation
error*=100
error=np.round(error,2)
# Results printing
xit=np.stack(xit,axis=0)
v_v=np.stack(v_v,axis=0)
total=np.vstack((xit,v_v))
total=np.vstack((total,error))
total=np.vstack((total,res))
total=np.transpose(total)
df=pd.DataFrame(total,columns=['x','y_v','E%','rk3'])
print(df)
## Results plotting
plt.plot(xit,v_v)
plt.plot(xit,res)
plt.legend(['Exact solution','Runge-Kutta 3 solution'])
plt.scatter(xit,v_v)
plt.scatter(xit,res)
plt.title('Runge-Kutta 3 Method')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()