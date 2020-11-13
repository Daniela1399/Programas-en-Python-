# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 00:55:57 2020

@author: Daniela G. Osuna
"""

import matplotlib.pyplot as plt

Estados = ['Coahuila', 'Chiapas','Zacatecas','Jalisco','Total']
defunciones = [1934,1090,752,3396,5439]
colores = ['red','green','blue','orange','yellow']

plt.title('Defunciones por covid-19')
plt.ylabel('No.Defunciones')
plt.xlabel('Estados')
plt.grid()
plt.bar(Estados, height=defunciones, color=colores, width=0.8)
plt.show()