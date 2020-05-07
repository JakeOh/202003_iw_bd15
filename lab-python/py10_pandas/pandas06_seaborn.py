import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
print(tips.iloc[:5])  # tips.head()

# 히스토그램: 연속형 변수를 일정한 크기의 구간으로 나눠서
# 그 구간 안에 포함된 개수를 막대 그래프로 그림.
# seaborn.distplot(): distribution plot
sns.distplot(tips['total_bill'], bins=10, kde=False)
plt.show()

# 막대 그래프: 범주형 변수(categorical variable)의 빈도수를 막대로 그림.
# seaborn.countplot(): count plot
# sns.countplot(x='sex', data=tips)  # 세로 막대 그래프
sns.countplot(y='sex', data=tips)  # 가로 막대 그래프
plt.show()

# size 변수의 세로 막대 그래프
sns.countplot(x='size', data=tips)
plt.show()
# matplotlib.pyplot.bar() 함수

# 산점도 그래프(scatter plot): 두 변수의 상관 관계
# seaborn.regplot(): regression plot
# tip ~ total_bill
sns.regplot(x='total_bill', y='tip', data=tips, fit_reg=False)
# fit_reg: 회귀 직선을 그릴지 말지를 결정. 기본값은 True.
plt.show()

# seaborn.jointplot():
# 두 변수의 상관관계를 보여주는 scatter plot과 함께
# 각 변수들의 히스토그램을 표현한 그래프.
sns.jointplot(x='total_bill', y='tip', data=tips)
plt.show()

# box plot: 요약 통계량을 보여주는 그래프
sns.boxplot(y='total_bill', data=tips)
# sns.boxplot(x='total_bill', data=tips)
plt.show()

# 성별 tip의 box plot
sns.boxplot(x='sex', y='tip', data=tips)
plt.show()

# 요일별 tip의 box plot
sns.boxplot(x='day', y='tip', data=tips)
plt.show()

# 막대 그래프(bar plot)
# 성별 total_bill의 평균
print(tips[tips['sex'] == 'Male']['total_bill'].mean())
print(tips[tips['sex'] == 'Female']['total_bill'].mean())

sns.barplot(x='sex', y='total_bill', data=tips)
plt.show()

# 요일별 tip의 평균을 가로 막대 그래프
print(tips[tips['day'] == 'Sun']['tip'].mean())

sns.barplot(x='tip', y='day', data=tips)
plt.show()

# tip_pct = tip / total_bill 컬럼을 추가
tips['tip_pct'] = tips['tip'] / tips['total_bill']
print(tips.iloc[:5])

# 성별 tip_pct의 평균 막대 그래프
sns.barplot(x='tip_pct', y='sex', data=tips)
plt.show()

# 요일별 tip_pct의 평균 막대 그래프
sns.barplot(x='tip_pct', y='day', data=tips)
plt.show()

# 요일별, 성별 tip_pct의 평균 막대 그래프
sns.barplot(x='day', y='tip_pct', data=tips,
            hue='sex')
plt.show()

# seaborn.catplot(): category plot
# 카테고리 별로 그래프를 분리해서 그림.
sns.catplot(x='day', y='tip_pct', data=tips,
            col='sex', kind='bar')
plt.show()

# 요일별 tip_pct의 평균 막대 그래프를 time별로 분리해서 그림.
sns.catplot(x='day', y='tip_pct', data=tips,
            row='time', kind='bar')
plt.show()

# 요일별 tip_pct의 평균 막대 그래프를 sex별, time별로 분리해서 그림.
sns.catplot(x='day', y='tip_pct', data=tips,
            row='time', col='sex', kind='bar')
plt.show()
