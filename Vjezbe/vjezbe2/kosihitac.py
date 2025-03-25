import numpy as np
import matplotlib.pyplot as plt
def gibanje (f,m,t,dt):
    a=f/m
    v=0
    x=0
    vlista = []
    xlista = []
    tlista = []
    for i in np.arrange(0,t/dt):
        x = x+v*dt
        v = v+a*dt
        t = t+dt
        vlista.append(v)
        xlista.append(x)
        tlista.append(t)
    
    plt.plot(tlista,xlista)
    plt.show()
    plt.plot(vlista,tlista)
    plt.show
    plt.plot(a,tlista)
    plt.show
    print(xlista)
    print(vlista)

gibanje(10, 2, 10, 0.001)