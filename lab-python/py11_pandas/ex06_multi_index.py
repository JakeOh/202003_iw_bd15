import pandas as pd
import numpy as np

# 계층적 색인(hierarchical indexing)
s = pd.Series(data=np.random.randn(9),
              index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                     [1, 2, 3, 1, 2, 1, 2, 2, 3]])
print(s)

print(s.values)  # Series: 1차원 데이터
print(s.index)  # MultiIndex

# MultiIndex의 속성들
print('nlevels:', s.index.nlevels)  # hierarchy(계층)의 수
print('levels:', s.index.levels)  # 계층별 level들의 리스트
print('codes:', s.index.codes)

# MultiIndex를 갖는 Series에서 원소를 접근하는 방법:
print(s['a'])
print(s['b'])
print(s[1], s.iloc[1])  # 2nd hierarchy의 인덱스를 의미하지 않음.

print(s['a':'c'])
print(s.loc['a':'c'])

print(s['a', 1], s.loc['a', 1])

print(s.loc['a', 1:2])
print(s.loc['a':'d', 1])
print(s.loc[:, 1])

# Pivoting
print(s)
wide = s.unstack()
print(wide)

narrow = wide.stack()
print(narrow)

# DataFrame에서 계층적 인덱스
df = pd.DataFrame(np.arange(12).reshape(4, 3),
                  columns=[['a', 'a', 'b'], ['a1', 'a2', 'b1']],
                  index=[['A', 'A', 'B', 'B'], [1, 2, 1, 2]])
print(df)

df.index.names = ['key1', 'key2']
df.columns.names = ['c1', 'c2']
print(df)

# DataFrame에서 특정 컬럼 선택
print(df['a'])
print(df.a)

# DataFrame 특정 행(row)를 선택
print(df.loc['A'])

# DataFrame에서 row index('A', 1)인 row를 선택
print(df.loc[('A', 1)])

# 계층적 인덱스를 이용한 요약 통계
print(df)
print(df.sum(level='key2'))  # axis=0은 기본값이므로 생략.
print(df.sum(level='c1', axis=1))  # axis=1은 생략 불가.

# DataFrame의 특정 컬럼(들)을 row index로 만들 수 있음.
df = pd.DataFrame({'class': [1, 1, 1, 2, 2, 2],
                   'stu_id': [1, 2, 3, 1, 2, 3],
                   'kor': [10, 20, 50, 90, 80, 70],
                   'eng': [99, 88, 60, 70, 40, 50]})
print(df)

df_reindexed = df.set_index(['class', 'stu_id'])
print(df_reindexed)

print(df_reindexed.mean(level='class'))  # -> group_by()와 동일한 기능.

# 인덱스를 다시 컬럼으로 변환
df_reset = df_reindexed.reset_index()
print(df_reset)

