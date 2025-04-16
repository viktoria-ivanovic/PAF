import numpy as np 
import math as m
import matplotlib.pyplot as plt

x=[12.5, 3.2 , 4 , 58.457, 654, 144.2, 27, 31, 45.1, 54]

sum_x= 0 

for i in x:
    sum_x+=i

avg_x=sum_x/len(x)

sigma_x= 0 

for i in x:
    sigma_x+=(i-avg_x)**2

sigma_x=m.sqrt(sigma_x/len(x))

plt.figure()
plt.plot(x, marker='o',markersize=5, c='k', label = 'Podaci')
plt.axhline(avg_x, c='red', label=avg_x)
plt.axhline(avg_x+sigma_x, c='red',label= sigma_x)
plt.axhline(avg_x-sigma_x, c='red')

plt.show()

print(np.mean(x))
print(np.std(x))