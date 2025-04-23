from particle import Particle
import matplotlib.pyplot as plt
import math

v0 = 10
theta = 60
g = 9.81
R_analytical = (v0**2 * math.sin(math.radians(2 * theta))) / g


dt_values = [0.1, 0.05, 0.01, 0.005, 0.001, 0.0005]
errors = []

for dt in dt_values:
    p = Particle(v0, theta)
    R_numeric = p.range(dt=dt)
    error = abs(R_numeric - R_analytical) / R_analytical
    errors.append(error)


plt.plot(dt_values, errors, marker='o')
plt.xlabel("∆t (s)")
plt.ylabel("Relativna pogreška")
plt.title("Relativna pogreška u ovisnosti o ∆t")
plt.grid()
plt.xscale("log")  
plt.yscale("log")
plt.show()
