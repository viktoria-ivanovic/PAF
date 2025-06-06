import numpy as np
import matplotlib.pyplot as plt

G = 6.67408e-11
masa_sunca = 1.989e30
masa_zemlje = 5.9742e24
udaljenost_au = 1.496e11
pocetna_brzina = 29783
sekundi_u_godini = 365.242 * 24 * 3600

dt = 60 * 60
koraka = int(sekundi_u_godini / dt)

pozicija_sunca = np.array([0.0, 0.0])
brzina_sunca = np.array([0.0, 0.0])

pozicija_zemlje = np.array([udaljenost_au, 0.0])
brzina_zemlje = np.array([0.0, pocetna_brzina])

putanja_sunca = []
putanja_zemlje = []

for i in range(koraka):
    razlika = pozicija_zemlje - pozicija_sunca
    udaljenost = np.sqrt(razlika[0]**2 + razlika[1]**2)
    sila = -G * masa_sunca * masa_zemlje / udaljenost**3 * razlika

    brzina_zemlje += sila / masa_zemlje * dt
    brzina_sunca -= sila / masa_sunca * dt

    pozicija_zemlje += brzina_zemlje * dt
    pozicija_sunca += brzina_sunca * dt

    putanja_zemlje.append(pozicija_zemlje.copy())
    putanja_sunca.append(pozicija_sunca.copy())

putanja_zemlje = np.array(putanja_zemlje)
putanja_sunca = np.array(putanja_sunca)

plt.figure(figsize=(8, 8))
plt.plot(putanja_sunca[:, 0], putanja_sunca[:, 1], 'yo', label="Sunce")
plt.plot(putanja_zemlje[:, 0], putanja_zemlje[:, 1], 'b-', label="Zemlja")
plt.plot(0, 0, 'ro', label="Početak")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Zemlja oko Sunca - jednostavna simulacija")
plt.legend()
plt.axis("equal")
plt.grid(True)
plt.show()
