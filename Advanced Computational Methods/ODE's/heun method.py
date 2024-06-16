# -*- coding: utf-8 -*-
"""
Heun's Method
Aldo Cervantes Marquez

The Heun's Method script implements the Heun's method for solving second-order 
differential equations. It includes a function for Heun's method, which uses a 
predictor-corrector approach to approximate the solution. The script also 
calculates and displays the error between the exact solution and the Heun's method solution.

"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import pandas as pd

x=sym.Symbol('x')
y=sym.Symbol('y')
sym.init_printing(use_unicode=True)

def heun(f,vv,start,end,h,corr): # Heun's Method for second order
    r1=[]
    r1.append(vv[0]) # Add initial value
    y0=0
    yy=0
    for aa in np.arange(start+h,end+h,h):
        m=float(f.subs({x:aa-h,y:r1[-1]})) # Slope calculation y'_0
        
        y0=r1[-1]+(m*h) # Predictor m1_euler y^0 _i+1
        y_temp=float(f.subs({x:aa,y:y0}))
        
        for bb in range(corr): # Corrector iterations
            yy=r1[-1]+(((m+y_temp)/2)*h) # Corrector y_i 
            y_temp=float(f.subs({x:aa,y:yy}))
        r1.append(yy)
    r1=np.around(r1,7)
    r1=np.stack(r1,axis=0)
    print('Corrector iterations:',corr)
    return(r1)

# Function to solve
f1=4*sym.exp(0.8*x)-0.5*y

# Evaluation boundary
xi=0
xf=4
h=abs(-xi+xf)/4 # Step size

# Solution
fsol=(4/1.3)*(sym.exp(0.8*x)-sym.exp(-0.5*x))+(2*sym.exp(-0.5*x))
v_v=[]
xit=[]
for a in np.arange(xi,xf+h,h):
    xit.append(a)
    sol=fsol.subs(x,a)
    v_v.append(float(sol))

# Initial conditions
x0=0
y0=2

m2_heun=heun(f1,v_v,xi,xf,h,10)
error=(m2_heun-v_v)/v_v # Error calculation
error*=100
error=error.round(2)

# Display results
total=np.vstack((xit,v_v))
total=np.vstack((total,error))
total=np.vstack((total,m2_heun))
total=np.transpose(total)
df=pd.DataFrame(total,columns=['x','y_v','E%','y_heun'])
print(df)

plt.plot(xit,v_v)
plt.plot(xit,m2_heun)
plt.legend(['Exact solution','Heun solution'])
plt.scatter(xit,v_v)
plt.scatter(xit,m2_heun)
plt.title('Heun\'s Method Solution')
plt.grid()
plt.show()
