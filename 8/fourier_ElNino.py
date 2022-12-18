# -*- coding: utf-8 -*-
"""
Created on Mon May  2 08:36:30 2022

@author: TorstenSchmidt
"""

import numpy as np
import scipy
from matplotlib import pyplot as plt
import pandas as pd
from scipy.fft import fft

# Import der Daten
data = pd.read_excel('Delta_p.xlsx')
print(data)
t = data['t_m'].values
deltap = data['delta_p'].values

# Ausagbe im Diagramm
plt.plot(t,deltap)
plt.show()

# FFT
N = len(deltap)
# Sample Spacing
T = 1 # in Monaten!
yf = fft(deltap)
#yf[np.abs(yf)<20] = 0
f = np.linspace(0,0.5*1/T,int(N/2))

# Frequency Plot
plt.plot(1/f, np.abs(yf[0:int(N/2)]),'*')
plt.grid()
plt.show()


















