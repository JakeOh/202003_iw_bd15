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
# movies.dat, ratings.dat, users.dat 세 개의 파일이 있습니다.
# 1) movies, ratings, users DataFrame을 생성
# 2) movies, ratings DataFrame을 merge: inner, left 비교
# 3) 2)에서 생성된 DataFrame과 users를 merge: inner, left 비교

movie_names = ['movie_id', 'title', 'genres']
movies = pd.read_csv('../datasets/movielens/movies.dat',
                     sep='::', engine='python',
                     header=None, names=movie_names)
print(movies.iloc[:5])
movies.info()

rating_names = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv('../datasets/movielens/ratings.dat',
                      sep='::', engine='python',
                      header=None, names=rating_names)
print(ratings.iloc[:5])
ratings.info()

user_names = ['user_id', 'gender', 'age', 'occupation', 'zip_code']
users = pd.read_csv('../datasets/movielens/users.dat',
                    sep='::', engine='python',
                    header=None, names=user_names)
print(users.iloc[:5])
users.info()

df_inner = pd.merge(movies, ratings, on='movie_id')  # how='inner'
# df_inner = movies.merge(ratings, on='movie_id')
df_inner.info()
print(df_inner.iloc[:5])  # df_inner.head()
print(df_inner.iloc[-5:])  # df_inner.tail()

df_left = pd.merge(movies, ratings, on='movie_id', how='left')
# df_left = movies.merge(ratings, on='movie_id', how='left')
df_left.info()
# left join(merge)에서는 movies(영화 정보)에는 있지만,
# ratings(별점 정보)에는 없는 데이터들이 포함된다.
print(df_left[df_left['user_id'].isnull()])

# movies와 ratings를 inner join한 결과와 users를 merge
data_inner = df_inner.merge(users, on='user_id')
# data_inner = pd.merge(df_inner, users, on='user_id')
data_inner.info()
print(data_inner.iloc[100])

data_left = df_inner.merge(users, on='user_id', how='left')
# data_left = pd.merge(data_left, users, on='user_id', how='left')
data_left.info()
