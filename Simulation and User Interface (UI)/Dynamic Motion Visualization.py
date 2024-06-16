# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 16:22:42 2022

@author: aldoa
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time 
import sympy as sym
from matplotlib.animation import PillowWriter

#"""
t_stop = 3
t_p_max = 0.3
t_pp_max = 0.09

t_1 = 3.35
t_2 = 10
t_f = 13.4
sym.init_printing(use_unicode=True)
t = sym.Symbol('t')

### Position
f1 = (t_pp_max/2)*t**2  # For an interval 0 < t < t_1
f2 = -((t_p_max**2)/(2*t_pp_max)) + (t_p_max*t)  # For an interval t_1 to t_2
f3 = (-t_p_max**2/(2*t_pp_max)) - ((t_stop**2*t_pp_max)/(2*t_p_max**2)) + (((t_stop*t_pp_max)/(t_p_max)) + t_p_max)*t - ((t_pp_max)/(2))*t**2  # For an interval t_2 to t_f
### Velocity
f1p = sym.diff(f1, t)
f2p = sym.diff(f2, t)
f3p = sym.diff(f3, t)

### Acceleration
f1pp = sym.diff(f1, t, 2)
f2pp = sym.diff(f2, t, 2)
f3pp = sym.diff(f3, t, 2)

y1 = [0]
y2 = [0]
y3 = [0]

xx = [0]
axis, (ax1, ax2, ax3) = plt.subplots(3, 1)

line1, = ax1.plot([], [], lw=2, color='y')
line2, = ax2.plot([], [], lw=2, color='g')
line3, = ax3.plot([], [], lw=2, color='b')
line = [line1, line2, line3]
ax1.set_ylim(0, 3.2)
ax1.set_xlim(0, 14)
ax1.set_xlabel('time [s]')
ax1.set_ylabel('Pos [rad]')
ax1.grid()

ax2.set_ylim(0, 0.32)
ax2.set_xlim(0, 14)
ax2.set_xlabel('time [s]')
ax2.set_ylabel('Vel [rad/s]')
ax2.grid()

ax3.set_ylim(-.1, .1)
ax3.set_xlim(0, 14)
ax3.set_xlabel('time [s]')
ax3.set_ylabel('Accel [rad/s^2]')
ax3.grid()

tp = 0.01

t1 = time.time()
for i in range(1600):
    if t_1 >= (i*tp):   # t0, t1, t2, tf
        y1.append(float(f1.subs(t, ((i+1)*tp))))
        y2.append(float(f1p.subs(t, ((i+1)*tp))))
        y3.append(float(f1pp.subs(t, ((i+1)*tp))))
        xx.append((i+1)*tp)
        plt.subplot(3, 1, 1)
        plt.plot(xx, y1, color='y')
        plt.grid()
        plt.subplot(3, 1, 2)
        plt.plot(xx, y2, color='g')  
        plt.grid()
        plt.subplot(3, 1, 3)
        plt.plot(xx, y3, color='b')
        plt.grid()
    elif (i*tp) > t_1 and (i*tp) <= t_2:
        y1.append(float(f2.subs(t, ((i+1)*tp))))
        y2.append(float(f2p.subs(t, ((i+1)*tp))))
        y3.append(float(f2pp.subs(t, ((i+1)*tp))))
        xx.append((i+1)*tp)
        plt.subplot(3, 1, 1)
        plt.plot(xx, y1, color='y')
        plt.grid()
        plt.subplot(3, 1, 2)
        plt.plot(xx, y2, color='g')  
        plt.grid()
        plt.subplot(3, 1, 3)
        plt.plot(xx, y3, color='b')
        plt.grid()
    elif (i*tp) > t_2 and (i*tp) <= t_f:
        y1.append(float(f3.subs(t, ((i+1)*tp))))
        y2.append(float(f3p.subs(t, ((i+1)*tp))))
        y3.append(float(f3pp.subs(t, ((i+1)*tp))))
        xx.append((i+1)*tp)
        plt.subplot(3, 1, 1)
        plt.plot(xx, y1, color='y')
        plt.grid()
        plt.subplot(3, 1, 2)
        plt.plot(xx, y2, color='g')  
        plt.grid()
        plt.subplot(3, 1, 3)       
        plt.plot(xx, y3, color='b')
        plt.grid()
    else:
        break

t2 = time.time()
print(t2-t1)

axis2, (ax1, ax2, ax3) = plt.subplots(3, 1)

line1, = ax1.plot([], [], lw=2, color='y')
line2, = ax2.plot([], [], lw=2, color='g')
line3, = ax3.plot([], [], lw=2, color='b')
line = [line1, line2, line3]
ax1.set_ylim(0, 3.2)
ax1.set_xlim(0, 14)
ax1.set_xlabel('time [s]')
ax1.set_ylabel('Pos [rad]')
ax1.grid()

ax2.set_ylim(0, 0.32)
ax2.set_xlim(0, 14)
ax2.set_xlabel('time [s]')
ax2.set_ylabel('Vel [rad/s]')
ax2.grid()

ax3.set_ylim(-.1, .11)
ax3.set_xlim(0, 14)
ax3.set_xlabel('time [s]')
ax3.set_ylabel('Accel [rad/s^2]')
ax3.grid()

def animate(ii):
    line[0].set_data(xx[:ii], y1[:ii])
    line[1].set_data(xx[:ii], y2[:ii])
    line[2].set_data(xx[:ii], y3[:ii])
    return line

t1 = time.time()
ani = FuncAnimation(axis2, animate, frames=len(xx), interval=1, save_count=50)
ani.save('result.gif', writer=PillowWriter(fps=5000))
plt.show()
t2 = time.time()
print(t2-t1)
