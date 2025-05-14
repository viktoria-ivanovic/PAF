

import numpy as np

class harmonic_oscilator:
    def __init__(self, masa, konstanta_opruge, x0, v0):
        self.m = masa
        self.k = konstanta_opruge
        self.x0 = x0
        self.v0 = v0
        self.omega = np.sqrt(self.k / self.m)

    def analiticko_rjesenje(self, t):
        A = self.x0
        B = self.v0 / self.omega
        x = A * np.cos(self.omega * t) + B * np.sin(self.omega * t)
        v = -A * self.omega * np.sin(self.omega * t) + B * self.omega * np.cos(self.omega * t)
        a = -self.omega**2 * x
        return x, v, a

    def eulerova_metoda(self, dt, trajanje):
        n = int(trajanje / dt)
        t = np.linspace(0, trajanje, n)
        x = np.zeros(n)
        v = np.zeros(n)
        a = np.zeros(n)

        x[0] = self.x0
        v[0] = self.v0
        a[0] = -self.k / self.m * x[0]

        for i in range(1, n):
            x[i] = x[i-1] + v[i-1] * dt + 0.5 * a[i-1] * dt**2
            a[i] = -self.k / self.m * x[i]
            v[i] = v[i-1] + a[i] * dt

        return t, x, v, a

    def odredi_period(self, dt, maks_vrijeme=20):
        x = self.x0
        v = self.v0
        a = -self.k / self.m * x
        t = 0.0

        prethodni_x = x
        prijelazi = []

        while t <= maks_vrijeme:
            x_novo = x + v * dt + 0.5 * a * dt**2
            a_novo = -self.k / self.m * x_novo
            v_novo = v + a_novo * dt

            if prethodni_x < 0 and x_novo >= 0:
                prijelazi.append(t)
                if len(prijelazi) == 2:
                    break

            t += dt
            prethodni_x = x_novo
            x = x_novo
            v = v_novo
            a = a_novo

        if len(prijelazi) == 2:
            return prijelazi[1] - prijelazi[0]
        else:
            return np.nan
