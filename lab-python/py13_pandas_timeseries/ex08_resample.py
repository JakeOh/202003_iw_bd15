import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(data={'data1': np.arange(1000)},
                  index=pd.date_range(start='2020/5/1', periods=1000))
print(df)

# 연도별 data1의 평균
df_2020 = df.loc['2020']
print(df_2020)
print(df_2020['data1'].mean())

df2 = df.reset_index()  # 인덱스를 컬럼으로 만듦.
print(df2)
df2['year'] = df2['index'].dt.year
print(df2)
print(df2.groupby('year').mean())

df2['month'] = df2['index'].dt.month
print(df2)
print(df2.groupby(['year', 'month']).mean())

print()
print('-' * 30)
print(df)

resampler = df.resample('Y')
print(resampler)
print(resampler.mean())  # 연도별 평균

# 월별 평균
print(df.resample('BM').mean())

# banklist.csv 파일을 읽어서 DataFrame 생성
# -> 월별 파산 은행 숫자를 resmaple을 사용해서 찾아보세요.
banks = pd.read_csv('banklist.csv',
                    parse_dates=['Closing Date', 'Updated Date'])
banks.info()

banks_wti = banks.set_index('Closing Date')
by_month = banks_wti.resample('M').size()
print(by_month.sort_values(ascending=False)[:10])
by_month.plot()
plt.show()

# resample 메서드를 이용해서 분기별 파산한 은행의 숫자를 찾아보세요.
# kind='timestamp', 'period'
by_quarter = banks_wti.resample('Q', kind='period').size()
print(by_quarter)
by_quarter.plot()
plt.show()
