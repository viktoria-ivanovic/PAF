import matplotlib.pyplot as plt
import math

V_0=500  # m/s
x_0=0   # m
y_0=-5   # m
kut_deg=45  # °

g=9.81  # m/s^2
dt=0.01

A=3
C=0.36
ro=1.23
m=1500

D=A*C*ro/2

kut_rad=kut_deg*math.pi/360
V_0_x=V_0*math.cos(kut_rad)
V_0_y=V_0*math.sin(kut_rad)

x_polozaj=[x_0]
y_polozaj=[y_0]

x_brzine=[V_0_x]
y_brzine=[V_0_y]

vrijeme=[0]

t=0
a_y=-g-(D/m)*V_0*V_0_y
a_x=-(D/m)*V_0*V_0_x
v_x=V_0_x
v_y=V_0_y
x=x_0
y=y_0


while y >= 0:
  x+=v_x*dt + 0.5*a_x*dt**2
  x_polozaj.append(x)
  y+=v_y*dt + 0.5*a_y*dt**2
  y_polozaj.append(y)
  v_x+=a_x*dt
  x_brzine.append(v_x)
  v_y+=a_y*dt
  y_brzine.append(v_y)
  v=math.sqrt(v_x**2 + v_y**2)
  a_y=-g-(D/m)*v*v_y
  a_x=-(D/m)*v*v_x
  t+=dt
  vrijeme.append(t)

plt.figure(figsize=(15,5))
plt.scatter(x_polozaj, y_polozaj)
plt.title("Putanja projektila")
plt.xlabel("Udaljenost [m]")
plt.ylabel("Visina [m]")
plt.show()

plt.figure(figsize=(15,6))
plt.scatter(vrijeme, x_brzine, s=10, c='b', marker="s", label='x komponenta brzine')
plt.scatter(vrijeme,y_brzine, s=10, c='r', marker="o", label='y komponenta brzine')
plt.legend(loc='upper right')
plt.show()