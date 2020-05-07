import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# mile per gallon(자동차 연비)
mpg = sns.load_dataset('mpg')
print(mpg.iloc[:5])  # mpg.head()

# row x column
print('shape:', mpg.shape)

# column(변수) 이름들
print(mpg.columns)

# DataFrame의 요약 통계 정보(summary statistics/descriptive statistics)
print(mpg.describe())  # 수치형 변수들에 대한 요약 통계량
print(mpg['origin'].describe())  # object 변수에 대한 도수, 유일값, 최빈값, ...
print(mpg['origin'].value_counts())  # 카테고리 변수 도수(frequency)

# mpg ~ displacement 산점도 그래프(scatter plot)
plt.scatter(x=mpg['displacement'], y=mpg['mpg'])
plt.xlabel('displacement')
plt.ylabel('mpg')
plt.title('MPG vs Displacement')
plt.show()

sns.scatterplot(data=mpg, x='displacement', y='mpg')
plt.show()

sns.regplot(data=mpg, x='displacement', y='mpg')
plt.show()

# 2x2 Subplots에 mpg ~ cylinders, mpg ~ horsepower,
# mpg ~ weight, mpg ~ acceleration scatter plot
fig, ax = plt.subplots(nrows=2, ncols=2, sharey=True)
ax[0][0].scatter(x=mpg['cylinders'], y=mpg['mpg'])
ax[0][0].set_xlabel('cylinders')
ax[0][0].set_ylabel('mpg')
ax[0][1].scatter(x=mpg['horsepower'], y=mpg['mpg'])
ax[0][1].set_xlabel('horsepower')
# ax[0][1].set_ylabel('mpg')

sns.scatterplot(data=mpg, x='weight', y='mpg', ax=ax[1][0])
sns.scatterplot(data=mpg, x='acceleration', y='mpg', ax=ax[1][1])

plt.subplots_adjust(wspace=0)
plt.show()

# cylinder별 mpg의 평균 막대 그래프(bar plot)
sns.barplot(data=mpg, x='cylinders', y='mpg')
plt.show()

mean_cly8 = mpg[mpg['cylinders'] == 8]['mpg'].mean()
print(mean_cly8)

# 1) pandas.Series.unique() 메서드를 사용해서 cylinders의 중복되지 않는 값을 찾으세요.
cylinders = mpg['cylinders'].unique()
print(cylinders, type(cylinders))
cylinders.sort()
print(cylinders)

# 2) cylinder별 평균 연비를 저장할 빈 리스트를 생성하세요.
# mpg_mean = []

# 3) 1에서 찾은 cylinder들에 대해서 반복하면서,
# 해당 cylinder의 mpg 평균을 계산해서 리스트에 append하세요.
# for cyl in cylinders:
#     mpg_mean.append(mpg[mpg['cylinders'] == cyl]['mpg'].mean())
# print(mpg_mean)
mpg_mean = [mpg[mpg['cylinders'] == cyl]['mpg'].mean()
            for cyl in cylinders]
print(mpg_mean)

# 4) cylinders를 인덱스로 하고, 평균 연비를 데이터로 하는 Series를 생성하세요.
s = pd.Series(data=mpg_mean, index=cylinders)
print(s)

# 5) 4에서 생성한 Series로 pyplot.bar() 함수를 사용해서 bar plot을 그리세요.
plt.bar(x=s.index, height=s)
plt.show()

# pandas.Series.plot.xyz()
s.plot.bar()
plt.show()

# pandas.DataFrame.plot.xyz()
mpg.plot.scatter(x='displacement', y='mpg')
plt.show()
