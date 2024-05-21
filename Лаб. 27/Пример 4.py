import numpy as np
import pandas as pd

d={'price': pd.Series([1,2,3], index=['v1', 'v2', 'v3']),
   'count': pd.Series([10, 12, 14], index=['v1', 'v2', 'v3'])}
df=pd.DataFrame(d)
print(df)

print('\n', df.index)
print('\n', df.columns)

d1=[{'price': 3, 'count': 8, 'count': 12}]
df1=pd.DataFrame(d1)
print('\n', df1)
print('\n', df1.info())

d2=np.array([[2, 5, 8], [1, 4, 7]])
df2=pd.DataFrame(d2)
print('\n', df2)