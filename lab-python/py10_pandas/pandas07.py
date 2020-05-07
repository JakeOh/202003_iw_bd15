import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# DataFrame
tips = sns.load_dataset('tips')
print(tips)

# Category 변수들의 도수(frequency)
sex_counts = tips['sex'].value_counts()
print(sex_counts)
print(type(sex_counts))  # pandas.Series 객체
print(sex_counts.index)  # index 속성
print(sex_counts['Male'], sex_counts['Female'])

smoker_counts = tips['smoker'].value_counts()
print(smoker_counts)

day_counts = tips['day'].value_counts()
print(day_counts)

time_counts = tips['time'].value_counts()
print(time_counts)

fig, ax = plt.subplots(nrows=2, ncols=2)
print(fig)
print(ax)  # 2-d list

ax[0][0].bar(x=sex_counts.index, height=sex_counts, width=0.3,
             color=['blue', 'red'])
ax[0][0].set_title('Sex')

ax[0][1].bar(x=smoker_counts.index, height=smoker_counts)
ax[0][1].set_title('Smoker')

ax[1][0].barh(y=day_counts.index, width=day_counts)
ax[1][0].set_title('Day')

ax[1][1].barh(y=time_counts.index, width=time_counts)
ax[1][1].set_title('Time')

plt.show()

# seaborn 패키지를 사용해서 subplot에 그래프 그리기
fig, ax = plt.subplots(nrows=2, ncols=2)

sns.countplot(x='sex', data=tips, ax=ax[0][0])
sns.countplot(x='smoker', data=tips, ax=ax[0][1])
sns.countplot(y='day', data=tips, ax=ax[1][0])
sns.countplot(y='time', data=tips, ax=ax[1][1])

plt.show()

# 요일별, 성별 도수(frequency) 막대 그래프
# x=요일, y=frequency, 막대색깔=성별
sns.countplot(x='day', hue='sex', data=tips)
plt.show()

# 요일별 남성 도수 - 남성들로만 이루어진 부분집합에서 요일의 도수
day_male_counts = tips[tips['sex'] == 'Male']['day'].value_counts()
print(day_male_counts)

# 요일별 여성 도수 - 여성들로만 이루어진 부분집합에서 요일의 도수
day_female_counts = tips[tips['sex'] == 'Female']['day'].value_counts()
print(day_female_counts)

df = pd.DataFrame(data={'Male': day_male_counts,
                        'Female': day_female_counts})
print(df)
print(df.index)

x = np.arange(len(df.index))
print(x)
w = 0.3

plt.bar(x=(x - w/2), height=df['Male'], width=w, label='Male')
plt.bar(x=(x + w/2), height=df['Female'], width=w, label='Female')

plt.xticks(ticks=x, labels=df.index)
plt.legend()

# pyplot 그래프를 파일(이미지, pdf)로 저장 - pyplot.show() 호출 전에
# plt.savefig('day_sex.png')
plt.savefig('day_sex.pdf')

plt.show()
