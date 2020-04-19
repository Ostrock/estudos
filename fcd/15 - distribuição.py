# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:13:35 2020

@author: guilh
"""

'''
Em teoria da probabilidade e em estatística, uma distribuição de probabilidade
descreve o comportamento aleatório de um fenômeno dependente do acaso.

A distribuição de probabilidade pode modelar incertezas e descrever fenômenos 
físicos, biológicos, econômicos, entre outros.

Probabilidade é uma medida que tenta prever fenômenos aleatórios sob os quais
não temos conhecimento ou controle de todas as variáveis.

Sobre a natureza dos números, uma distribuição pode ser:
    Discreta: Números contáveis (lados de uma moeda, faces de um dado, etc)
    Contínua: Números não contáveis (valores financeiros, peso, etc)
    
Distribuição é o estudo da frequência dos valores de uma variável numa 
amostragem.
    Distribuição de Frequência. (ocorrência em uma determinada faixa de valores
gera um gráfico de histograma)
    Distribuição de Probabilidade
        Cumulative Density Function (CDF) é a distribuição acumulada de 
        probabilidade (pnorm)
        Probability Density Function (PDF) é a distribuição pontual de 
        probabilidade (dnorm)

Obliquidade (Skew) e Curtose (Kurtosis)

Obliquidade (Skewness) é a medida da assimetria de uma curva de distribuição.
A obliquidade pode ser positive, negativa ou zero. Ela descreve a inclinação
da curva.

Negative Skew = concentra a maior parte dos valores acima da média
                o ponto mais alto está acima da média
                pende à direita
                Indicativo de distribuição normal
                
Positive Skew = concentra a maior parte dos valores abaixo da média
                o ponto mais alto está abaixo da média
                pende à esquerda
                
Curtose é a medida do achatamento da curva de distribuição. Ela descreve a 
forma da curva.

A medida de curtose é últil para verificar o peso dos “outliers” nos dados. 
Curtose alta indica um peso maior, o que pode ser um indicativo de problemas 
na tentativa de usar esses dados para fazer previsões.


Curtose zero e olbliquidade (skew) zero é uma distribuição normal

Distribuição normal = completamente simétrica, os valores mais extremos estão a
uma distância de até três desvios padrão da média

Kurtose positiva = valores extremos estão a uma distância acima dos 
três desvios padrões da média curva mais pontuda

Kurtose negativa =  valores extremos estão a uma distância menor da média 
(curva achatada), até três desvios padrões da média

''' 

import pandas as pd
folder = 'C:/Users/guilh/OneDrive/Documentos/code/python/fcd/'
file = folder + 'mamalia_sleep.csv'

df_mamiferos = pd.read_csv(file)

sono = df_mamiferos['sleep_total']

# Obliquidade para todo o data frame 
'''
Afeta as colunas de valores numéricos
Axis = 0 ou 1
0 = linhas representantes diversas observações e colunas as diferentes variáveis
1 = os valores estão como linhas representando uma informação diferente

skipna = forma de lidar com valores nulos, pode pular esses valores
True = pula o valor nulo
False = não pula o valor 
'''
df_mamiferos.skew(axis=0, skipna=True)

'''
Alguns tem valores altos, alguns baixos
Obliquidade é a medida de assimetria 
Se 0 = o centro da curva está no meio, matade dos dados estão acima e metada
    está abaixo
Se negativa a maior parte dos valores se encontra em posição acima da média
Se positiva a mior parte dos valores se encontra abaixo da média 

sleep_total    0.054255 -> positiva próxima de zero
sleep_rem      1.536348
sleep_cycle    1.646095 
awake         -0.053244 -> negativa próxima a zero (complementar à sleep_total)
brainwt        4.886142
bodywt         7.364201
dtype: float64
'''

sono.skew(axis=0,skipna=True)
# 0.054254905263379366

df_mamiferos.kurtosis(axis=0, skipna=True)
'''
Kutosis mede o achatamento de uma curva
se negativo é mais baixo, mais espalhado
se positiva é mais alta, mais concentrada
se zero representa um equilíbrio

Analisa o peso dos outliners (pontos fora da curva) influenciam no cálculo da 
média 
se positiva ou negativa, há uma influencia maior desses extremos no cálculo da média

sleep_total    -0.616265
sleep_rem       3.287078
sleep_cycle     2.418337
awake          -0.616193
brainwt        24.041834
bodywt         58.655642
dtype: float64
'''
sono.kurtosis(axis=0, skipna=True)
# -0.6162646603313915

sono.describe()
'''
count    83.000000
mean     10.433735
std       4.450357
min       1.900000
25%       7.850000
50%      10.100000
75%      13.750000
max      19.900000
Name: sleep_total, dtype: float64

A obliquidade da sleep_total é muito próxima de zero, a média e a mediana são 
também muito próximas o que nos leva a cre ser uma distribuição normal
'''

'''
# Questionário 04 - Exame - Parte 2.2 - Introdução a Distribuição #

## 01 - Qual dessas definições de distribuição é a mais correta?

### a) Estudo de como as estatísticas de um número se distribuem em um gráfico
### b) Descreve o comportamento aleatório de uma variável (X)
### c) Calcula a probabilidade de determinado valor estar a uma determinada quantidade de desvios padrões da média da variável
### d) Modela a incerteza encontrada em fenômeros naturais ou artificiais de variáveis discretas


## 02 - Sobre distribuições, marque a opção incorreta.

### a) Uma distribuição pode descrever números discretos ou contínuos
### b) Uma distribuição pode mostrar a frequência ou a probabilidade de um valor
### c) Uma função PDF mostra a probabilidade daquele valor ser encontrado na distribuição
### d) Uma função CDF mostra a probabilidade de um valor na distribuição ser maior ou igual ao valor analisado. (X)
### e) A quantidade de elementos entre dois valores discretos é finita


## 03 - Uma distribuição teve suas medidas estatísticas calculadas e encontrou-se uma obliquidade igual a -367543.45 
##     e uma curtose de 5432. Sobre esses resultados, qual a alternativa mais correta?

### Obliquidade Positiva = Maioria dos valores abaixo da média
### Obliquidade Negativa = Maioria dos valores acima da média
#####
### Curtose Positiva Alta: Extremidades além de 3 DP da média
### Curtose Negativa Alta: Extremidades abaixo de 3 DP da média
#####

### a) A maioria dos valores está na região acima da média e os valores extremos 
###    estão além de três desvios padrões da média (X)

### b) A maioria dos valores está na região acima da média e os valores extremos 
###    estão abaixo de três desvios padrões da média

### c) A maioria dos valores está na região abaixo da média e os valores extremos 
###    estão além de três desvios padrões da média

### d) A maioria dos valores está na região abaixo da média e os valores extremos 
###    estão abaixo de três desvios padrões da média

### e) A maioria dos valores está na região abaixo da média e os valores extremos 
###    estão até três desvios padrões da média



## 04 - Uma distribuição teve suas medidas estatísticas calculadas e encontrou-se uma obliquidade igual a 0.07 
##      e uma curtose de -128. Sobre esses resultados, qual a alternativa mais correta?

### a) A maioria dos valores está na região acima da média e os valores extremos 
###    estão além de três desvios padrões da média

### b) A maioria dos valores está na região acima da média e os valores extremos 
###    estão abaixo de três desvios padrões da média

### c) A maioria dos valores está na região abaixo da média e os valores extremos 
###    estão além de três desvios padrões da média

### d) A maioria dos valores está na região próxima da média e os valores extremos 
###    estão abaixo de três desvios padrões da média (X)

### e) A maioria dos valores está na região abaixo da média e os valores extremos 
###    estão abaixo de três desvios padrões da média



## 05 - Uma distribuição teve suas medidas estatísticas calculadas e encontrou-se uma 
##      obliquidade igual a 7543 e uma curtose de -2763. Sobre esses resultados, qual a alternativa mais correta?

### a) A maioria dos valores está na região acima da média e os valores extremos 
###    estão além de três desvios padrões da média

### b) A maioria dos valores está na região acima da média e os valores extremos 
###    estão abaixo de três desvios padrões da média

### c) A maioria dos valores está na região abaixo da média e os valores extremos 
###    estão além de três desvios padrões da média

### d) A maioria dos valores está na região abaixo da média e os valores extremos 
###    estão abaixo de três desvios padrões da média (X)

### e) A maioria dos valores está na região abaixo da média e os valores extremos 
###    estão até três desvios padrões da média
'''