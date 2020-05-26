import pandas as pd
import matplotlib.pyplot as plt

# ./country_timeseries.csv 파일 읽어서 DataFrame 생성
ebola = pd.read_csv('country_timeseries.csv', parse_dates=['Date'])
ebola.info()
print(ebola.iloc[:5])
print(ebola.iloc[-5:])
print(ebola.iloc[-5:, :5])
print(ebola.iloc[-5:, -5:])

print('min:', ebola['Date'].min())
print('max:', ebola['Date'].max())

# Datetime 타입으로 인덱스 설정
ebola.index = ebola['Date']
# ebola = ebola.reset_index('Date')
print(ebola.index)
print(ebola.iloc[:5])

# 월별 UnitedStates, Spain의 사망자 수
print(ebola['2014-10']['Deaths_UnitedStates'])
print(ebola.resample('M')[['Deaths_UnitedStates', 'Deaths_Spain']].sum())

# 월별 확진자 수
print(ebola.resample('M')[['Cases_UnitedStates', 'Cases_Spain']].sum())

# Cases_Xyz(확진자 수)로 이루어진 subset을 만듦.
ebola_cases = ebola.iloc[:, 2:10]
ebola_cases.info()
ebola_cases.plot()
plt.show()

# 월별 확진자 수를 찾고, 시각화
by_month = ebola_cases.resample('M').sum()
print(by_month)

by_month.plot()
plt.show()
