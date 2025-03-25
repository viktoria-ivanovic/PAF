import numpy as np
import matplotlib.pyplot as plt
def kosi_hitac(v_0, k,t,dt):
    x=0
    g=9.81
    v=0
    y=0
    xlista=[]
    ylista=[]
    tlista=[]
    for i in np.range(0,t/dt):
        x=x+v_0*cos(k)*dt
        y=y+v_0*sin(k)*dt-1/2*g*t**2
        xlista.append(x)
        ylista.append(y)
        tlista(t)

kosi_hitac(1,45,10,0.0001)