import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t=np.arange(0,10,0.1)
def razm_bakt(m,t):
    dndt=n*k
    return dndt
n=1
k=10
solver=odeint(razm_bakt, n, t)
plt.plot(t,solver[:,0])
plt.show