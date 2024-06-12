# -*- coding: utf-8 -*-
"""
@author: aldocema
Taylor series 4.1 & 4.2 from chapra's book
use sympy, sympy.diff(funcion,respecto),sympy.integrate(funcion,respecto), funcion.subs(variable,valor)
"""

import numpy as np
import sympy
import math
import time
import pandas as pd

x=sympy.symbols('x')
sympy.init_printing(use_unicode=True)

f1=-(.1*x**4)-(0.15*x**3)-(0.5*x**2)-(0.25*x)+(1.2);
f2=sympy.cos(x);

#print(sympy.diff(f1))
#print(sympy.integrate(sympy.diff(f1)))
a11=0;
a12=1;
a21=np.pi/4;
a22=np.pi/3;
h1=a12-a11;
h2=a22-a21;
n=8;
z=0.5;

vv1=f1.subs(x,a12)
vv2=f2.subs(x,a22)
def serie_Taylor(f,a1,a2,n,z,vv):
    t1=time.time()
    aprox=0;
    h=a2-a1;
    m=pd.DataFrame()
    temp=[]
    for i in range(n):
        temp.append(i);
        temp.append(f);
        aprox=aprox+((f.subs(x,a1)/math.factorial(i))*h**(i)) #serie de taylor
        temp.append(aprox)
        erp=((vv-aprox)/vv)*100
        temp.append(erp)
        f=sympy.diff(f)
        m=m.append(pd.Series(temp),ignore_index=True)
        temp.clear()
        #print(aprox)
    
    fint=sympy.integrate(f,x)
    r_n=(fint.subs(x,z)/math.factorial(n+1))*(h**(n+1)) #calculo de r_n
    t2=time.time()
    print('tiempo de ejecución: ',t2-t1)
    print('r_n=',r_n)
    m.columns=['orden n','f(n)(x)','f(x)','et']
    print(m)
    aprox=aprox+r_n
    return aprox


res=serie_Taylor(f1, a11, a12, n, z,vv1)
print('Valor verdadero: ',f1.subs(x,a12),'Evaluación de f1',res)
res=serie_Taylor(f2, a21, a22, n, z,vv2)
print('valor verdadero: ',f2.subs(x,a22),'Evaluación de f2',res)