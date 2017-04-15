# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:27:23 2017

@author: Aniket Pant
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4*np.pi, 33)
y = np.sin(x)
plt.errorbar(x, y, fmt='ro', label="data",
             xerr=0.25, yerr=0.25, ecolor='black')
plt.plot(x, y)
plt.show()