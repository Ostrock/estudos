# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
import pandas as pd
folder = 'C:/Users/guilh/OneDrive/Documentos/code/python/fcd/'
file = folder + 'mamalia_sleep.csv'

df_mamiferos = pd.read_csv(file)

df_mamiferos.describe()

sono = df_mamiferos['sleep_total']

sono.describe()

sono.count()
sono.mean()
sono.median()
sono.mode()
sono.min()
sono.max()

sono.quantile(0.25)

sono2 = df_mamiferos[df_mamiferos['name'] != 'Horse']['sleep_total']
sono2.quantile

# quantile usa a distanta linear

import numpy as np
np.percentile(sono2, 75, interpolation="midpoint") #13,75
np.percentile(sono2, 75, interpolation="lower") #13,7
np.percentile(sono2, 75, interpolation="higher") # 13,8
np.percentile(sono2, 75, interpolation="nearest") #13,8
np.percentile(sono2, 75, interpolation="linear")

# Manualmente
# i + (j-i) * fractil
13.7 + (13.8-13.7) * 0.75

sono.var()
sono.std()
sono2.std()

import matplotlib as plt

sono.plot(kind='hist', bins=15)
plt.xlabel('Horas de sono diária')

sono.plot(kind='box')

sono_ordem = df_mamiferos.groupby('order')['sleep_total'].mean()

sono_ordem.plot(kind='bar')

# somente top7
sono_ordem.sort_values()[-7:].plot(kind='bar')
plt.pyplot.ylabel('média de horas de sono')