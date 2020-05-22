# ../datasets/babynames/yob2010.txt 파일을 읽어서 DF 생성
# 성별 출생자 숫자를 계산

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

col_names = ['name', 'gender', 'births']
path = '../datasets/babynames/yob2010.txt'
df = pd.read_csv(path, header=None, names=col_names)
print(df.iloc[:5])
print(df.iloc[-5:])
print(df.groupby('gender')['births'].sum())

# ../datasets/babynames/ 폴더 안에 있는 모든 txt을 읽어서 DF을 생성(131개)
# 각 DF에 year 컬럼을 추가
# 모든 DF을 하나의 DF으로 합치기
# 성별, 연도별 출생자 숫자

names_year = []
years = np.arange(1880, 2011)
for year in years:
    path = f'../datasets/babynames/yob{year}.txt'
    df = pd.read_csv(path, header=None, names=col_names)
    df['year'] = year
    names_year.append(df)
# print(names_year[130])

names_df = pd.concat(names_year)
print(names_df)

result = names_df.groupby(['gender', 'year'])['births'].sum()
print(result)

# result의 shape을 바꿈 - 성별을 컬럼으로 만듦.
reshaped = result.unstack(level=0)
print(reshaped)

reshaped = reshaped.reset_index()
print(reshaped)

sns.lineplot(x='year', y='F', data=reshaped, label='Female')
sns.lineplot(x='year', y='M', data=reshaped, label='Male')
plt.legend()
plt.ylabel('births')
plt.show()

# pivot_table 메서드
ptable = names_df.pivot_table(values='births',
                              index='year',
                              columns='gender',
                              aggfunc='sum')
print(ptable)

# pivot_table을 사용해서
# tips 데이터 프레임에서 시간별, 요일별 tip의 평균
tips = sns.load_dataset('tips')
tip_by_time_day = tips.pivot_table(values='tip',
                                   index='time',
                                   columns='day',
                                   aggfunc='mean')
print(tip_by_time_day)

df = tips.pivot_table(values='tip',
                      index=['day', 'time'],
                      columns=['sex', 'smoker'])  # aggfunc='mean'
print(df)
