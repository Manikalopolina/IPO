import numpy as np
import pandas as pd
s=pd.Series([11, 22, 33, 44, 55], ['a', 'b', 'c', 'd', 'e'])
print(s)

s.iloc[1]=111
s['d']=222
print('\n\n', s)
s1=pd.Series([1,2,3,4,5], ['a', 'b', 'c', 'd', 'e'])
s_sum=s+s1
print('\n\n', s_sum)