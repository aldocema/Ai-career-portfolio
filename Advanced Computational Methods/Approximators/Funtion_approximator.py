# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 13:03:01 2022

@author: aldocema
"""
import math
import numpy as np
import time
import matplotlib.pyplot as plt

tic=time.time()
tac=time.time()

def aprox_ex(n,x):
    tic=time.time()
    vv=math.exp(x) # valor verdadero
    serie_ex=0
    #iteracion=[]
    l_ev=0
    aact=0
    ea=0
    aant=0
    res=np.zeros((3,n))
    for i in range(0,n):
        serie_ex=serie_ex+ (x**i/math.factorial(i)) #suma para la aproximación (serie) 
        va=serie_ex
        res[0,i]=i+1 #numero de iteración
        l_ev=abs((vv-va)/vv)*100 #formula de error verdadero y es puesto en una lista
        res[1,i]=l_ev #almacenamiento de error 
        
        aant=aact
        aact=serie_ex
        ea=abs((aact-aant)/aact)*100
        res[2,i]=ea

    print('El valor final de la serie es: ',serie_ex)
    #time.sleep(1)
    tac=time.time()
    print('El tiempo de ejecución es: ',tac-tic) 
    return res


def aprox_sin(n,x):
   tic=float(time.time())
   vv=math.sin(x) # valor verdadero
   serie_sin=0
   #iteracion=[]
   l_ev=0
   aact=0
   ea=0
   aant=0
   res=np.zeros((3,n))
   for i in range(0,n):
       sumas=(x**((2*i)+1)/math.factorial((2*i+1)))
       if i%2!=0:
           sumas=-sumas
       serie_sin=serie_sin + sumas #suma para la aproximación (serie) 
       va=serie_sin
       res[0,i]=i+1 #numero de iteración
       l_ev=abs((vv-va)/vv)*100 #formula de error verdadero y es puesto en una lista
       res[1,i]=l_ev #almacenamiento de error 
       
       aant=aact
       aact=serie_sin
       ea=abs((aact-aant)/aact)*100  #error aproximado
       res[2,i]=ea

   print(serie_sin)
   #time.sleep(1)
   tac=float(time.time())
   print(tac-tic) 
   return res 
    
"""
def prueba(n,x):
  sumas=0
  serie_ex=0
  for i in range(0,n):
      sumas=(x**((2*i)+1)/math.factorial((2*i+1)))
      if i%2!=0:
          sumas=-sumas
      serie_ex=serie_ex + sumas #suma para la aproximación (serie) 
  return serie_ex
"""

def aprox_cos(n,x):
    tic=float(time.time())
    vv=math.cos(x) # valor verdadero
    serie_cos=0
    #iteracion=[]
    l_ev=0
    aact=0
    ea=0
    aant=0
    res=np.zeros((3,n))
    for i in range(0,n):
        sumas=(x**((2*i))/math.factorial((2*i)))
        if i%2!=0:
            sumas=-sumas
        serie_cos=serie_cos + sumas #suma para la aproximación (serie) 
        va=serie_cos
        res[0,i]=i+1 #numero de iteración
        l_ev=abs((vv-va)/vv)*100 #formula de error verdadero y es puesto en una lista
        res[1,i]=l_ev #almacenamiento de error 
        
        aant=aact
        aact=serie_cos
        ea=abs((aact-aant)/aact)*100  #error aproximado
        res[2,i]=ea

    print(serie_cos)
    #time.sleep(1)
    tac=float(time.time())
    print(tac-tic) 
    return res 
    
    
    

resultado=aprox_ex(15, 0.5)
plt.scatter(resultado[0,],resultado[1,],color='r')
plt.plot(resultado[0,],resultado[1,],color='r',label='Error verdadero')
plt.scatter(resultado[0,],resultado[2,],color='b')
plt.plot(resultado[0,],resultado[2,],color='b',label='Error aproximado')
plt.grid()
plt.xlabel('Iteración (n)')
plt.ylabel('Porcentaje (%)')
plt.title('cos(x) evaluada en pi/4')
plt.legend()
plt.show()