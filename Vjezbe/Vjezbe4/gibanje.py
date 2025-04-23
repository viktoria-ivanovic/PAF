from particle import Particle
import math


v0 = 20
theta = 45


g = 9.81
R_analytical = (v0**2 * math.sin(math.radians(2 * theta))) / g


p = Particle(v0, theta)


R_numerical = p.range(dt=0.01)


print(f"Analitički domet: {R_analytical:.2f} m")
print(f"Numerički domet:  {R_numerical:.2f} m")
print(f"Odstupanje:       {abs(R_numerical - R_analytical):.2f} m")


p.plot_trajectory()
