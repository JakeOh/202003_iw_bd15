import pandas as pd
import matplotlib.pyplot as plt

banks = pd.read_csv('banklist.csv')
print(banks.iloc[:5])
banks.info()

# object 타입의 컬럼을 datetime 타입의 컬럼으로 변환
banks['close_date'] = pd.to_datetime(banks['Closing Date'])
banks['update_date'] = pd.to_datetime(banks['Updated Date'])

# banks DataFrame에서 Closing Date, Update Date,
# close_date, update_date 컬럼의 내용을 출력
# print(banks[['Closing Date', 'Updated Date', 'close_date', 'update_date']])
print(banks.iloc[:, -4:])

# csv 파일에서 DF을 생성할 때
# Closing Date, Updated Date 컬럼을 시간 타입으로 생성.
banks2 = pd.read_csv('banklist.csv',
                     parse_dates=['Closing Date', 'Updated Date'])
banks2.info()

# Closing Date의 year 값을 close_year 컬럼으로 만드세요.
banks2['close_year'] = banks2['Closing Date'].dt.year

# Closing Date의 분기 값을 close_quarter 컬럼으로 만드세요.
banks2['close_quarter'] = banks2['Closing Date'].dt.quarter

# 첫 5개 행에서 Closing Date, close_year, close_quarter를 출력
print(banks2.iloc[:5, [5, 7, 8]])

# 마지막 5개 행에서 Closing Date, close_year, close_quarter를 출력
print(banks2.iloc[-5:, [5, 7, 8]])

# 수집된 데이터에서 Closing Date가 가장 빠른/늦은 날짜
print('min closing date:', banks2['Closing Date'].min())
print('max closing date:', banks2['Closing Date'].max())

# 연도별 파산한 은행의 숫자
by_year = banks2.groupby('close_year').size()
print(by_year)
# 파산한 은행 숫자 내림차순으로 정렬 출력
print(by_year.sort_values(ascending=False))

# 연도별, 분기별 파산한 은행의 숫자
by_year_quarter = banks2.pivot_table(index='close_year',
                                     columns='close_quarter',
                                     aggfunc='size')
print(by_year_quarter)

by_year_quarter2 = banks2.groupby(['close_year', 'close_quarter']).size()
print(by_year_quarter2)

# 연도별(/분기별) 파산한 은행 그래프
by_year.plot()
plt.show()

by_year_quarter2.plot()
plt.show()
