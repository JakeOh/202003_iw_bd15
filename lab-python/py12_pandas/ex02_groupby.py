import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# 성별(sex)로 group
grouped_by_sex = tips.groupby('sex')

# 그룹에 describe() 메서드를 적용
print(grouped_by_sex.describe())  # 수치형 데이터들의 요약 통계량
print(grouped_by_sex.describe().stack())

# 그룹에서 total_bill 컬럼에만 describe()를 적용
print(grouped_by_sex['total_bill'].describe())
print(grouped_by_sex['total_bill'].describe().stack())

# 두 개 이상의 컬럼으로 그룹을 만드는 방법
# 성별(sex), 시간별(time) tip의 평균
grouped_by_sex_time = tips.groupby(['sex', 'time'])
print(grouped_by_sex_time['tip'].mean())
print(grouped_by_sex_time['tip'].mean().unstack())
# 막대 그래프
sns.barplot(x='sex', y='tip', hue='time', data=tips)
plt.show()

# 성별(sex), 흡연/비흡연 여부(smoker)별 그룹에서 total_bill, tip의 평균
grouped_by_sex_smoker = tips.groupby(['sex', 'smoker'])
means = grouped_by_sex_smoker[['total_bill', 'tip']].mean()
print(means)

sns.barplot(x='sex', y='total_bill', hue='smoker', data=tips)
plt.show()

sns.barplot(x='sex', y='tip', hue='smoker', data=tips)
plt.show()

fig, axes = plt.subplots(nrows=2, ncols=1)
print(axes)
sns.barplot(x='sex', y='total_bill', hue='smoker', data=tips,
            ax=axes[0])
sns.barplot(x='sex', y='tip', hue='smoker', data=tips,
            ax=axes[1])
plt.show()
