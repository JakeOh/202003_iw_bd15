# 시계열(Time Series) 데이터: 주식, 환율, 물가, 실업률, ...

from datetime import datetime
# Python 기본 모듈 datetime, 클래스 datetime

# import dateutil  # dateutil 패키지를 import
from dateutil import parser  # dateutil 패키지에서 parser 모듈을 import

now = datetime.now()  # OS의 시간대(time zone)에서의 현재 시간
print(now, type(now))

date1 = datetime(2020, 6, 21)  # 특정 날짜와 시간으로 datetime을 생성
print(date1, type(date1))

date2 = datetime(2020, 5, 21)

# datetime 클래스는 -과 같은 연산자들이 정의되어 있음.
date_diff = date1 - date2
print(date_diff, type(date_diff))  # timedelta 클래스

# 문자열을 datetime 객체로 변환: datetime.strptime()
date_string = '2020/05/21'  # 문자열(str 클래스 객체)
date_obj = datetime.strptime(date_string, '%Y/%m/%d')
print(date_obj, type(date_obj))

# datetime 객체를 문자열로 변환: datetime.strftime()
date_string = date_obj.strftime('%y-%m-%d')
print(date_string)
date_string2 = date_obj.strftime('%m/%d/%Y')
print(date_string2)
date_string3 = date_obj.strftime('%d/%m/%Y')
print(date_string3)

# 문자열 형식(format)은 다양하기 때문에(년/월/일, 월/일/년, 일/월/년, ...)
# 문자열을 datetime 객체로 변환할 때마다 format을 맞춰줘야 함.
# datetime.strptime() 함수를 사용할 때는 format을 잘 맞춰줘야 함.
print(datetime.strptime(date_string, '%y-%m-%d'))

# 문자열의 날짜/시간 포맷을 유추해서 datetime 객체로 변환하는 패키지: dateutil
print(date_string, parser.parse(date_string))
print(date_string, parser.parse(date_string, yearfirst=True))
print(date_string2, parser.parse(date_string2))
print(date_string3, parser.parse(date_string3))
