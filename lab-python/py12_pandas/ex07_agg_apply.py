import numpy as np
import pandas as pd

np.random.seed(1)  # 실행할 때마다 동일한 난수가 만들어지도록 하기 위해서
df = pd.DataFrame({'species': ['A'] * 3 + ['B'] * 3,
                   'data1': np.arange(6),
                   'data2': np.arange(6, 12),
                   'data3': np.arange(12, 18)})
print(df)


def test_fn(x):
    print(type(x))
    print(x)
    return 1


print('-' * 20)
rslt = test_fn(1234)
print('rslt =', rslt)

print('-' * 20)
rslt = test_fn('hello')
print('rslt =', rslt)

print('-' * 20)
rslt = test_fn(df['data1'])
print('rslt =', rslt)

print('-' * 20)
rslt = test_fn(df)
print('rslt =', rslt)

print('-' * 20)
by_species = df.groupby('species')
for n, g in by_species:
    print(g)

print('-' * 20)
# groupby가 된 객체에 aggregate로 test_fn을 적용
print(by_species.agg('mean'))

print('-' * 20)
result = by_species.agg(test_fn)
print(result)

print('-' * 20)
result = by_species.apply(test_fn)
print(result)

# agg, aggregate 함수는 groupyby된 데이터 프레임의 각 컬럼들을 함수의 argument로 전달.
# -> (그룹/부분집합 개수) * (컬럼 개수) 만큼 함수가 호출되고, 리턴값이 생김.
# apply 함수는 groupby된 데이터 프레임을 함수의 argument로 전달.
# -> 그룹/부분집합 개수만큼 함수가 호출되고, 리턴값이 생김.

print('-' * 20)
result = by_species[['data1', 'data2']].agg(test_fn)
print(result)

print('-' * 20)
result = by_species[['data1', 'data2']].apply(test_fn)
print(result)


def max_min(x):
    print(type(x))
    print(x)
    return x.max() - x.min()


print('-' * 20)
rslt = max_min(df['data2'])
print('rslt =', rslt)

print('-' * 20)
rslt = max_min(df[['data1', 'data2']])
print(rslt, type(rslt))

print('-' * 20)
result = by_species.agg(max_min)
print(result)

print('-' * 20)
result = by_species.apply(max_min)
print(result)

# 적용하는 함수의 구현 여부에 따라서 agg와 apply가 동작 방식은 다르지만,
# 같은 결과를 줄 수 있다.
