import vpython
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math


def dZ_dt(Z, t):
    return [Z[1], (F_0 * math.cos(omega_0 * t) - c * Z[1] - k * Z[0]) / m]

m = 0.5
c = 0.2
k = 8
F_0 = 100
omega_0 = 5
Z0 = [120, 0]
ts = np.linspace(0, 25, 200)
Zs = odeint(dZ_dt, Z0, ts)
ys = Zs[:,0]
zs = Zs[:, 1]

vpython.scene.height = 200
vpython.scene.width = 300
vpython.scene.title = "Motion of block suspended by a spring" 
vpython.scene.center = vpython.vector(0,2,0)
ceiling = vpython.box(pos=vpython.vector(0,4.8,1), axis=vpython.vector(1,0,0), 
                      length=8, width=2, height=0.2, color=vpython.color.cyan) 
spring = vpython.helix(pos=vpython.vector(0,0.7,1), axis=vpython.vector(0,1,0), 
            radius=0.4, length=4, coils=10) 
block = vpython.box(pos=vpython.vector(0,0,1), axis=vpython.vector(1,0,0), length=1.4, 
            width=1.4, height=1.4, color=vpython.color.yellow)

for y in ys: 
    vpython.rate(50)
    _y = y/100
    block.pos = vpython.vector(0,0 + _y,1)
    spring.pos = vpython.vector(0,0.7 + _y,1)

plt.subplot(1, 2, 1)
plt.plot(ts,ys)
plt.title("Displacement vs time")
plt.xlabel("Time")
plt.ylabel("Displacement")

plt.subplot(1, 2, 2)
plt.plot(ts,zs)
plt.title("Velocity vs time")
plt.xlabel("Time")
plt.ylabel("Velocity")

plt.show()