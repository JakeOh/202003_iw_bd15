import pandas as pd
import numpy as np

# date_range: 날짜 범위
index = pd.date_range(start='2020/5/1', end='2020/5/31')
print(index)

index2 = pd.to_datetime(['2020/5/1', '2020/5/2', '2020/5/3'])
print(index2)

index3 = pd.date_range(start='2020/5/1', periods=7)
print(index3)

index4 = pd.date_range(end='2020/5/1', periods=7)
print(index4)

index5 = pd.date_range(start='2020/5/25', periods=10, freq='H')
print(index5)
# 교재 p.438 표 11-4 기본 시계열 frequency
# M: Month, D: Day, H: Hour, ...

# BM: 달(month)의 마지막 영업일(business day)
index6 = pd.date_range(start='2020/1/1', periods=20, freq='BM')
print(index6)

# WOM: Week Of Month
index7 = pd.date_range(start='2020/1/1', periods=20, freq='WOM-4FRI')
print(index7)

# normalize=True: 모든 시간 정보를 00:00:00로 만듦.
index8 = pd.date_range(start='2020/1/1 12:34:55', periods=5,
                       normalize=True)
print(index8)

# shift: 데이터 이동
ts = pd.Series(data=np.arange(5),
               index=pd.date_range(start='2020/1/1', periods=5, freq='M'))
print(ts)

print(ts.shift(1))
print(ts.shift(-1))

# 전달 대비 증가/감소 비율
np.random.seed(1)
ts = pd.Series(data=np.random.rand(5),
               index=pd.date_range(start='2020/1/1', periods=5, freq='M'))
print(ts)
print(ts / ts.shift(1))
