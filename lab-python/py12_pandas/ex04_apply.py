# aggregate, apply 차이점

import numpy as np
import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')
print(tips.head())


# median_mean_diff 함수: Series의 중위값과 평균의 차이를 리턴
def median_mean_diff(s):
    return s.median() - s.mean()


print(tips.describe())
print(median_mean_diff(tips['total_bill']),
      median_mean_diff(tips.tip),
      median_mean_diff(tips['size']))

# sex, smoker별 total_bill, tip의 median, mean, median_mean_diff를 계산
grouped = tips.groupby(['sex', 'smoker'])
result = grouped[['total_bill', 'tip']].\
    agg([np.median, np.mean, median_mean_diff])
print(result)
print(result.stack())


# 함수 top: DataFrame과 컬럼 이름을 argument로 전달받아서,
# 컬럼 값들 기준으로 DataFrame을 내림차순 정렬하고, 상위 5개 데이터를 리턴
def top(df, column, n=5):
    return df.sort_values(by=column, ascending=False)[:n]


print(top(tips, 'total_bill', n=5))
print(top(tips, column='tip', n=6))

# time별 total_bill의 상위 5개 row를 출력
grouped = tips.groupby('time')
result = grouped.apply(top, column='total_bill')
print(result)

result = grouped['total_bill'].apply(median_mean_diff)
print(result)

result = grouped['total_bill'].agg(median_mean_diff)
print(result)

result = grouped.apply(median_mean_diff)
print(result)

result = grouped.agg(median_mean_diff)
print(result)

# result = grouped.agg(top, column='total_bill')
result = grouped.apply(top, column='total_bill')
print(result)

# agg: 컬럼 별로 함수를 적용할 때
# apply: 데이터 프레임에 함수를 적용할 때
