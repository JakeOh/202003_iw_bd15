# Missing Data(결측치, NA) 처리
import numpy as np
import pandas as pd

# pandas.Series 객체 생성
s = pd.Series([1, np.NaN, 3, np.NaN, 5])
print(s)

# isnull(), notnull() 메소드
print(s.isnull())  # NA이면 True
print(s.notnull())  # NA가 아니면 True
print(s[s.notnull()])  # Series의 원소들 중에서 NA가 아닌 원소들을 선택

df = pd.DataFrame([ [1, 2, 3, 4],
                    [5, np.NaN, 7, 8],
                    [9, 10, np.NaN, 12],
                    [np.NaN, np.NaN, np.NaN, np.NaN] ])
print(df)
print(df.isnull())
# print(df[df.notnull()])

# 한 행에서 NA가 하나라도 있는 경우, 그 행을 삭제.
dropped = df.dropna()  # df.dropna(how='any')
print(dropped)

# 한 행에서 모든 데이터가 NA인 경우, 그 행을 삭제.
dropped2 = df.dropna(how='all')
print(dropped2)

# 한 열(column)에서 NA가 하나라도 있으면, 그 열(column)을 삭제
print(df.dropna(axis=1, how='any'))
# 한 컬럼의 데이터가 모두 NA인 경우, 그 컬럼을 삭제
print(df.dropna(axis=1, how='all'))

# DataFrame에서 인덱스 2번 컬럼이 NA가 아닌 row를 선택
# select * from df where df[2] is not null;
print(df[df[2].notnull()])

# DataFrame에서 인덱스 1번 컬럼이 NA가 아닌 row를 선택
print(df[df[1].notnull()])

# Missing Value(NA) 채우기: fillna()
# fillna() 메서드는 원본 Series, DataFrame을 변경하지 않고,
# 새로운 Series, DataFrame을 만들어서 리턴함.
# 원본 Series, DataFrame을 변경하고자 할 때는 inplace='True'로 설정.
print(s.fillna(0))
print(s)

s.fillna(0, inplace=True)
print(s)

# DataFrame의 모든 NA를 한가지 값으로 채울 때:
df1 = df.fillna(0)
print(df1)

# DataFrame에서 column별로 NA의 값들을 다르게 채울 때:
df2 = df.fillna({1: -1, 2: -999})
print(df2)

# DataFrame에서 이전값 또는 다음값으로 NA를 채우는 방법:
print(df)
df3 = df.fillna(method='ffill')  # method='ffill': 이전값으로 채우기
print(df3)

df4 = df.fillna(method='bfill')  # method='bfill': 다음값으로 채우기
print(df4)

# DataFrame에서 NA들을 그 컬럼의 평균값으로 대체
df5 = df.fillna({0: df[0].mean(), 1: df[1].mean()})
print(df5)

for i in range(df.shape[1]):
    # df[i] = df[i].fillna(df[i].mean())
    df[i].fillna(df[i].mean(), inplace=True)
print(df)
