import matplotlib.pyplot as plt
import math


m = 1.0      
k = 1.0      
x0 = 1.0     
v0 = 0.0     
dt = 0.01    
T = 20       


omega = math.sqrt(k / m)


t = 0.0
x = x0
v = v0
a = -k / m * x


vrijeme = [t]
x_polozaji = [x]
v_brzine = [v]
a_ubrzanja = [a]


while t <= T:
    x += v * dt + 0.5 * a * dt**2
    a = -k / m * x
    v += a * dt

    t += dt

    vrijeme.append(t)
    x_polozaji.append(x)
    v_brzine.append(v)
    a_ubrzanja.append(a)


x_analiticki = [x0 * math.cos(omega * t_i) for t_i in vrijeme]
v_analiticki = [-x0 * omega * math.sin(omega * t_i) for t_i in vrijeme]
a_analiticki = [-omega**2 * x0 * math.cos(omega * t_i) for t_i in vrijeme]


plt.figure(figsize=(15, 4))
plt.plot(vrijeme, x_polozaji, label='Numerički x(t)')
plt.plot(vrijeme, x_analiticki, '--', label='Analitički x(t)')
plt.title('Položaj x(t)')
plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(15, 4))
plt.plot(vrijeme, v_brzine, label='Numerički v(t)')
plt.plot(vrijeme, v_analiticki, '--', label='Analitički v(t)')
plt.title('Brzina v(t)')
plt.xlabel('t [s]')
plt.ylabel('v [m/s]')
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(15, 4))
plt.plot(vrijeme, a_ubrzanja, label='Numerički a(t)')
plt.plot(vrijeme, a_analiticki, '--', label='Analitički a(t)')
plt.title('Ubrzanje a(t)')
plt.xlabel('t [s]')
plt.ylabel('a [m/s²]')
plt.legend()
plt.grid()
plt.show()
