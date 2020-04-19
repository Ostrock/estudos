# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 05:47:22 2020

@author: guilh
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

folder = 'C:/Users/guilh/OneDrive/Documentos/code/python/fcd/'
file = folder + 'cereals.csv'

df_cereals = pd.read_csv(file)

cal = df_cereals['calories']
df_cereals['fiber'].mode()


r_min = df_cereals['rating'].min()
r_max = df_cereals['rating'].max()

ampl = (r_max - r_min)

a = round(ampl)

ma_cal = cal.mean()
max_cal = cal.max()
min_cal = cal.min()
std_cal = cal.std()
n = cal.count()

distr_cal = stats.norm(ma_cal, std_cal)

cdf_cal_130 = distr_cal.cdf(130)

a = max_cal - min_cal
a

df_cereals.kurtosis(axis=0,skipna=True)

df_cereals[0]

df_cereals['calories'].std()
df_cereals['protein'].std()
df_cereals['fat'].std()
df_cereals['sodium'].std()
df_cereals['fiber'].std()

np.percentile(df_cereals['sodium'], 85, interpolation='linear')

df_cereals.skew(axis=0,skipna=True)

np.var(cal)
cal.skew(axis=0,skipna=True)
cal.describe()
