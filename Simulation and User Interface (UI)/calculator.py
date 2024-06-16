# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:05:08 2022

@author: aldoa
"""

import tkinter as tk
from tkinter import ttk,messagebox
import time
def numeros(a):
    global tres
    global temp
    global temp2
    global signo
    #print(ord())
    global bandera_p
    global bandera_p2
    """
    if tres=='' and (a=='+' or a=='X' or a=='/'):
        pass
    elif tres!='' and(tres[-1]=='-' or tres[-1]=='+' or tres[-1]=='X' or tres[-1]=='/') and (a=='+' or a=='X' or a=='/'):
        pass
    elif :
        pass
    
    elif tres!='' and (tres[-1]=='+' or tres[-1]=='X' or tres[-1]=='/') and (ord(str(a))>=48 and ord(str(a))<=57):
        
        temp=float(tres[0:-1])
        l=len(tres)-1
        tres+=str(a) 
    else:
        tres+=str(a)  
       # temp=float(tres)
    """
    if tres=='' and (a=='+' or a=='X' or a=='/'):
        pass
    elif tres=='' and a=='-':
        temp='-'
    elif temp=='-' and (a=='+' or a=='X' or a=='/'):
        pass
    #elif and temp[-1]=='.' and a=='.':
    #    pass
    elif ord(str(a))>=48 and ord(str(a))<=57 and signo=='' :
        if abs((float(temp+str(a))))>100:
            pass
        else:
            
            if temp.find('.')>=0 and bandera_p<=1:
                temp+=str(a)
                bandera_p=bandera_p+1
                print(bandera_p)
            elif temp.find('.')==-1:
                temp+=str(a)
            else :
                pass
            
    elif a=='.':
        if temp[-1]=='.':
            pass
        elif abs((float(temp)))<=100 and signo=='' and not '.' in temp: #Agregar condicion para no agregar más puntos
               temp+=str(a)
        elif abs((float(temp2)))<=100 and signo!='' and not '.' in temp2:
               temp2+=str(a)
        
    elif temp!='' and (a=='+' or a=='X' or a=='/' or a=='-') and signo=='':
        signo=str(a)
    elif signo!='' and temp!='' and ord(str(a))>=48 and ord(str(a))<=57 :
        if abs((float(temp2+str(a))))>100:
            pass
        else:
            
            if temp2.find('.')>=0 and bandera_p2<=1:
                temp2+=str(a)
                bandera_p2=bandera_p2+1
                print(bandera_p2)
            elif temp2.find('.')==-1:
                temp2+=str(a)
            else :
                pass
    if a=='=':
        if signo=='+':
            tres=str(float(temp)+float(temp2))
            res.configure(text=tres)
            ventana.update()
            time.sleep(1)
            answer=messagebox.askyesno('Operation finished','Would you like to perform another operation?')
            if answer:
                ce()
            else:
                ventana.destroy()
        if signo=='-':
            tres=str(float(temp)-float(temp2))
            res.configure(text=tres)
            ventana.update()
            time.sleep(1)
            answer=messagebox.askyesno('Operation finished','Would you like to perform another operation?')
            if answer:
                ce()
            else:
                ventana.destroy()
        if signo=='X':
            tres=str(round(float(temp)*float(temp2),2))
            res.configure(text=tres)
            ventana.update()
            time.sleep(1)
            answer=messagebox.askyesno('Operation finished','Would you like to perform another operation?')
            if answer:
                ce()
            else:
                ventana.destroy()
        if signo=='/':
            try:
                tres=str(round(float(temp)/float(temp2),2))
                res.configure(text=tres)
                ventana.update()
                time.sleep(1)
                answer=messagebox.askyesno('Operation finished','Would you like to perform another operation?')
                if answer:
                    ce()
                else:
                    ventana.destroy()
            except:
                tres='Numeric or syntax error'
                res.configure(text=tres)
                res.place(x=0,y=0)
                ventana.update()
                time.sleep(1)
                answer=messagebox.askyesno('Operation finished','Would you like to perform another operation?')
                if answer:
                    ce()
                else:
                    ventana.destroy()
        
    else:
        tres=str(temp)+str(signo)+str(temp2) 
        res.configure(text=tres)
        ventana.update()
    
    
def info():
    tk.messagebox.showinfo(title='Directions',message='Calculator: operations between 2 values in the range of -100 to 100. Press number values on the calculator, press operation, and finally the equal key.')

def ce():
    global tres
    global temp
    global temp2
    global signo
    global bandera_p,bandera_p2
    temp=''
    temp2=''
    signo=''
    tres=''
    bandera_p=0
    bandera_p2=0
    res.place(x=100,y=0)
    res.configure(text=tres)
    ventana.update()
    
def c():
    """
    global tres
    tres=tres.rstrip(tres[-1])
    res.configure(text=tres)
    ventana.update()
    """
    global tres
    global temp
    global temp2
    global signo
    
    if temp2!='':
        temp2=''
    elif signo!='':
        signo=''
    elif temp!='':
        temp=''
    tres=str(temp)+str(signo)+str(temp2) 
    res.configure(text=tres)
    ventana.update()
    
ventana=tk.Tk()
ventana.title('Simple Mathematical Operations')
ventana.configure(bg='#d4edff')
ventana.geometry('300x100')
tres=''
temp=''
temp2=''
signo=''
bandera_p=0
bandera_p2=0
res=tk.Label(ventana,text=tres,font=('Arial 14 bold'),bg='#d4edff')
res.place(x=100,y=0)
val=tk.StringVar()
pixelVirtual = tk.PhotoImage(width=1, height=1)
boton_info=tk.Button(ventana,text='Info.',font=('Arial 14 bold'),fg='white',bg='red',command=info,image=pixelVirtual,height=20,width=50,compound='c')
boton_info.place(x=0,y=70)

boton_0=tk.Button(ventana,text='0',font=('Arial 14'),fg='white',bg='gray',command=lambda:numeros(0),image=pixelVirtual,height=20,width=20,compound='c')
boton_0.place(x=60,y=70)

boton_p=tk.Button(ventana,text='.',font=('Arial 20'),fg='white',bg='gray',command=lambda:numeros('.'),image=pixelVirtual,height=20,width=20,compound='c')
boton_p.place(x=90,y=70)

boton_1=tk.Button(ventana,text='1',font=('Arial 14'),fg='white',bg='gray',command=lambda:numeros(1),image=pixelVirtual,height=20,width=20,compound='c')
boton_1.place(x=0,y=40)

boton_2=tk.Button(ventana,text='2',font=('Arial 14'),fg='white',bg='gray',command=lambda:numeros(2),image=pixelVirtual,height=20,width=20,compound='c')
boton_2.place(x=30,y=40)

boton_3=tk.Button(ventana,text='3',font=('Arial 14'),fg='white',bg='gray',command=lambda:numeros(3),image=pixelVirtual,height=20,width=20,compound='c')
boton_3.place(x=60,y=40)

boton_4=tk.Button(ventana,text='4',font=('Arial 14'),fg='white',bg='gray',command=lambda:numeros(4),image=pixelVirtual,height=20,width=20,compound='c')
boton_4.place(x=90,y=40)

boton_5=tk.Button(ventana,text='5',font=('Arial 14'),fg='white',bg='gray',command=lambda:numeros(5),image=pixelVirtual,height=20,width=20,compound='c')
boton_5.place(x=120,y=40)

boton_6=tk.Button(ventana,text='6',font=('Arial 14'),fg='white',bg='gray',command=lambda:numeros(6),image=pixelVirtual,height=20,width=20,compound='c')
boton_6.place(x=150,y=40)

boton_7=tk.Button(ventana,text='7',font=('Arial 14'),fg='white',bg='gray',command=lambda:numeros(7),image=pixelVirtual,height=20,width=20,compound='c')
boton_7.place(x=180,y=40)

boton_8=tk.Button(ventana,text='8',font=('Arial 14'),fg='white',bg='gray',command=lambda:numeros(8),image=pixelVirtual,height=20,width=20,compound='c')
boton_8.place(x=210,y=40)

boton_9=tk.Button(ventana,text='9',fg='white',font=('Arial 14'),bg='gray',command=lambda:numeros(9),image=pixelVirtual,height=20,width=20,compound='c')
boton_9.place(x=240,y=40)

boton_ce=tk.Button(ventana,text='ce',fg='white',font=('Arial 14'),bg='orange',command=ce,image=pixelVirtual,height=20,width=20,compound='c')
boton_ce.place(x=270,y=40)

boton_c=tk.Button(ventana,text='del',font=('Arial 14'),fg='white',bg='orange',command=c,image=pixelVirtual,height=20,width=20,compound='c')
boton_c.place(x=270,y=70)

#### Botones de operación ###

boton_mas=tk.Button(ventana,text='+',fg='white',font=('Arial 20'),bg='gray',command=lambda:numeros('+'),image=pixelVirtual,height=20,width=20,compound='c')
boton_mas.place(x=120,y=70)

boton_menos=tk.Button(ventana,text='-',fg='white',font=('Arial 20'),bg='gray',command=lambda:numeros('-'),image=pixelVirtual,height=20,width=20,compound='c')
boton_menos.place(x=150,y=70)

boton_por=tk.Button(ventana,text='x',fg='white',font=('Arial 18'),bg='gray',command=lambda:numeros('X'),image=pixelVirtual,height=20,width=20,compound='c')
boton_por.place(x=180,y=70)

boton_div=tk.Button(ventana,text='/',fg='white',font=('Arial 18'),bg='gray',command=lambda:numeros('/'),image=pixelVirtual,height=20,width=20,compound='c')
boton_div.place(x=210,y=70)

boton_igual=tk.Button(ventana,text='=',fg='white',font=('Arial 18'),bg='blue',command=lambda:numeros('='),image=pixelVirtual,height=20,width=20,compound='c')
boton_igual.place(x=240,y=70)
ventana.mainloop()