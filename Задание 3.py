import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t=np.arange(0,10**3,1)
def scorost(v,t):
    dvdt=((f-g*v**2)/m)
    return dvdt

g=0.1
f=10
v_0=0
m=100
k=0.5

solver=odeint(scorost,v_0,t)
plt.plot(t,solver[:,0])
plt.show