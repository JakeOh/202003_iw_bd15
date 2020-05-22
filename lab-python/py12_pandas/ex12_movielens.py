import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def h_line():
    print()
    print('-' * 30)
    print()


# ../datasets/movielens/ 폴더 안에 있는
# ratings, users, movies 파일들을 읽어서 DataFrame을 생성
# ratings와 users를 merge(inner join)
# 위에서 merge된 결과와 movies를 merge(inner join)
# DataFrame 확인
# 영화 제목별 평점의 평균 출력
# 영화 제목별 성별 평점의 평균을 출력

path = '../datasets/movielens/'
rating_names = ['user_id', 'movie_id', 'rating', 'timestamp']
user_names = ['user_id', 'gender', 'age', 'occupation', 'zip_code']
movie_names = ['movie_id', 'title', 'genres']

ratings = pd.read_csv(path + 'ratings.dat',
                      sep='::', engine='python',
                      header=None, names=rating_names)
print(ratings.iloc[:5])

h_line()
users = pd.read_csv(path + 'users.dat',
                    sep='::', engine='python',
                    header=None, names=user_names)
print(users.iloc[:5])

h_line()
movies = pd.read_csv(path + 'movies.dat',
                     sep='::', engine='python',
                     header=None, names=movie_names)
print(movies.iloc[:5])

h_line()
data = pd.merge(pd.merge(ratings, users), movies)
print(data.iloc[:5])

h_line()
data.info()

h_line()
by_title = data.groupby('title')['rating'].mean()
print(by_title)

h_line()
by_title_gender = data.pivot_table(values='rating',
                                   index='title',
                                   columns='gender',
                                   aggfunc='mean')
print(by_title_gender)

h_line()
# 평점의 평균이 높은 순서로 10개의 영화 제목과 평점 평균을 출력
top10 = by_title.sort_values(ascending=False)[:10]
print(top10)

h_line()
# 여성의 평점 평균이 높은 순서로 10개의 영화 제목과 평점 평균을 출력
top10 = by_title_gender.sort_values(by='F', ascending=False)[:10]
print(top10)

h_line()
# 남성의 평점 평균이 높은 순서로 10개의 영화 제목과 평점 평균을 출력
top10 = by_title_gender.sort_values(by='M', ascending=False)[:10]
print(top10)

h_line()
# 전체 DataFrame에서 title이 등장하는 횟수(count) 찾아보세요.
rating_counts = data['title'].value_counts()  # 내림차순 정렬되어 있음.
print(rating_counts)

h_line()
rating_counts2 = data.groupby('title').size()  # 인덱스(title)로 정렬.
print(rating_counts2)

h_line()
# 가장 많이 평점을 받은 영화 상위 20개를 찾아보세요.
top_rating20 = rating_counts[:20]
print(top_rating20)

h_line()
# rating_counts의 요약(기술) 통계량
print(rating_counts.describe())
sns.boxplot(y=rating_counts)
plt.show()

h_line()
# rating_counts에서 리뷰 횟수가 350회 이상인 영화 제목들을 선택
indexer = rating_counts.index[rating_counts >= 350]
print(indexer)

h_line()
# 제목별 평점 평균 DataFrame(by_title)에서 평점이 높은 상위 10개 영화
# print(by_title.loc[indexer])
top10 = by_title.loc[indexer].sort_values(ascending=False)[:10]
print(top10)

h_line()
# 350회 이상 평점을 받은 영화들 중에서 여성이 높은 평점을 준 영화 상위 10개
top10 = by_title_gender.loc[indexer].sort_values(by='F', ascending=False)[:10]
print(top10)

h_line()
# 350회 이상 평점을 받은 영화들 중에서 남성이 높은 평점을 준 영화 상위 10개
top10 = by_title_gender.loc[indexer].sort_values(by='M', ascending=False)[:10]
print(top10)

# 여성과 남성의 평점 (평균) 차이가 큰 영화 상위 10개
# 1) 여성이 더 높은 평점을 준 10개
# 2) 남성이 더 높은 평점을 준 10개

# 평점 평균의 차이를 컬럼에 추가
by_title_gender['diff'] = by_title_gender['F'] - by_title_gender['M']
active_titles = by_title_gender.loc[indexer]  # 350회 이상 평점을 받은 영화

h_line()
top_diff10 = active_titles.sort_values(by='diff', ascending=False)[:10]
print(top_diff10)

h_line()
top_diff10_male = active_titles.sort_values(by='diff')[:10]
print(top_diff10_male)

h_line()
# 남녀 평점 차이가 큰 영화 20개에서 가장 많이 등장하는 장르 5개를 출력
# 1) 여성이 높은 평점을 준 20개 영화에서 자주 등장하는 장르 5개
# 여성이 높은 평점을 준 영화 20개 제목들
top20 = active_titles.sort_values(by='diff', ascending=False)[:20]  # DataFrame
female_tiles = top20.index  # DataFrame의 index -> 영화 제목
print(female_tiles)

# 2) 남성이 높은 평점을 준 20개 영화에서 자주 등장하는 장르 5개
# 남성이 높은 평점을 준 영화 20개 제목들
top20_m = active_titles.sort_values(by='diff')[:20]  # DataFrame
male_titles = top20_m.index  # DataFrame index
print(male_titles)

h_line()
# movies 데이터 프레임에서 title 컬럼을 인덱스로 만듦.
movies_with_index = movies.set_index(keys='title')
print(movies_with_index.iloc[:5])

h_line()
female_movies = movies_with_index.loc[female_tiles, 'genres']
print(female_movies)

h_line()
female_genres = []  # 영화 장르들을 추가할 리스트
for genres in female_movies:
    female_genres.extend(genres.split('|'))
# Python list를 pandas Series 객체로 변환
female_genres = pd.Series(female_genres)
print(female_genres.value_counts())

h_line()
male_movies = movies_with_index.loc[male_titles, 'genres']
male_genres = []
for genres in male_movies:
    male_genres.extend(genres.split('|'))
male_genres = pd.Series(male_genres)
print(male_genres.value_counts())
