import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

t=np.arange(0,100,0.1)
def func_A (z,t):
    x,v_x,y,v_y=z
    dxdt=v_x
    dv_xdt=(F1+(F2*np.cos(a))+(F3*np.cos(a)*2)+(F4*np.cos(a)*3))
    dydt=v_y
    dv_ydt=(F1+(F2*np.cos(a))+(F3*np.cos(a)*2)+(F4*np.cos(a)*3))
    return dxdt,dv_xdt,dydt,dv_ydt

x0=0
v_x0=-10
y0=0
v_y0=-10
z0=x0,v_x0,y0,v_y0

F1=4
F2=8
F3=12
F4=16
a=0.524

sol = odeint(func_A, z0, t)

plt.plot(sol[:,0],sol[:,2])
plt.show()