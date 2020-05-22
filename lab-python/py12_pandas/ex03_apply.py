# groupby: split-apply-combine

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# 성별 tip의 평균, 표준편차
grouped_by_sex = tips.groupby('sex')
avg1 = grouped_by_sex['tip'].mean()
print(avg1)
std1 = grouped_by_sex['tip'].std()
print(std1)

# groupby된 객체에서 선택한 컬럼(들)에 함수 여러개를 적용
avg_std = grouped_by_sex['tip'].agg(['mean', 'std'])  # aggregate
print(avg_std)


def max_min(x):
    return x.max() - x.min()


print('tip max:', tips['tip'].max())  # tip 컬럼의 최댓값
print('tip min:', tips['tip'].min())  # tip 컬럼의 최솟값
print(max_min(tips['tip']))

print(grouped_by_sex['tip'].agg(['max', 'min', max_min]))

# 성별 total_bill, tip의 평균, 표준편차, max_min 차이를 계산
result = grouped_by_sex[['total_bill', 'tip']].agg(['mean', 'std', max_min])
print(result)
print(result.stack())

# groupby된 객체에서 컬럼(변수)별로 서로 다른 함수를 적용
# 성별로 groupby된 객체에서 total_bill 컬럼의 평균, tip 컬럼의 최댓값
print(grouped_by_sex['total_bill'].mean())
print(grouped_by_sex['tip'].max())

# aggregate({컬럼이름: 적용할 함수, ...})
print(grouped_by_sex.agg({'total_bill': 'mean', 'tip': 'max'}))

# time별 total_bill의 평균, 표준편차와
# time별 tip의 최댓값, 최솟값, 중위값을 찾아서 출력
grouped = tips.groupby('time')
print(grouped['total_bill'].agg(['mean', 'std']))
print(grouped['tip'].agg(['max', 'min', 'median']))

result = grouped.agg({'total_bill': ['mean', 'std'],
                      'tip': ['max', 'min', 'median']})
print(result)

# 요일별, 시간별 total_bill의 최댓값, 최솟값,
# 요일별, 시간별 tip의 평균, 표준편차,
# 요일별, 시간별 size(인원수)의 합계
grouped = tips.groupby(['day', 'time'])
result = grouped.agg({'total_bill': [np.max, np.min],
                      'tip': [np.mean, np.std],
                      'size': np.sum})
print(result)

# groupby 객체를 index없이 만들고 싶을 때
# (groupby의 기준을 index가 아니라 컬럼으로 만들고 싶을 때)
result = tips.groupby(by='sex', as_index=False).tip.mean()
print(result)

result = tips.groupby(by=['sex', 'smoker'], as_index=False).tip.mean()
print(result)
