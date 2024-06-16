# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:06:58 2022

@author: aldoa
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sympy as sym
from matplotlib.animation import PillowWriter



vel_max=0.069
acel_max=0.1

t_0=0
t_1=0.69#0.4
t_2=2.31
t_3=3

tiempo=[]
xt=[0.04]
yt=[0.18]
xf=0.2
yf=0.06
t=sym.Symbol('t')


a0_x=xt[0]
a1_x=0
a2_x=(xf/2)
b0_x=(0.5*(-vel_max**2/(2*acel_max)))+a0_x
b1_x=acel_max
c2_x=-acel_max/2
c1_x=(vel_max-(2*c2_x*t_2))
c0_x=xf-(c1_x*t_3)-(c2_x*t_3**2)

p_x1=((acel_max/2)*t**2)+ xt[0]
p_x2=(((-vel_max**2)/(2*acel_max))+((vel_max)*t))+xt[0]
p_x3=c0_x+c1_x*t+c2_x*t**2

vel_maxy=0.05194
acel_maxy=0.075
vel_max=vel_maxy
acel_max=acel_maxy

a0_y=yt[0]
a1_y=0
a2_y=-(yf/2)
b0_y=(0.5*(vel_max**2/(2*acel_max)))+yt[0]
b1_y=-acel_max
c2_y=acel_max/2
c1_y=(-vel_max-(2*c2_y*t_2))
c0_y=yf-(c1_y*t_3)-(c2_y*t_3**2)


p_y1=-((acel_max/2)*t**2)+ yt[0]
p_y2=-(((-vel_max**2)/(2*acel_max))+((vel_max)*t))+yt[0]
p_y3=c0_y+(c1_y*t)+(c2_y*t**2)

tiempo=[0]
for tt in range(201):
    if (tt+1)*0.025 <= t_1:
        tiempo.append((tt+1)*0.025)
        xt.append(float(p_x1.subs(t,tiempo[-1])))
        yt.append(float(p_y1.subs(t,tiempo[-1])))        
    elif (tt+1)*0.025 >t_1 and (tt+1)*0.025 <= t_2:
        tiempo.append((tt+1)*0.025)
        xt.append(float(p_x2.subs(t,tiempo[-1])))
        yt.append(float(p_y2.subs(t,tiempo[-1])))
    elif (tt+1)*0.025>t_2 and (tt+1)*0.025<t_3:
        tiempo.append((tt+1)*0.025)
        xt.append(float(p_x3.subs(t,tiempo[-1])))
        yt.append(float(p_y3.subs(t,tiempo[-1])))        

axx=plt.figure()

ax1=plt.subplot2grid(shape=(50,20),loc=(0,0),rowspan=21,colspan=8)
ax2=plt.subplot2grid(shape=(60,20),loc=(40,0),rowspan=21,colspan=8)
ax3=plt.subplot2grid(shape=(100,20),loc=(25,12),rowspan=60,colspan=8)

line1, = ax1.plot([], [], lw=2,color='k')
line2, = ax2.plot([], [], lw=2, color='b')
line3, = ax3.plot([], [], lw=2, color='r')
line=[line1,line2,line3]

ax1.set_ylim(0,0.25)
ax1.set_xlim(0,3.2)
ax1.set_xlabel('time [s]')
ax1.set_ylabel('Pos [rad]')
ax1.set_title('Position in X')
ax1.grid()

ax2.set_ylim(0,0.2)
ax2.set_xlim(0,3)
ax2.set_xlabel('time [s]')
ax2.set_ylabel('Pos [rad]')
ax2.set_title('Position in Y')
ax2.grid()

ax3.set_ylim(-0.01,0.2)
ax3.set_xlim(0,0.25)
ax3.set_xlabel('Pos X [rad]')
ax3.set_ylabel('Pos Y [rad]')
ax3.set_title('Position in X,Y')
ax3.grid()

axx.tight_layout()


def animate(ii):
    line[0].set_data(tiempo[:ii],xt[:ii])
    line[1].set_data(tiempo[:ii],yt[:ii])
    line[2].set_data(xt[:ii],yt[:ii])
    return line

ani=FuncAnimation(axx,animate,frames=len(tiempo),interval=1,save_count=50)
ani.save('2d motion planner1.gif',writer=PillowWriter(fps=5000))
