import pandas as pd
import numpy as np

# 중복된 row 삭제.
df = pd.DataFrame({'k1': ['a', 'b', 'a', 'b', 'a', 'b', 'b'],
                   'k2': [1, 1, 2, 3, 3, 4, 4]})
print(df)

print(df.duplicated())
dropped = df.drop_duplicates()
print(dropped)

# 값 치환(replace)
s = pd.Series([1, 2, 999, 4, 5])
print(s)
# 999 값을 NA로 치환(대체)
s2 = s.replace(999, np.NaN)
print(s2)

s = pd.Series([1, -2, 3, 999, 4])
s2 = s.replace([-2, 999], [0, np.NaN])
print(s2)

# Series의 모든 음수 값들을 0으로 치환
s = pd.Series(np.random.randn(6))
print(s)
s2 = s.map(lambda x: 0 if x < 0 else x)
print(s2)


def transform(x):
    if x < 0:
        return 0
    else:
        return x


s3 = s.map(transform)
print(s3)

names = pd.Series(['scott', 'Tiger', 'KING'])
# names의 모든 값들을 소문자로 변경
names_lower = names.map(lambda x: x.lower())
print(names_lower)
# names의 모든 값들을 대문자로 변경
names_upper = names.map(lambda x: x.upper())
print(names_upper)

# DataFrame의 row/column 이름 변경
df = pd.DataFrame({'Aa': [1, 2], 'bB': [3, 4]},
                  index=['abc', 'Def'])
print(df)
print(df.index)  # row 이름
print(df.columns)  # column 이름

# row의 이름을 모두 대문자로 변경
df.index = df.index.map(lambda x: x.upper())
print(df)

# column의 이름을 모두 소문자로 변경
df.columns = df.columns.map(lambda x: x.lower())
print(df)

# pd.DataFrame.rename() 메서드
df.rename(index=str.lower, columns=str.upper, inplace=True)
print(df)

df.rename(columns={'AA': 'column1'}, inplace=True)
print(df)
