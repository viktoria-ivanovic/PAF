import numpy as np

def izracunaj_izvod(funkcija, tocka, epsilon=1e-5, metoda="tri-koraka"):
   
    if metoda == "tri-koraka":
        return (funkcija(tocka + epsilon) - funkcija(tocka - epsilon)) / (2 * epsilon)
    elif metoda == "dva-koraka":
        return (funkcija(tocka + epsilon) - funkcija(tocka)) / epsilon
    else:
        raise ValueError("Nepoznata metoda.")

def derivacija_u_rasponu(funkcija, donja_granica, gornja_granica, epsilon=1e-5, metoda="tri-koraka", broj_tocaka=100):
   
    x_vrijednosti = np.linspace(donja_granica, gornja_granica, broj_tocaka)
    derivacije = [izracunaj_izvod(funkcija, x, epsilon, metoda) for x in x_vrijednosti]
    return x_vrijednosti, np.array(derivacije)



import numpy as np

def izracunaj_izvod(funkcija, tocka, epsilon=1e-5, metoda="tri-koraka"):
    if metoda == "tri-koraka":
        return (funkcija(tocka + epsilon) - funkcija(tocka - epsilon)) / (2 * epsilon)
    elif metoda == "dva-koraka":
        return (funkcija(tocka + epsilon) - funkcija(tocka)) / epsilon
    else:
        raise ValueError("Nepoznata metoda. ")

def derivacija_u_rasponu(funkcija, donja_granica, gornja_granica, epsilon=1e-5, metoda="tri-koraka", broj_tocaka=100):
    x_vrijednosti = np.linspace(donja_granica, gornja_granica, broj_tocaka)
    derivacije = [izracunaj_izvod(funkcija, x, epsilon, metoda) for x in x_vrijednosti]
    return x_vrijednosti, np.array(derivacije)


def pravokutna_aproksimacija(funkcija, a, b, n):
    
    dx = (b - a) / n
    x_lijevo = np.linspace(a, b - dx, n)
    x_desno = np.linspace(a + dx, b, n)

    donja_međa = np.sum(funkcija(x_lijevo)) * dx
    gornja_međa = np.sum(funkcija(x_desno)) * dx

    return donja_međa, gornja_međa

def trapezna_metoda(funkcija, a, b, n):
   
    dx = (b - a) / n
    x_vrijednosti = np.linspace(a, b, n + 1)
    y_vrijednosti = funkcija(x_vrijednosti)
    
    integral = (dx / 2) * (y_vrijednosti[0] + 2 * np.sum(y_vrijednosti[1:-1]) + y_vrijednosti[-1])
    return integral

