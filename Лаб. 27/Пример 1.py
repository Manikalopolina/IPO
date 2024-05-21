'''Способы создания одномерного массива Series'''

import numpy as np
import pandas as pd
s = pd.Series([12, -4, 7, 9])
print(s)

d = {'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5}
s1 = pd.Series(d)
print('\n\n', s1)

d1 = 9
s2 = pd.Series(d, ['q', 'w', 'e', 'r', 't'])
print('\n\n', s2)

s3 = pd.Series([11, 22, 33, 44, 55], ['a', 'b', 'c', 'd', 'e'])
print('\n\n', s3)

ar = np.array([1, 2, 3, 4, 5])
s4 = pd.Series(ar, ['a', 'b', 'c', 'd', 'e'])
print('\n\n', s4)
