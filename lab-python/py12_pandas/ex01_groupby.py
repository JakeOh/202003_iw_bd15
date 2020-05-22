import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# seaborn 패키지에 포함된 tips DataFrame을 로드
tips = sns.load_dataset('tips')
print(tips.iloc[:5])
tips.info()
print(tips.describe())

# 흡연/비흡연 그룹별 tip의 평균을 계산, 막대 그래프
sns.barplot(x='smoker', y='tip', data=tips)
plt.show()

# 흡연자 subset
smoker = tips[tips['smoker'] == 'Yes']
print(smoker)
# 비흡연자 subset
non_smoker = tips[tips['smoker'] == 'No']
print(non_smoker)
# smoker에서 tip의 평균
tip_smoker = smoker['tip'].mean()
print('smoker tip mean:', tip_smoker)
# non_smoker에서 tip의 평균
tip_non_smoker = non_smoker['tip'].mean()
print('non_smoker tip mean:', tip_non_smoker)

tip_mean = tips['tip'].groupby(by=tips['smoker']).mean()
print(tip_mean)

tip_mean2 = tips.groupby(by='smoker').tip.mean()
print(tip_mean2)

# groupby를 사용해서, time별 total_bill의 평균 계산
total_bill_by_time = tips.groupby('time')['total_bill'].mean()
print(total_bill_by_time)

sns.barplot(x='time', y='total_bill', data=tips)
plt.show()

# GroupBy 객체
grouped = tips.groupby('time')
print(grouped)
for time, subset in grouped:
    print(time)
    print(subset)
