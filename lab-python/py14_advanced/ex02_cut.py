import numpy as np
import pandas as pd

np.random.seed(1)

df = pd.DataFrame(data={'age': np.random.randint(0, 100, 20)})
print(df)

# df에 0 <= age < 10, 10 <= age < 20, ... 구간 정보를 컬럼으로 추가
# cut() 함수: 연속형 변수에서 카테고리 변수를 만듦.
# labels: 'age0', ... 'age90' 10개의 원소를 갖는 리스트
labels = [f'age{x}' for x in range(0, 100, 10)]
print(labels)
df['age_range'] = pd.cut(df['age'], bins=range(0, 105, 10),
                         right=False,
                         labels=labels)
print(df)
df.info()

print()
# 난수 20개를 갖는 컬럼 value 하나만 갖는 데이터 프레임
df = pd.DataFrame(data={'value': np.random.randn(20)})
print(df)

# value 컬럼의 최솟값, 최댓값, 4분위값들
print(df['value'].describe())
# 4분위값을 이용한 cut
bins = [-2.07, -0.73, -0.15, 0.66, 1.47]
labels = ['Q1', 'Q2', 'Q3', 'Q4']
df['group'] = pd.cut(df['value'], bins=bins, labels=labels, right=True)
print(df)

# qcut(): quartile cut
bins = pd.qcut(df['value'], 4)
print(bins)  # Category

bins = pd.qcut(df['value'], 10)
print(bins)

