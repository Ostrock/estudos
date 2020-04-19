# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
import pandas as pd
import numpy as np

folder = 'C:/Users/guilh/OneDrive/Documentos/code/python/fcd/'
file = folder + 'mamalia_sleep.csv'

df_mamiferos = pd.read_csv(file)

sono = df_mamiferos['sleep_total']

# Média aritimética
ma = sono.mean()
ma

# Média ponderada
peso = df_mamiferos['bodywt']
peso = np.ceil(peso)

mp = (sono * peso).sum() / peso.sum()
mp

# média geométrica
# Média geométrica é sempre menor que a média aritimética
from scipy.stats.mstats import gmean

mg = gmean(sono)
mg

# média harmonica
# sempre menor que a média geométrica

from scipy.stats.mstats import hmean

hm = hmean(sono)
hm

import statistics as s

s.harmonic_mean(sono)

# ma > mg > ma (a média ponderada vai depender da variação do pesso atribuído )

# ma e mp são as mais flexiciveis, hm e mg não pode ser zero (mg não é indicada se um dos valores for igual a zero)