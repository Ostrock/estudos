# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:43:40 2020

@author: guilh
"""

'''
Distribuição Normal (Gaussiana) é um tipo de distribuição em que a media é igual à mediana (ou muito
próxima). Ou seja, a Obliquidade é zero ou próxima de zero.

Mostra quão Incomum é um valor específico.

há uma variação aceitável mas é usada para saber o quão aceitável ela é.
Regra Empírica:
    68% dos valores estão há 1 desvio padrão da média.
        Media – DP >= X <= Media + DP
    95% dos valores estão há 2 desvio padrões da média.
        Media – 2*DP >= X <= Media + 2*DP
    99.7% dos valores estão há 3 desvio padrões da média.
        Media – 3*DP >= X <= Media + 3*DP
        
Teorema Central do Limite
    Todas as distribuições serão normais se a amostra for grande o bastante
    Populações tendem a ser normalmente distribuídas.
    
Uma extrapolação do Teorema diz que em eventos naturais as distribuições tendem a serem normais
conforme o tamanho da amostra aumente.
'''

import pandas as pd
folder = 'C:/Users/guilh/OneDrive/Documentos/code/python/fcd/'
file = folder + 'mamalia_sleep.csv'

df_mamiferos = pd.read_csv(file)

sono = df_mamiferos['sleep_total']

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

media = sono.mean()
devpd = sono.std()
min = sono.min()
max = sono.max()
n = sono.count()

# necessário informar média e desvio padrão
distr_sono = stats.norm(media, devpd)

x = np.linspace(min, max, n)

# PDF
y = distr_sono.pdf(x)

plt.plot(x,y)

# CDF
y = distr_sono.cdf(x)
plt.plot(x,y)

