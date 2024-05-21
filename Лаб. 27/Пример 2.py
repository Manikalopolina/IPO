'''Выбор элементов из массива Series'''
import numpy as np
import pandas as pd
s = pd.Series([11, 22, 33, 44, 55], ['a', 'b', 'c', 'd', 'e'])
print(s.iloc[1])

print(s.iloc[3])

print(s['d'])

print('\n\n', s[1:3])

print('\n\n', s[:3])

print('\n\n', s[['b', 'e']])

print('\n\n', s[s<=33])
