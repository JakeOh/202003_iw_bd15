import pandas as pd

# pd.DataFrame: 테이블 또는 표와 같은 2차원 모양의 데이터 타입.
data = {
    'city': ['Seoul', 'Seoul', 'Seoul', 'Jeju', 'Jeju', 'Jeju'],
    'year': [2018, 2019, 2020, 2018, 2019, 2020],
    'pop': [1.5, 1.7, 1.8, 0.5, 0.6, 0.5]
}  # dict
df = pd.DataFrame(data)
print(df)
print(df.shape)  # (row, col)
print(df.index)  # DataFrame.index: row(행)의 인덱스
print(df.columns)  # DataFrame.columns: column(열)의 인덱스

# DataFrame에서 컬럼 선택
print(df['city'])  # dictionary-like 방법
print(df.city)  # attribute-like 방법

# DataFrame에서 row 선택
print(df.iloc[0])
print(df.loc[0])
print(df.iloc[0:2])
print(df.loc[0:2])
print(df.loc[2, 'pop'], df.iloc[2, 2])

print(df)
# select * from df where df.year = 2020
print(df[df['year'] == 2020])  # df.year == 2020
print(df[df['pop'] > 1.0])  # df.pop 안됨
