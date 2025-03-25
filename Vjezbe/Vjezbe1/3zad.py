import numpy as
import matplotlib.pyplot as plt
while True:
    unos_1=input().strip()
    odvoji=unos_1.split()
    if len(odvoji)==2 and odvoji[0].lstrip('.').replace('.','',1)-isdigit() and odvoji[1].lstrip('-').replace('.','',1):
        x1,y1= float(odvoji[0]),float(odvoji[1])
        break
    else:
        print('Greška')
while True:
    unos_2=input().strip()
    odvoji_2=unos_2.split()
    if len(odvoji_2)==2 and odvoji_2[0].lstrip('').replace('.','',1).isdigit() and odvoji_2[1].lstrip('-').replace('.','',1):
        x2,y2=float(odvoji_2[0]),float(odvoji_2[1])
        break
    else:
        print('Greška')
    k=(y2-y1)/(x2-x1)
    z=y1-k*x1
    print(f'Jednadžba pravca je y={k:.0f}x+{z:.0f}')

