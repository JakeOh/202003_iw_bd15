# gapminder.tsv 파일을 폴더에 복사 - read_csv() 사용해서 DataFrame 생성.
# DataFrame 확인: head, tail, shape, dtypes, 요약 통계량, ...

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gapminder = pd.read_csv('gapminder.tsv', sep='\t')
# tsv(tap-separated values): tab('\t')으로 값들이 구분되어 있는 파일
print(gapminder.iloc[:5])  # head()
print(gapminder.iloc[-5:])  # tail()

print(gapminder.columns)  # 컬럼 이름들
print(gapminder.shape)  # row x column 개수
print(gapminder.describe())  # 요약 통계량
gapminder.info()
# DataFrame 정보(row 개수, 컬럼 이름, 데이터 타입, NN, ...)

# DataFrame에서 특정 컬럼 선택
# country 컬럼만 선택, 출력
print(gapminder['country'])
# country, continent, year 컬럼을 선택, 출력
print(gapminder[['country', 'continent', 'year']])

# DataFrame에서 특정 행(row)을 선택 -> 인덱스
# iloc, loc
# 100 <= index <= 105 데이터 출력
print(gapminder.loc[100:105])
print(gapminder.iloc[100:106])

# 특정 행과 열을 함께 선택 - iloc, loc
# 840 ~ 851 행과 country, year, pop 열을 선택
print(gapminder.loc[840:851, ['country', 'year', 'pop']])
print(gapminder.iloc[840:852, [0, 2, 4]])

# gapminder DF에서 gdpPercap의 최솟값, 최댓값
min_gdp = gapminder['gdpPercap'].min()
max_gdp = gapminder['gdpPercap'].max()
print(min_gdp, max_gdp)

# gdpPercap 최솟값, 최댓값 데이터를 갖는 row를 출력
data = gapminder[(gapminder['gdpPercap'] == min_gdp) |
                 (gapminder['gdpPercap'] == max_gdp)]
print(data)

# lifeExp의 최솟값, 최댓값 - 데이터 출력
min_life = gapminder['lifeExp'].min()
max_life = gapminder['lifeExp'].max()
print(min_life, max_life)

data = gapminder[(gapminder['lifeExp'] == min_life) |
                 (gapminder['lifeExp'] == max_life)]
print(data)

# year 변수(컬럼)의 중복되지 않는 값들을 찾아서 출력
years = gapminder['year'].unique()
print(years)

# country는 모두 몇개의 나라가 있을까요?
countries = gapminder['country'].unique()
print(len(countries))

# year, 평균 lifeExp 두개의 컬럼을 갖는 DataFrame 생성
# mean_lifeExp = []
# for year in years:  # [1952, ..., 2007] 반복
#     subset = gapminder[gapminder['year'] == year]  # 해당 연도의 DF
#     mean = subset['lifeExp'].mean()  # 해당 연도의 lifeExp의 평균
#     mean_lifeExp.append(mean)  # 계산된 평균을 리스트에 추가

mean_lifeExp = [gapminder[gapminder['year'] == year]['lifeExp'].mean()
                for year in years]
print(mean_lifeExp)
df = pd.DataFrame({'year': years, 'life_exp': mean_lifeExp})
print(df)

# 평균 lifeExp ~ year 선 그래프
plt.plot(df['year'], df['life_exp'], marker='o')
plt.xticks(years)
plt.yticks(range(45, 70, 5))
plt.xlabel('year')
plt.ylabel('life_exp')
plt.show()

sns.scatterplot(x='year', y='lifeExp', data=gapminder)
plt.show()

sns.lineplot(x='year', y='lifeExp', data=gapminder,
             err_style='bars', estimator='mean')
plt.show()

# boolean indexing 사용
# country 문자열이 'Korea'를 포함(contain)하는 DataFrame을 만들어서 출력

