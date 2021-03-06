import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t=np.arange(0,4,0.1)
def invest(n,t):
    dndt=-n*k*t
    return dndt
n_0=1000
k=0.08
solver=odeint(invest,n_0,t)
plt.plot(t,solver[:,0])
plt.show
