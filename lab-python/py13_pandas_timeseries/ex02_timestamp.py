from datetime import datetime
# datetime 패키지(디렉토리/폴더)에서 datetime 모듈(파이썬 파일)을 임포트.

import pandas as pd

# timestamp(unix time, POSIX time, epoch time, ...):
# 1970/01/01 00:00:00를 0으로 시작해서 1초마다 1씩 증가하는 숫자

# 현재 날짜/시간
now = datetime.now()
print(now)

# datetime 객체를 timestamp(숫자)로 변환: timestmap() 메서드
ts = now.timestamp()
print(ts, type(ts))

# timestamp 숫자를 datetime 객체로 변환: fromtimestamp() 함수
dt = datetime.fromtimestamp(1590115800)
print(dt, type(dt))

print(datetime.fromtimestamp(0))
# UTC(Coordinated Universal Time):
# UTC+0: 영국 그리니치 천문대 시간
# UTC+9: KST(Korea Strandard Timezon)

# movielens/ratings.dat 파일을 읽어서 DataFrame을 생성
# ratings DF에서 timestamp 컬럼을 datetime 형식으로 변환한 컬럼을 추가
# head(), tail() 등으로 확인

path = '../datasets/movielens/ratings.dat'
rating_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv(path, sep='::', engine='python',
                      header=None, names=rating_cols)
print(ratings.iloc[:5])

for ts in ratings.loc[:4, 'timestamp']:
    print(ts, datetime.fromtimestamp(ts))

for ts in ratings.iloc[-5:, 3]:
    print(ts, datetime.fromtimestamp(ts))

dts = [datetime.fromtimestamp(ts) for ts in ratings['timestamp']]
ratings['dt'] = pd.Series(dts)
print(ratings.iloc[:5])
print(ratings.iloc[-5:])

print(ratings['dt'].min(), ratings['dt'].max())

dt1 = ratings.iloc[0, 4]  # datetime 객체
# datetime 객체에서 년/월/일/시/분/초 정보를 얻는 방법:
print(dt1)  # 2001-01-01 07:12:40
print(dt1.year, dt1.month, dt1.day)
print(dt1.hour, dt1.minute, dt1.second)

# ratings 데이터 프레임에서 2000년 4월 데이터만 선택, 출력
ratings_200004 = ratings[(ratings['dt'].dt.year == 2000) &
                         (ratings['dt'].dt.month == 4)]
print(ratings_200004)

