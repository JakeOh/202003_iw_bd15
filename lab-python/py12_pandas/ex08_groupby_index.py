import numpy as np
import pandas as pd

groups = ['a', 'b'] * 4
print(groups)

types = ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three']
print(types)

np.random.seed(1)
df1 = pd.DataFrame({'group': groups,
                    'type': types,
                    'data1': np.random.randn(8),
                    'data2': np.random.randn(8)})
print(df1)

print('-' * 30)
print(df1.groupby('group').mean())

print('-' * 30)
print(df1.groupby('type').mean())

print('-' * 30)
print(df1.groupby(['group', 'type']).mean())

print('-' * 30)
df2 = df1.set_index(['group', 'type'])
df2.info()
print(df2)

print('-' * 30)
print(df2.groupby('group').mean())  # 인덱스의 level 이름을 찾음.

print('-' * 30)
print(df2.groupby(level='group').mean())  # 인덱스 level 이름

print('-' * 30)
print(df2.groupby(level=0).mean())  # 인덱스 level 숫자

print('-' * 30)
print(df2.groupby(level=[0, 1]).mean())
