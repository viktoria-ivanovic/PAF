import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv('monthly_in_situ_co2_mlo (1).csv',header=63)

print(data)

CO2=data[:][3]
dates=data[:][2]

plt.figure()
plt.plot(dates,CO2)
plt.show