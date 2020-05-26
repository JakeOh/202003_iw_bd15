import numpy as np
import pandas as pd

'''
groupby와 함께 사용되는 메서드
agg(aggregate) vs apply vs transform

* 함수 argument(input):
    - agg, transform: Series를 argument로 사용.
    - apply: DataFrame을 argument로 사용.
* 함수 return type(output):
    - agg, apply: scalar, Series, DataFrame
    - transform: input과 동일한 길이의 배열과 같은 형태
        scalar를 리턴하는 함수인 경우 broadcast가 될 수도 있음.
'''


def inspect_input(x):
    print('inspect 내부 type(x):', type(x))  # argument의 data type을 확인
    print('inspect 내부 x:', x)  # argument의 값을 확인
    raise   # 강제로 에러 발생


np.random.seed(1)

df = pd.DataFrame(data={'key': ['A', 'A', 'B', 'B'],
                        'data1': np.random.randint(0, 10, 4),
                        'data2': np.random.randint(0, 10, 4)})
print(df, '\n')

g = df.groupby('key')
print(g, '\n')

# GroupBy 객체에 inspect_input 함수를 agg/apply/transform으로 적용
# g.agg(inspect_input)
# g.apply(inspect_input)
# g.transform(inspect_input)


# agg/apply/transform에서 사용되는 함수의 리턴 타입 비교
def scalar_output(x):
    return 1  # scalar를 리턴


result = g.agg(scalar_output)
print(result, '\n')  # (2, 2) shape

result = g.apply(scalar_output)
print(result, '\n')  # (2, 1) shape - Series

result = g.transform(scalar_output)
print(result, '\n')  # (4, 2) shape


def same_length_output(x):
    return x * 2


print(same_length_output(2))  # scalar -> scalar
print(same_length_output([0, 1, 2]))  # list -> 길이가 2배가 된 list
print(same_length_output(np.arange(3)))  # ndarray -> 같은 길이의 ndarray
print(same_length_output(pd.DataFrame(np.arange(4).reshape(2, 2))))
# DataFrame -> DataFrame

print()
# result = g.agg(same_length_output)  # ValueError 발생
# agg의 목적: GroupBy된 객체의 데이터들을 집계(평균, 표준편차, 최댓값, ...)

result = g.apply(same_length_output)
print(result, '\n')

result = g.transform(same_length_output)
print(result, '\n')

# 평균(mean) 함수를 agg, apply, transform
print(g.agg('mean'), '\n')
# print(g.apply('mean'), '\n')
print(g.transform('mean'), '\n')


def diff_cols(x):
    return x['data1'] - x['data2']


# g.agg(diff_cols)
# g.transform(diff_cols)
print(g.apply(diff_cols), '\n')
