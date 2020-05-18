# pandas.DataFrame에서 문자열 다루기

import pandas as pd

col_name = ['movie_id', 'title', 'genres']
movies = pd.read_csv('../datasets/movielens/movies.dat',
                     header=None, names=col_name, sep='::')
print(movies.iloc[:5])

# movies DataFrame에서 Animation들로 이루어진 부분집합
print(movies['genres'].str.contains('Animation'))
animations = movies[movies['genres'].str.contains('Animation')]
print(animations)

# 장르가 Romance, Comedy인 영화들을 찾아보세요.
romance_comedy = movies[movies.genres.str.contains('Romance') &
                        movies.genres.str.contains('Comedy')]
print(romance_comedy)

# movies DataFrame의 genres 컬럼의 문자열을 모두 소문자로 변경
movies['genres'] = movies.genres.str.lower()
print(movies)

# 영화 제목
print(movies.loc[:9, 'title'])
print(movies.iloc[-10:, 1])

# movies DataFrame에서 title 컬럼을 이용해서, 영화 발표 연도만 출력.
title = 'Toy Story (1995)'
print(title[0:5])  # Python의 문자열(str)은 리스트처럼 인덱스를 사용 가능.
print(title[-5:-1])

print(movies['title'].str[-5:-1])  # movies.title.str[-5:-1]

# movies DataFrame에 year 컬럼을 추가하고, 영화 발표 연도를 컬럼의 값으로
movies['year'] = movies.title.str[-5:-1]
print(movies.iloc[:5])

# year 컬럼의 데이터 타입?
movies.info()  # object -> 문자열
# movies DataFrame의 year 컬럼의 데이터 타입을 'int32'로 변환
movies['year'] = movies['year'].astype('int32')
movies.info()

# 연도별 영화 숫자(개수)
print(movies['year'].value_counts())  # pandas.Series
# 가장 영화 개수가 많은 연도 상위 10개
print(movies['year'].value_counts()[:10])

