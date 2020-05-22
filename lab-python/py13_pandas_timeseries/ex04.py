import pandas as pd

# ../examples/tseries.csv 읽어서 DataFrame 생성
path = '../examples/tseries.csv'

df1 = pd.read_csv(path)
print(df1)
df1.info()  # date 컬럼의 데이터 타입은 object(문자열)

# 문자열 컬럼을 날짜/시간 타입으로 변환해서 새로운 컬럼으로 작성
df1['dt'] = pd.to_datetime(df1['date'])
df1.info()

df2 = pd.read_csv(path, parse_dates=['date'])
print(df2)
df2.info()

