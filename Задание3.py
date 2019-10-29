print('-----Задание 3-----')
def energy (m, v, g, h):
    E=(m*v**2)/2+(m*g*h)
    return E
from modul_const import g
m=1
v=1
h=1
tab=energy(m, v, g, h)
print(tab)