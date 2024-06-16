# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 18:10:30 2022

@author: aldoa
"""

import tkinter as tk
import time 
#from pynput import keyboard  # using module keyboard
from pynput import keyboard as kb
from pynput.keyboard import Key

def press(key):
    if key==Key.left:
        value=float(num.cget("text"))
        value-=0.5
        formatted_value=format_value(value)
        num.config(text=formatted_value)
    elif key==Key.down:
        value=float(num.cget("text"))
        value-=1
        formatted_value=format_value(value)
        num.config(text=formatted_value)
    elif key==Key.up:
        value=float(num.cget("text"))
        value+=1
        formatted_value=format_value(value)
        num.config(text=formatted_value)
    elif key==Key.right:
        value=float(num.cget("text"))
        value+=0.5
        formatted_value=format_value(value)
        num.config(text=formatted_value)
    elif key==kb.KeyCode.from_char('i') or key==kb.KeyCode.from_char('I'):
        num.config(text='00.0')
    elif key==kb.KeyCode.from_char('q'):
        window.destroy()
        return False

def format_value(val):
    if val < 0:
        return '-{:04.1f}'.format(-val)
    else:
        return '{:05.1f}'.format(val)

def release(key):
    pass

window=tk.Tk()
window.title('Dynamic Value')
window.configure(bg='white')
window.geometry('500x200')
value=0.0
num=tk.Label(window,text='0'+str(value),bg='white',font=('Arial 24 bold'),fg='#000064')
num.place(x=430,y=100)

listener = kb.Listener(press, release)
listener.start()
window.mainloop()
