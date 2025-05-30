import numpy as np
import matplotlib.pyplot as plt

q_e = -1.602e-19
q_p = 1.602e-19
m = 9.109e-31
Bz = 1e-3

def simulate(q, r0, v0, dt, steps):
    r = np.zeros((steps, 3))
    v = np.zeros((steps, 3))
    r[0] = r0
    v[0] = v0
    B = np.array([0, 0, Bz])
    for i in range(1, steps):
        a = (q / m) * np.cross(v[i-1], B)
        v[i] = v[i-1] + a * dt
        r[i] = r[i-1] + v[i] * dt
    return r

r0 = np.array([0, 0, 0])
v0 = np.array([1e5, 2e5, 3e5])
dt = 1e-11
steps = 5000

r_e = simulate(q_e, r0, v0, dt, steps)
r_p = simulate(q_p, r0, v0, dt, steps)

fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(121, projection='3d')
ax1.plot(r_e[:,0], r_e[:,1], r_e[:,2], color='blue')
ax1.set_title("Putanja elektrona")
ax1.set_xlabel("x [m]")
ax1.set_ylabel("y [m]")
ax1.set_zlabel("z [m]")

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot(r_p[:,0], r_p[:,1], r_p[:,2], color='red')
ax2.set_title("Putanja pozitrona")
ax2.set_xlabel("x [m]")
ax2.set_ylabel("y [m]")
ax2.set_zlabel("z [m]")

plt.tight_layout()
plt.show()
