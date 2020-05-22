import numpy as np
import pandas as pd

np.random.seed(1)
s = pd.Series(np.random.randn(5))

s[2] = np.nan
print(s)

mu = s.mean()
print('mean =', mu)

cleaned = s.fillna(mu)
print(cleaned)

df = pd.DataFrame({'region': ['A'] * 3 + ['B'] * 3,
                   'data1': np.random.randn(6),
                   'data2': np.random.randn(6)})

df.loc[1, 'data1'] = np.nan
df.loc[4, 'data2'] = np.nan
print(df)

mu = df.mean()
print(mu)

cleaned = df.fillna(mu)
print(cleaned)


def fill_mean(x):
    # x: Series, DataFrame
    # mu = x.mean()
    # cleaned = x.fillna(mu)
    # return cleaned
    return x.fillna(x.mean())


# region별 data1과 data2의 평균
means = df.groupby('region').mean()
print(means)

cleaned = df.groupby('region').apply(fill_mean)
print(cleaned)

cleaned = df.groupby('region').apply(lambda x: x.fillna(x.mean()))
print(cleaned)
