import numpy as np
import matplotlib.pyplot as plt

q_e = -1.602e-19
q_p = 1.602e-19
m = 9.109e-31
Bz = 1e-3

def lorentz(y, q):
    v = y[3:]
    B = np.array([0, 0, Bz])
    a = (q / m) * np.cross(v, B)
    return np.concatenate((v, a))

def rk4_step(y, dt, q):
    k1 = lorentz(y, q)
    k2 = lorentz(y + 0.5 * dt * k1, q)
    k3 = lorentz(y + 0.5 * dt * k2, q)
    k4 = lorentz(y + dt * k3, q)
    return y + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)

def simulate_rk4(q, r0, v0, dt, steps):
    y = np.zeros((steps, 6))
    y[0, :3] = r0
    y[0, 3:] = v0
    for i in range(1, steps):
        y[i] = rk4_step(y[i-1], dt, q)
    return y[:, :3]  # vraćamo samo pozicije

r0 = np.array([0, 0, 0])
v0 = np.array([1e5, 2e5, 3e5])
dt = 1e-11
steps = 5000

r_e = simulate_rk4(q_e, r0, v0, dt, steps)
r_p = simulate_rk4(q_p, r0, v0, dt, steps)

fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(121, projection='3d')
ax1.plot(r_e[:,0], r_e[:,1], r_e[:,2], color='blue')
ax1.set_title("Putanja elektrona (RK4)")
ax1.set_xlabel("x [m]")
ax1.set_ylabel("y [m]")
ax1.set_zlabel("z [m]")

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot(r_p[:,0], r_p[:,1], r_p[:,2], color='red')
ax2.set_title("Putanja pozitrona (RK4)")
ax2.set_xlabel("x [m]")
ax2.set_ylabel("y [m]")
ax2.set_zlabel("z [m]")

plt.tight_layout()
plt.show()
