import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')
print(tips.iloc[:5])

# 성별(sex) 흡연자/비흡연자(smoker) 숫자
cross_tab = pd.crosstab(index=tips['sex'],
                        columns=tips['smoker'])
print(cross_tab)
print(tips['sex'].value_counts())
print(tips['smoker'].value_counts())

cross_tab = pd.crosstab(index=tips['sex'], columns=tips['smoker'],
                        margins=True)
print(cross_tab)

# 성별, 흡연여부별, 요일별 식당을 방문한 사람들의 숫자
# 인덱스(성별, 흡연여부), 컬럼(요일) -> Cross Table
cross_tab = pd.crosstab(index=[tips.sex, tips.smoker],
                        columns=tips.day,
                        margins=True)
print(cross_tab)

# 성별, 흡연여부별, 요일별, 시간별 식당 방문자 숫자
cross_tab = pd.crosstab(index=[tips['sex'], tips['smoker']],
                        columns=[tips['day'], tips['time']],
                        margins=True)
print(cross_tab)





