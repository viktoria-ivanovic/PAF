import numpy as np
import matplotlib.pyplot as plt
import calculus


def kubna(x):
    return x**3 + 2*x**2 - x + 1

def kubna_izvod(x):
    return 3*x**2 + 4*x - 1

def trigonometrijska(x):
    return np.sin(x)

def trigonometrijska_izvod(x):
    return np.cos(x)


donja_granica, gornja_granica = -2, 2
epsilon_vrijednosti = [1e-1, 1e-3, 1e-5]
metode = ["tri-koraka", "dva-koraka"]


x_analiticki = np.linspace(donja_granica, gornja_granica, 100)
y_analiticki_kubna = kubna_izvod(x_analiticki)

plt.figure(figsize=(12, 6))
for metoda in metode:
    for eps in epsilon_vrijednosti:
        x_vrijednosti, derivacije = calculus.derivacija_u_rasponu(kubna, donja_granica, gornja_granica, epsilon=eps, metoda=metoda)
        plt.plot(x_vrijednosti, derivacije, label=f'Numerički ({metoda}, ε={eps})')

plt.plot(x_analiticki, y_analiticki_kubna, 'k--', label='Analitički')
plt.title("Izvod kubne funkcije")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.legend()
plt.grid(True)
plt.show()

y_analiticki_trig = trigonometrijska_izvod(x_analiticki)

plt.figure(figsize=(12, 6))
for metoda in metode:
    for eps in epsilon_vrijednosti:
        x_vrijednosti, derivacije = calculus.derivacija_u_rasponu(trigonometrijska, donja_granica, gornja_granica, epsilon=eps, metoda=metoda)
        plt.plot(x_vrijednosti, derivacije, label=f'Numerički ({metoda}, ε={eps})')

plt.plot(x_analiticki, y_analiticki_trig, 'k--', label='Analitički')
plt.title("Izvod trigonometrijske funkcije")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.legend()
plt.grid(True)
plt.show()

