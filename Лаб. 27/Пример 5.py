'''Выполнение операций выбора'''

import numpy as np
import pandas as pd

d={'price': np.array([1,2,3]), 'count': np.array([10,20,30])}
df=pd.DataFrame(d, index=['q','w','r'])
print(df)

print('\nОперация выбора столбца')
print(df['count'])

print('\nОперация выбора строки по метке')
print(df.loc['w'])

print('\nОперция выбора строки по индексу')
print(df.iloc[0])

print('\nОперация slice по строкам')
print(df[0:2])

print('\nОперация выбора строк отвечающих условию')
print(df[df['count']>=20])