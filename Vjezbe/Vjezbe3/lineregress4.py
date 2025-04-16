import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 5, 100)
y = 5 * x + np.random.normal(loc=0, scale=25, size=len(x))

a = np.linspace(3.5, 6.5, 50)

pravci = np.zeros((len(x), len(a)))
suma = np.zeros(len(a))

for i in range(len(a)):
    pravci[:, i] = x * a[i]
    suma[i] = np.sum((y - pravci[:, i])**2)

indeks = np.argmin(suma)

plt.figure()
plt.scatter(x, y, label='Podaci')
plt.plot(x, pravci[:, indeks], 'r', label=f'Najbolji pravac (a={a[indeks]:.2f})')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Metoda najmanjih kvadrata (ručna)')
plt.show()




