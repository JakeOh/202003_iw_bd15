# seaborn 패키지의 iris 데이터 세트를 로드
# species별 모든 컬럼의 평균, 표준편차 출력

import numpy as np
import pandas as pd
import seaborn as sns

iris = sns.load_dataset('iris')
print(iris.head())

grouped = iris.groupby('species')
result = grouped.agg(['mean', 'std'])
print(result)
print(result.stack())

# iris 데이터 프레임에서 품종별 데이터 개수
print(grouped.size())
print(grouped.count())

iris.iloc[[1, 51, 101], [0, 1, 2]] = np.nan
print(iris.iloc[[1, 51, 101], :])

print(iris.groupby('species').size())  # 데이터의 크기(row의 길이)
print(iris.groupby('species').count())  # NA가 아닌 데이터 개수

