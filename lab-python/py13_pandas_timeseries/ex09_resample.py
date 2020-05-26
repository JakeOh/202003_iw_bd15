import pandas as pd

# ../examples/spx.csv 파일을 읽어서 DataFrame을 생성.
# 날짜/시간 정보는 DataFrame의 인덱스로 사용.
# resample() 메서드를 사용해서,
# 연도별 SPX의 평균, 표준편차, 최댓값, 최솟값을 찾아보세요.
# 분기별 SPX의 평균, 표준편차, 최댓값, 최솟값을 찾아보세요.

path = '../examples/spx.csv'
df = pd.read_csv(path,
                 names=['DATE', 'SPX'],  # 컬럼 이름을 재지정
                 header=0,  # 0번 row가 header 정보(컬럼 이름)
                 parse_dates=[0])
print(df.iloc[:5])
# df['DATE'] = pd.to_datetime(df['DATE'])
df.info()

df = df.set_index('DATE')
print(df.iloc[:5])
print(df.index)

print()
df2 = pd.read_csv(path,
                  index_col=0,  # 인덱스로 사용할 컬럼(번호, 이름)
                  parse_dates=True)
print(df2.iloc[:5])
print(df2.index)

resampled = df2.resample('Y', kind='period').\
    agg(['mean', 'std', 'max', 'min'])
print(resampled)
