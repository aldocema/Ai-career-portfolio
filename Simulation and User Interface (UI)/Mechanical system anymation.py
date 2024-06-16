
import tkinter as tk
import sympy as sym
import numpy as np
import random
from ipycanvas import Canvas, Path2D
import time

t_1=sym.Symbol('t_1')
t_2=sym.Symbol('t_2')

## Valores iniciales del brazo
#posicion=np.array([[1.7],[0.2]])
    


a=25
ang1=0.75 #2.1 #solucion 1 #0.75 ---solucion 2
ang2=2.3#0.4             #2.3
l_1=6*a
l_2=5*a
eq1=(l_1*sym.cos(t_1))+(l_2*sym.cos(t_2))
eq2=(l_1*sym.sin(t_1))+(l_2*sym.sin(t_2))
# Agregar matrices y solucion del metodo
a11=sym.diff(eq1,t_1)
a12=sym.diff(eq1,t_2)
a21=sym.diff(eq2,t_1)
a22=sym.diff(eq2,t_2)
j=sym.Matrix([[a11,a12],[a21,a22]])
root = tk.Tk()
 
canvas_width = 800
canvas_height = 600
w, h  = canvas_width // 2, canvas_height // 2
canvas = tk.Canvas(root, width=canvas_width, height = canvas_height)
canvas.pack()
valores_x=np.arange(40,200,0.8) # ajustar valores
## Definicion de los puntos de la geometría del elemento
p1_azul=[w-a,0+h,               #1  #Figura azul inmobil
         w-a,h+a,               #2
         w-(2*a),h+a,           #3
         w-(2*a),h+(2*a),       #4
         w+(2*a),h+(2*a),       #5
         w+(2*a),h+a,           #6
         w+a,h+a,               #7
         w+a,h]                 #8

p2_vec1=np.array([[w,w,w+(6*a),w+(6*a)],[h-(1.5*a),h+(1.5*a),h+(0.5*a),h-(0.5*a)]]) #ver posiciones en otras formas
print('p2_vec1=',p2_vec1)
p2_vecr=np.array([[w-(1.5*a),w+(1.5*a)],[h-(1.5*a),h+(1.5*a)]]) #circulo verde
p2_vecr2m=np.array([[p2_vec1[0,2]+(a/2),p2_vec1[0,3]-(a/2)],[p2_vec1[1,2],p2_vec1[1,3]]]) #circulo verde mobil
p3_purp1=np.array([[w,w,w+(4*a),w+(5*a),w+(4*a)],[h+(0.5*a),h-(0.5*a),h-(0.5*a),h,h+(0.5*a)]])
p3_purp_c=np.array([[w-(a/4),w+(a/4)],[h-(a/4),h+(a/4)]]) 
p_per2_movil=np.array([[w-(a/4),w+(a/4)],[h-(a/4),h+(a/4)]]) 
"""
def actualizar():
    canvas.delete(fig_verde)
    canvas.delete(fig_c_verde)
    canvas.delete(fig_az11)
    canvas.delete(fig_az12)
    

    fig_verde=canvas.create_polygon(parametrizar(p_verde_imp),fill='green',outline='green')
    #fig_c_verde=canvas.create_oval(parametrizar(p2_vecr),fill='green',outline='green')
    fig_az11=canvas.create_polygon(p1_azul,fill='blue',outline='blue')
    fig_az12=canvas.create_arc(w-a,h-(a),w+a,h+(a),fill='blue',outline='blue',extent=180)
    root.update()
#"""
def eq_nr(xt,yt,ang1,ang2,eq1,eq2,j):
    eq1=eq1-xt
    eq2=eq2-yt
    #F=sym.Matrix([[eq1],[eq2]])
    v_f=np.array([[ang1],[ang2]])
    for it in range(100):
        b11=float(j[0,0].subs({t_1:v_f[0,0],t_2:v_f[1,0]}))
        b12=float(j[0,1].subs({t_1:v_f[0,0],t_2:v_f[1,0]}))
        b21=float(j[1,0].subs({t_1:v_f[0,0],t_2:v_f[1,0]}))
        b22=float(j[1,1].subs({t_1:v_f[0,0],t_2:v_f[1,0]}))
        e11=float(eq1.subs({t_1:v_f[0,0],t_2:v_f[1,0]}))
        e22=float(eq2.subs({t_1:v_f[0,0],t_2:v_f[1,0]}))
        if abs(e11)<0.01 and abs(e22)<0.01:
            break
        j_num=np.array([[b11,b12],[b21,b22]])
        F_num=np.array([[e11],[e22]])
        v_f=v_f-(np.linalg.inv(j_num).dot(F_num))
    return v_f
    #print('falta actualizar angulos y resolver método')

def s_p(x):  #-0.75x +0.21 #multiplicar por 1000
    y=-(0.75*x)+210
    return y
def parametrizar(pos):
    row,col=pos.shape # obtener el numero de renglones y columnas
    r=[]
    for o in range(col):
        r.append(pos[0,o])
        r.append(pos[1,o])
    return r

def mrot(t1,fig):
    if t1==0:
        print('caso 0')
        return fig
    
    row,col=fig.shape
    
    for oo in range(col):
        fig[0,oo]=fig[0,oo]-w
        fig[1,oo]=fig[1,oo]-h
    if t1<0:
        t1=abs(t1)
        m_rot=np.array([[np.cos(t1), -np.sin(t1)],[np.sin(t1),np.cos(t1)]])
        mtemp=m_rot.dot(fig)
        #print(mtemp, 'caso 1')
        for oo in range(col):
            mtemp[0,oo]=mtemp[0,oo]+w
            mtemp[1,oo]=mtemp[1,oo]+h
        return mtemp
    elif t1>0:
        t1=abs(t1)
        m_rot=np.array([[np.cos(t1), np.sin(t1)],[-np.sin(t1),np.cos(t1)]])
        mtemp=m_rot.dot(fig)
        #print(mtemp,'caso 2')
        for oo in range(col):
            mtemp[0,oo]=mtemp[0,oo]+w
            mtemp[1,oo]=mtemp[1,oo]+h
        return mtemp

    

#def pol1verde(a):
#    puntos=[w,h]


# ejes
ejex=canvas.create_line(w,0,w,canvas_height,fill='black',width=3)
ejey=canvas.create_line(0,h,canvas_width,h,fill='black',width=3)
# Figuras verdes
fig_verde=canvas.create_polygon(parametrizar(p2_vec1),fill='green',outline='green')
fig_c_verde=canvas.create_oval(parametrizar(p2_vecr),fill='green',outline='green')
fig_c2_verde=canvas.create_oval(parametrizar(p2_vecr2m),fill='green',outline='green')

#figura purpura
fig_purp=canvas.create_polygon(parametrizar(p3_purp1),fill='purple', outline='purple')
# Perno movil
fig_perno_movil=canvas.create_oval(parametrizar(p_per2_movil),fill='yellow',outline='blue')


# figura estatica azul y perno inmobil
fig_az11=canvas.create_polygon(p1_azul,fill='blue',outline='blue')
fig_az12=canvas.create_arc(w-a,h-(a),w+a,h+(a),fill='blue',outline='blue',extent=180)
fig_perno1=canvas.create_oval(w-(a/2),h-(a/2),w+(a/2),h+(a/2),fill='yellow',outline='black')
linea_sp=canvas.create_line(w+0.04*40*a,h-s_p(0.04*40*a),w+0.2*40*a,h-s_p(0.2*40*a),fill='blue',width=3.2)

root.update()

#"""

#p_verde_new=p2_vec1
valores_y=(s_p(valores_x))
valores_x=(valores_x)
#linea_eq=canvas.create_line(valores_x[0],valores_y[0],valores_x[-1],valores_y[-1],fill='red',width=3.2)
p_verde_new=mrot(ang1,p2_vec1) #rotaciones------------
p_morado_new=mrot(ang2,p3_purp1)
p_morado_imp=parametrizar(p_morado_new)
p_verde_imp=parametrizar(p_verde_new)
print(p_verde_imp)
#actualizar()
#canvas.delete(fig_verde)
#fig_verde=canvas.create_polygon(p_verde_imp,fill='green',outline='green')
canvas.delete(fig_verde)
#canvas.delete(fig_c_verde)
canvas.delete(fig_c2_verde)
#canvas.delete(fig_c2_verde)
canvas.delete(fig_az11)
canvas.delete(fig_az12)
canvas.delete(fig_perno_movil)
canvas.delete(fig_purp)
fig_purp=canvas.create_polygon(parametrizar(p_morado_new),fill='purple',outline='purple')
fig_verde=canvas.create_polygon(parametrizar(p_verde_new),fill='green',outline='green')

#canvas.move(fig_c2_verde,0,0)#(fig_c2_verde,((p_verde_imp[4]+p_verde_imp[6])/2)+w,((p_verde_imp[5]+p_verde_imp[7])/2)-h)
### Mover circulos
fig_c2_verde=canvas.create_oval(w-(a/2),h-(a/2),w+(a/2),h+(a/2),fill='green',outline='green') #circulo movil
canvas.move(fig_c2_verde,((p_verde_imp[4]+p_verde_imp[6])/2)-w,((p_verde_imp[5]+p_verde_imp[7])/2)-h)

canvas.move(fig_purp,((p_verde_imp[4]+p_verde_imp[6])/2)-w,((p_verde_imp[5]+p_verde_imp[7])/2)-h) ##-------

fig_perno_movil=canvas.create_oval(parametrizar(p_per2_movil),fill='yellow',outline='blue')
canvas.move(fig_perno_movil,((p_verde_imp[4]+p_verde_imp[6])/2)-w,((p_verde_imp[5]+p_verde_imp[7])/2)-h)
#fig_c2_verde=canvas.create_arc(p_verde_imp[4:8],fill='blue',outline='red',extent=180)#create_oval((p_verde_imp[4],p_verde_imp[5]+(1.5*a),p_verde_imp[6],+p_verde_imp[7]-(1.5*a)))
fig_az11=canvas.create_polygon(p1_azul,fill='blue',outline='blue')
fig_az12=canvas.create_arc(w-a,h-(a),w+a,h+(a),fill='blue',outline='blue',extent=180)
fig_perno1=canvas.create_oval(w-(a/2),h-(a/2),w+(a/2),h+(a/2),fill='yellow',outline='black')



root.update()
time.sleep(1.6)
punto1=canvas.create_text(650,140,text='Puntos: (,)')
angulos=canvas.create_text(700,340, text='t_1: '+str(round(np.degrees(ang1)%360,2))+'[°]',font=('Arial',15),fill='green')
angulos2=canvas.create_text(700,380, text='t_2: '+str(round(np.degrees(ang2)%360,2))+'[°]',font=('Arial',15),fill='blue')
#"""
for step in range(len(valores_x)):
    ## asegurar constantes
    p2_vec1=np.array([[w,w,w+(6*a),w+(6*a)],[h-(1.5*a),h+(1.5*a),h+(0.5*a),h-(0.5*a)]]) #ver posiciones en otras formas
    p3_purp1=np.array([[w,w,w+(4*a),w+(5*a),w+(4*a)],[h+(0.5*a),h-(0.5*a),h-(0.5*a),h,h+(0.5*a)]])
    ## Primero se calculan los valores de interes--------------
    F=eq_nr(valores_x[step],valores_y[step], ang1, ang2, eq1, eq2, j)#(440,120, ang1, ang2, eq1, eq2, j)#valores_x[step]-w,-valores_y[step]+h, ang1, ang2, eq1, eq2, j)
    ang1=F[0,0]
    ang2=F[1,0]
    ## Crear matrices de rotación
    p_verde_new=mrot(ang1,p2_vec1) #rotaciones------------
    p_morado_new=mrot(ang2,p3_purp1)
    # Parametrizar valores al origen
    p_morado_imp=parametrizar(p_morado_new)
    p_verde_imp=parametrizar(p_verde_new)
    #eliminar plano
    canvas.delete(fig_verde)
    #canvas.delete(fig_c_verde)
    canvas.delete(fig_c2_verde)
    #canvas.delete(fig_c2_verde)
    canvas.delete(fig_az11)
    canvas.delete(fig_az12)
    canvas.delete(fig_perno_movil)
    canvas.delete(fig_purp)
    canvas.delete(punto1)
    canvas.delete(angulos)
    canvas.delete(angulos2)
    ## Actualización de los planos
    fig_purp=canvas.create_polygon(p_morado_imp,fill='purple',outline='purple')
    fig_verde=canvas.create_polygon(p_verde_imp,fill='green',outline='green')

    #canvas.move(fig_c2_verde,0,0)#(fig_c2_verde,((p_verde_imp[4]+p_verde_imp[6])/2)+w,((p_verde_imp[5]+p_verde_imp[7])/2)-h)
    ### Mover circulos
    fig_c2_verde=canvas.create_oval(w-(a/2),h-(a/2),w+(a/2),h+(a/2),fill='green',outline='green')
    canvas.move(fig_c2_verde,((p_verde_imp[4]+p_verde_imp[6])/2)-w,((p_verde_imp[5]+p_verde_imp[7])/2)-h)
    canvas.move(fig_purp,((p_verde_imp[4]+p_verde_imp[6])/2)-w,((p_verde_imp[5]+p_verde_imp[7])/2)-h)
    fig_perno_movil=canvas.create_oval(parametrizar(p_per2_movil),fill='yellow',outline='blue')
    canvas.move(fig_perno_movil,((p_verde_imp[4]+p_verde_imp[6])/2)-w,((p_verde_imp[5]+p_verde_imp[7])/2)-h)
    #fig_c2_verde=canvas.create_arc(p_verde_imp[4:8],fill='blue',outline='red',extent=180)#create_oval((p_verde_imp[4],p_verde_imp[5]+(1.5*a),p_verde_imp[6],+p_verde_imp[7]-(1.5*a)))
    fig_az11=canvas.create_polygon(p1_azul,fill='blue',outline='blue')
    fig_az12=canvas.create_arc(w-a,h-(a),w+a,h+(a),fill='blue',outline='blue',extent=180)
    fig_perno1=canvas.create_oval(w-(a/2),h-(a/2),w+(a/2),h+(a/2),fill='yellow',outline='black')
    punto1=canvas.create_text(650,140,text='Puntos (x,y): '+'('+str(round(valores_x[step]/1000,2))+','+str(round(valores_y[step]/1000,2))+')',font=('Arial',14))
    angulos=canvas.create_text(700,340, text='t_1: '+str(round(np.degrees(ang1)%360,2))+'[°]',font=('Arial',15),fill='green')
    angulos2=canvas.create_text(700,380, text='t_2: '+str(round(np.degrees(ang2)%360,2))+'[°]',font=('Arial',15),fill='blue')
    root.update()
    time.sleep(0.1)
# """
#"""

root.mainloop()
#Figuras mobiles
#fig_ve21=canvas.create_polygon(pol1ve(a),,fill='green',outline='green')



""" 
r1 = canvas.create_rectangle(w,h, w+10, h+10)
                              
def keypress(event):
    	x, y = 0, 0
    	if event.char == "a": x = -10; 
    	elif event.char == "d": x = 10
    	elif event.char == "w": y = -10
    	elif event.char == "s": y = 10
    	canvas.move(r1, x, y) 

root.bind("<Key>", keypress)
 
root.mainloop()
"""