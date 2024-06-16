# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 16:55:27 2022

@author: aldoa
"""

import tkinter as tk
import time 
from pynput import keyboard as kb

window=tk.Tk()
window.title('Number')
window.configure(bg='yellow')
window.geometry('200x50')

num=tk.Label(window,text='00.00',bg='yellow',font=('Arial 16 bold'),fg='red')
num.place(x=70,y=10)
cont=0
contador=0
flag=0
word=''
while contador!=10.00:
    window.update()
    time.sleep(1)
    cont+=5
    contador=cont/100
    if cont % 10==0:
        flag=1
        word=word+str(contador)+'0'
    else:
        flag=0
        word=word+str(contador)     

    if contador<10:
        word='0'+word
    else:
        contador=0
        cont=0
    num.config(text=word)
    word=''

window.mainloop()
