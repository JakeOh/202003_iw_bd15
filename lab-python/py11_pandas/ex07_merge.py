import numpy as np
import pandas as pd

# DataFrame 합치기: merge, join, concat

df1 = pd.DataFrame({'key': ['a', 'a', 'b', 'c', 'a', 'c'],
                    'data1': range(6)})
print(df1)

df2 = pd.DataFrame({'key': ['a', 'c', 'd'],
                    'data2': [10, 20, 30]})
print(df2)

# pandas.merge(left_df, right_df, ...) 함수
m1 = pd.merge(df1, df2, on='key')  # on: merge 기준이 되는 컬럼(들) 이름
print(m1)

# how: merge 방법(inner: 기본값, left, right, outer)
m2 = pd.merge(df1, df2, on='key', how='left')
print(m2)

# pandas.DataFrame.merge() 메서드: left_df.merge(right_df, ...)
m3 = df1.merge(df2, on='key')
print(m3)

m4 = df1.merge(df2, on='key', how='left')
print(m4)

m5 = df2.merge(df1, on='key', how='left')
print(m5)

# ../datasets/movielens/ 폴더에는
# movies.dat, ratings.data, users.dat 세 개의 파일이 있습니다.
# 1) movies, ratings, users DataFrame을 생성
# 2) movies, ratings DataFrame을 merge: inner, left 비교
# 3) 2)에서 생성된 DataFrame과 users를 merge: inner, left 비교

