import pandas as pd

# Date 컬럼을 datetime 타입으로 분석해서 DataFrame을 생성
tesla = pd.read_csv('tesla_stock_quandl.csv', parse_dates=['Date'])
# head 정보 출력
print(tesla.iloc[:5])  # tesla.head()
# DataFrame info
tesla.info()

# Date 컬럼의 최솟값/최댓값
print('min:', tesla['Date'].min())
print('max:', tesla['Date'].max())

# tesla 데이터 프레임에서 2010년 데이터만 선택 출력
tesla2010 = tesla[tesla['Date'].dt.year == 2010]
print(tesla2010)

# tesla 데이터 프레임에서 2010년 6월 데이터만 선택 출력
tesla201006 = tesla[(tesla['Date'].dt.year == 2010) &
                    (tesla['Date'].dt.month == 6)]
print(tesla201006)

# datetime 타입의 데이터(Date 컬럼)를 인덱스로 만들면,
# 시간으로 데이터를 선택하는 것이 편리해짐.
tesla.index = tesla['Date']
# Date 컬럼은 원본대로 남아 있고, 인덱스에 Date 값들로 수정.
print(tesla.iloc[:5])

# tesla = tesla.set_index('Date')
# Date 컬럼이 없어지고, 인덱스가 Date가 됨.

# 2010년 데이터
print(tesla.loc['2010'])

# 2010년 6월 데이터
print(tesla.loc['2010-06'])

# 2010 ~ 2011년까지 데이터 선택
print(tesla.loc['2011':'2010'])

# 2011년 4분기
print(tesla.loc['2011-12-31':'2011-10-01'])




