# -*- coding: utf-8 -*-
"""
Aldo Cervantes Marquez
Chapter 25.1 Euler's Method
Formula 25.2 

This code implements Euler's Method to approximate solutions of first-order ordinary differential equations.
"""

import numpy as np
import sympy as sym
import pandas as pd 
import matplotlib.pyplot as plt

# Function for Euler's Method
def euler_method(start, end, h, f, vv):
    r_euler=[]
    r_euler.append(vv[0,0])
    for aa in np.arange(start, end, h):
        yy=float(r_euler[-1]+(f.subs(x,aa))*h)
        r_euler.append(yy)
    r_euler=np.stack(r_euler,axis=0)
    return r_euler

# Function to calculate errors
def errors(xi, xf, v_m, vv, f1, n, h):
    ## Global Relative Percentage Error
    e_rg=(vv[:,0]-v_m[:,0])/vv[:,0]
    e_rg*=100
    e_rg=e_rg.astype(float)

    e_rg=e_rg.round(1)
    f_temp=0
    erpl=[]
    paso=np.arange(xi,xf,h)
    
    ren=paso.shape
    #print(paso)
    for l in range(ren[0]):   # Formula 25.2 para cada valor del 
        for o in range(n):
            f_temp=float(f_temp+((((float(sym.diff(f1,x,o+1).subs(x,paso[l,])))/float((sym.factorial(o+2))))*h**(o+2))))
            #print(f_temp,'o:',o+2)
        #print(f_temp,l,v_m[l])
        erpl.append(f_temp)
        
        f_temp=0
    #print(erpl)
    erpl.insert(0,0)
    erpl=np.stack(erpl,axis=0)
    erpl=(erpl*100)/vv[:,0]
    erpl=erpl.round(1)
    error=np.vstack((e_rg,erpl)).T
    #print(error.shape)
    return error

# Symbolic variables
x=sym.Symbol('x')
y=sym.Symbol('y')
sym.init_printing(use_unicode=True)

# Differential equation
f1=-2*x**3+12*x**2-20*x+8.5

## Initial Condition
xci=0
yci=1
#f1=f1+xci
xi=0
xf=4
h=0.5 # Step size

# Exact solution calculation
s_e=[]
xit=[]
for a in np.arange(xi,xf+h,h):
    s_e.append(float(sym.integrate(f1,x).subs(x,a)+yci)) #Exact solution
    xit.append(a)
s_e_len=len(s_e)
s_e=np.stack(s_e,axis=0)
s_e=np.reshape(s_e,(s_e_len,1))
res=euler_method(xi,xf,h,f1,s_e)
res_l=res.shape
res=np.reshape(res,(res_l[0],1))

# Error calculation
err=errors(xi,xf,res,s_e,f1,4,h)
# Results printing

xit_len=len(xit)
xit=np.stack(xit,axis=0)
xit=np.reshape(xit,(xit_len,1))
s_e=np.hstack((xit,s_e))
total=np.hstack((s_e,res))
total=np.hstack((total,err))
df=pd.DataFrame(total,columns=['x','V_real','V_e','Epg %','Epl %'])
print(df)

# Plotting
plt.plot(xit,s_e[:,1])
plt.plot(xit,res)
plt.legend(['Exact solution','Euler solution'])
plt.scatter(xit,s_e[:,1])
plt.scatter(xit,res)
plt.title('Euler\'s Solution')
plt.grid()
plt.show()
