"""
Created on Tue Aug  1 12:40:31 2017

@author: Zachery Van Es
"""
from numpy import sin, cos
import numpy as np
import scipy.integrate as intergrate
import matplotlib.pyplot as plt
import matplotlib.animation as ani

#Global Values
G = 9.8
L1 = 2.0
L2 = 0.5
M1 = 1.0
M2 = 1.0


def System(state, t):     

    y0 = state[1]

 

    del_ = state[2] - state[0]

    den1 = (M1 + M2)*L1 - M2*L1*cos(del_)*cos(del_)

    y1 = (M2*L1*state[1]*state[1]*sin(del_)*cos(del_) + M2*G*sin(state[2])*cos(del_) +

               M2*L2*state[3]*state[3]*sin(del_) - (M1 + M2)*G*sin(state[0]))/den1

 

    y2 = state[3]

 

    den2 = (L2/L1)*den1

    y3 = (-M2*L2*state[3]*state[3]*sin(del_)*cos(del_) + (M1 + M2)*G*sin(state[0])*cos(del_) -

               (M1 + M2)*L1*state[1]*state[1]*sin(del_) - (M1 + M2)*G*sin(state[2]))/den2

 

    return [y0,y1,y2,y3]

def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*dt))
    return line, time_text

dt = 0.05
t = np.arange(0.0,50,dt)

th1 = 180.0
w1 = -90.0
th2 = -10.0
w2 = 1.0

init_state = np.radians([th1,w1,th2,w2])

y = intergrate.odeint(System, init_state, t)

x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1

#animation
fig = plt.figure()

ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))

ax.grid()

 

line, = ax.plot([], [], 'o-', lw=2)

time_template = 'time = %.1fs'

time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

 

clip = ani.FuncAnimation(fig, animate, np.arange(1, len(y)), interval=25, blit=True, init_func=init)

 


clip.save('double_pendulum.mp4', fps=15)

plt.show()















