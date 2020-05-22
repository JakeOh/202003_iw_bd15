from datetime import datetime

import pandas as pd
import numpy as np

# 문자열 -> datetime 변환
#   datetime.strptime(문자열, 포맷)
#   dateutil.parser.parse(문자열, ...)
# 타임스탬프 -> datetime 변환
#   datetime.fromtimestamp(숫자)

date1 = pd.to_datetime('2020-05-22')
print(date1, type(date1))

date2 = pd.to_datetime('05/22/2020')
print(date2)

date3 = pd.to_datetime('01/03/20', yearfirst=True)
print(date3)
date4 = pd.to_datetime('01-03-20', dayfirst=True)
print(date4)
date5 = pd.to_datetime('01-03-20')
print(date5)

date6 = pd.to_datetime(datetime(2020, 5, 22, 14, 40))
print(date6, type(date6))

ts = datetime.now().timestamp()
print(ts)
date7 = pd.to_datetime(ts, unit='s')  # UTC+0 시간으로 표시
print(date7, type(date7))

# pd.to_datetime() 함수
#   문자열 -> pandas 시간 타입(Timestamp)
#   python datetime 객체 -> pandas 시간 타입
#   숫자(UNIX time, timestamp) -> pandas 시간 타입
#   리스트, 시리즈 -> pandas 시간 타입들을 원소로 갖는 인덱스 객체

dates = ['2020-5-22', datetime(2020, 5, 22, 14, 55, 30), np.nan]
result = pd.to_datetime(dates)
print(result)

ratings = pd.read_csv('../datasets/movielens/ratings.dat',
                      sep='::', engine='python',
                      header=None,
                      names=['uid', 'mid', 'rating', 'timestamp'],
                      nrows=10)
print(ratings)
ratings.info()

ratings['ts'] = pd.to_datetime(ratings['timestamp'], unit='s')
print(ratings)

# ratings2 = pd.read_csv('../datasets/movielens/ratings.dat',
#                        sep='::', engine='python',
#                        header=None,
#                        names=['uid', 'mid', 'rating', 'timestamp'],
#                        nrows=10,
#                        parse_dates=['timestamp'])
# print(ratings2)
# ratings2.info()
