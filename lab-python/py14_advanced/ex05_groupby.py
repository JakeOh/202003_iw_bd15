import numpy as np
import pandas as pd

np.random.seed(1)

df = pd.DataFrame(data={'key': list('AAABBB'),
                        'data': np.random.randint(0, 10, 6)})
print(df)

g = df.groupby('key')['data']
print(g, '\n')

print(g.mean(), '\n')
print(g.agg('mean'), '\n')
print(g.apply(np.mean), '\n')
# agg: 함수 이름(np.mean), 함수를 찾을 수 있는 문자열('mean')
# apply: 함수 이름
print(g.transform(np.mean), '\n')

# GroupBy 객체에 lambda를 apply/transform으로 적용
print(g.apply(lambda x: 2 * x), '\n')
print(g.transform(lambda x: 2 * x), '\n')

# transform
#   1) 순위
#   2) normalize: 데이터의 평균을 0, 표준편차를 1이 되도록 변환

print(df['data'].rank(ascending=False))
# g = df.groupby('key')['data']
print(g.rank())
print(g.transform(lambda x: x.rank()))

df['normalized'] = g.transform(lambda x: (x - x.mean()) / x.std())
print(df)

df['norm2'] = (df['data'] - g.transform(np.mean)) / g.transform(np.std)
print(df)

