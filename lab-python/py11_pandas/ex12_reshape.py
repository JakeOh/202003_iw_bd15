# DataFrame의 모양(shape) 바꾸기
# pivot: row -> column: Long format -> Wide format
# melt: column -> row: Wide format -> Long format
# unstack: MultiIndex -> columns: Long -> Wide
# stack: columns -> MultiIndex: Wide -> Long

import numpy as np
import pandas as pd

# Index를 갖는 DataFrame을 생성
df = pd.DataFrame(data=np.arange(6).reshape((2, 3)),
                  index=['Seoul', 'GG'],
                  columns=['a', 'b', 'c'])
print(df)

# stack: 컬럼(Wide) -> MultiIndex(Long)
df_stacked = df.stack()
print(df_stacked)
print(df_stacked.index)

# unstack: MultiIndex(Long) -> 컬럼(Wide)
df_unstacked1 = df_stacked.unstack()  # level=1
print(df_unstacked1)

df_unstacked2 = df_stacked.unstack(level=0)
print(df_unstacked2)

s = pd.Series(data=np.arange(5),
              index=[['One', 'One', 'One', 'Two', 'Two'],
                     ['a', 'b', 'c', 'b', 'c']])
s.index.names = ['key1', 'key2']
print(s)

# print(s.unstack())
# print(s.unstack(level=-1))  # level=1: 인덱스 레벨
print(s.unstack('key2'))  # 인덱스 이름

# print(s.unstack(level=0))
print(s.unstack('key1'))

df = pd.DataFrame(data={'left': np.arange(6),
                        'right': np.arange(6) * 5},
                  index=[['A', 'A', 'A', 'B', 'B', 'B'],
                         ['one', 'two', 'three'] * 2])
df.index.names = ['state', 'number']
print(df)

print(df.unstack('number'))
print(df.unstack('state'))

print(df.unstack('state').stack(level=0))

t = df.unstack('state').stack(level=0)
t = t.swaplevel()
print(t.sort_index())


