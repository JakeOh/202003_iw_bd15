# 샘플링
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.DataFrame(np.arange(20).reshape((5, 4)))
print(df)

sample1 = df.sample(3)
print(sample1)

sample2 = df.sample(2)
print(sample2)

length = len(df)  # DataFrame의 length = row의 개수
print(length)

sampler = np.random.permutation(length)
print(sampler)

print(df.iloc[sampler])

train_set = df.iloc[sampler[:3]]
test_set = df.iloc[sampler[-2:]]
print(train_set)
print(test_set)

# seaborn 패키지의 iris 샘플 데이터를 로딩
iris = sns.load_dataset('iris')
print(iris.iloc[:5])  # iris.head()
print(iris.iloc[-5:])  # iris.tail()

# iris DataFrame을 iris_train(100개), iris_test(50개) 두개로 샘플링
sampler = np.random.permutation(len(iris))
print(sampler)
iris_train = iris.iloc[sampler[:100]]
iris_test = iris.iloc[sampler[-50:]]
print(iris_train['species'].value_counts())
print(iris_test['species'].value_counts())

data = iris.iloc[:, :4]
value = iris.iloc[:, 4]
print(data.head())
print(value.head())
# data, value를 data_train/data_test, value_train/value_test로 샘플링.
sampler = np.random.permutation(150)
data_train = data.iloc[sampler[:100]]
data_test = data.iloc[sampler[-50:]]
value_train = value.iloc[sampler[:100]]
value_test = value.iloc[sampler[-50:]]

# one-hot encoding
df = pd.DataFrame({'data': range(6),
                   'spam': ['y', 'y', 'n', 'n', 'y', 'y']})
print(df)

dummies = pd.get_dummies(df['spam'])
print(dummies)
df_one_hot = df.join(dummies)
print(df_one_hot)

df = pd.DataFrame({'data': range(6),
                   'species': ['a', 'b', 'a', 'c', 'a', 'b']})
print(df)

dummies = pd.get_dummies(df['species'])
print(dummies)

df_one_hot = df.join(dummies)
print(df_one_hot)

# iris DataFrame을 one-hot encoding이 추가된 DF로 변환.
dummies = pd.get_dummies(iris['species'])
iris_one_hot = iris.join(dummies)
print(iris_one_hot[:5])
print(iris_one_hot[50:55])
print(iris_one_hot[100:105])

# ../datasets/movielens/movies.dat 파일을 읽어서 DataFrame 생성
col_names = ['movie_id', 'title', 'genres']  # DataFrame의 컬럼 이름
movies = pd.read_csv('../datasets/movielens/movies.dat',
                     header=None,
                     sep='::',
                     names=col_names,
                     engine='python')
print(movies.iloc[:5])
print(movies.iloc[-5:])

# 영화 장르
all_genres = []
for x in movies['genres']:
    all_genres.extend(x.split('|'))
print(all_genres)

# all_genres에서 중복되지 않은 값들로만 이루어진 리스트를 생성.
genres = pd.unique(all_genres)
print(genres)

# 영화개수(3883)x영화장르개수(18) 모양의 numpy.ndarray를 생성
zero_matrix = np.zeros(shape=(len(movies), len(genres)))
print(zero_matrix.shape)
print(zero_matrix)

# numpy.ndarray를 pandas.DataFrame으로 변환
dummies = pd.DataFrame(data=zero_matrix, columns=genres)
print(dummies)

# 첫번째 영화의 장르
g = movies['genres'][1]
print(g.split('|'))
indexer = dummies.columns.get_indexer(g.split('|'))
print(indexer)

for i, gen in enumerate(movies['genres']):
    indexer = dummies.columns.get_indexer(gen.split('|'))
    dummies.iloc[i, indexer] = 1
print(dummies)

print(dummies.iloc[1])

movies_with_genre = movies.join(dummies)
print(movies_with_genre.iloc[2])
