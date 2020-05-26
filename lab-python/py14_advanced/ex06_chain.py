import pandas as pd
import numpy as np

# 1) DataFrame 생성
df = pd.read_csv('../examples/tips.csv')
# print(df)

# 2) size == 2인 부분집합
subset = df[df['size'] == 2]
# print(subset.head())

# 3) smoker 별로 groupby
g = subset.groupby('smoker')
# print(g)

# 4) DataFrameGroupBy에서 tip 컬럼만 선택
g_tip = g['tip']
# print(g_tip)

# 5) size == 2인 부분집합에서 smoker별 tip의 평균
tip_by_smoker = g_tip.mean()
print(tip_by_smoker)

# method chaining/method chain-call(연쇄 호출)
result = pd.read_csv('../examples/tips.csv')\
    [lambda x: x['size'] == 2]\
    .groupby('smoker')['tip'].mean()

print(result)


# pipe 함수: R에서 %>%와 비슷한 기능
def de_mean(df, cols):
    """데이터 프레임 df와 그 데이터 프레임의 컬럼이름들의 리스트 cols를
    argument로 받아서, 해당 컬럼의 값들을 평균이 0이 되도록 변환.
    원본 데이터 프레임 df는 유지, 새로운 데이터 프레임을 생성해서 리턴"""
    result = df.copy()
    for col in cols:
        result[col] = df[col] - df[col].mean()
    return result


# de_mean() 함수 테스트
np.random.seed(1)
df = pd.DataFrame(data={'A': np.random.randint(-10, 10, 5),
                        'B': np.random.randint(0, 10, 5),
                        'C': np.random.randint(0, 10, 5)})
print(df)

result = de_mean(df, ['B', 'C'])
print(result)

# pipe 함수
result = df.pipe(de_mean, cols=['B']).pipe(de_mean, cols=['C'])
print(result)
