import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
from matplotlib.animation import ArtistAnimation 

second_in_year = 365 * 24 * 60 * 60
second_in_day = 24 * 60 * 60
years = 6
t = np.arange(0, years*second_in_year, second_in_day)

def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3) = s
     
    dxdt1 = v_x1
    dv_xdt1 = (-G * m2 * (x1 - x2) / ((x1 - x2)**2+(y1 - y2)**2)**1.5
             - G * m3 * (x1 - x3) / ((x1 - x3)**2+(y1 - y3)**2)**1.5)
             
    dydt1 = v_y1
    dv_ydt1 = (-G * m2 * (y1 - y2)/((x1 - x2)**2 + (y1 - y2)**2)**1.5
             - G * m3 * (y1 - y3) / ((x1-x3)**2 + (y1-y3)**2)**1.5)

    dxdt2 = v_x2
    dv_xdt2 = (-G * m1 * (x2 - x1) / ((x2 - x1)**2+(y2 - y1)**2)**1.5
             - G * m3 * (x2 - x3) / ((x2 - x3)**2+(y2 - y3)**2)**1.5)
             
    dydt2 = v_y2
    dv_ydt2 = (-G * m1 * (y1 - y2)/((x1 - x2)**2 + (y1 - y2)**2)**1.5
             - G * m3 * (y1 - y3) / ((x1-x3)**2 + (y1-y3)**2)**1.5  )           
      
    dxdt3 = v_x3
    dv_xdt3 = (-G * m1 * (x3 - x1) / ((x3 - x1)**2+(y3 - y1)**2)**1.5
             - G * m2 * (x3 - x2) / ((x3 - x2)**2+(y3 - y2)**2)**1.5)
             
    dydt3 = v_y3
    dv_ydt3 = (-G * m1 * (y3 - y1)/((x3 - x1)**2 + (y3 - y1)**2)**1.5
             - G * m2 * (y3 - y2) / ((x3-x2)**2 + (y3-y2)**2)**1.5)
     
    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
                dxdt2, dv_xdt2, dydt2, dv_ydt2,
                dxdt3, dv_xdt3, dydt3, dv_ydt3)
        
x10 = -8*149 * 10**9
v_x10 = 0
y10 = 0
v_y10 = 10000

x20 = -149 * 10**9
v_x20 = 1
y20 = 0
v_y20 = -3000

x30 = 0
v_x30 = 5000
y30 = 5*149 * 10**9
v_y30 = 0

s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30)

m1 = 2.10777 * 10**30
m2 = 1.193 * 10**30
m3 = 0.596 *10**30
G = 6.67 * 10**(-11)

sol = odeint(move_func, s0, t)
fig = plt.figure()
bodys = []

for i in range (0, len(t), 1):
    body1, = plt.plot(sol[:i,0], sol[:i,2], '-', color='r')
    body1_line, = plt.plot(sol[i, 0], sol[i,2], 'o', color='r')
    
    body2, = plt.plot(sol[:i,4], sol[:i,6], '-', color='g')
    body2_line, = plt.plot(sol[i, 4], sol[i,6], 'o', color='g')

    body3, = plt.plot(sol[:i,8], sol[:i,10], '-', color='b')
    body3_line, = plt.plot(sol[i, 8], sol[i,10], 'o', color='b')
    
    bodys.append([body1, body1_line, body2, body2_line, body3, body3_line])
    
ani = ArtistAnimation(fig, bodys, interval=50)
plt.axis('equal')
ani.save('N_body_G+K.gif')