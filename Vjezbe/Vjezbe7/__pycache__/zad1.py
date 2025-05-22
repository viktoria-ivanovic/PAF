import matplotlib.pyplot as plt
from projektil import Projektil

# Početni uslovi
x0, y0 = 0, 0
v0 = 50
kut = 45
masa = 1
otpor = 0.1
dt = 0.01

# Eulerova metoda
p1 = Projektil(x0, y0, v0, kut, masa, otpor, dt)
x_e, y_e = p1.euler_simulacija()

# Runge-Kutta 4. reda
p2 = Projektil(x0, y0, v0, kut, masa, otpor, dt)
x_rk, y_rk = p2.rk4_simulacija()

# Prikaz rezultata
plt.plot(x_e, y_e, label='Eulerova metoda')
plt.plot(x_rk, y_rk, label='Runge-Kutta 4. reda')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('Putanja projektila')
plt.legend()
plt.grid(True)
plt.show()


