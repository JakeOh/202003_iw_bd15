# 파일(csv, txt, xlx, ...)에서 데이터 읽기 -> DataFrame 생성

import pandas as pd

# ../examples/ex1.csv 파일을 읽어서 DataFrame을 생성
# 헤더 정보(컬럼 이름들)이 파일의 첫번째 줄에 있는 경우
df = pd.read_csv('../examples/ex1.csv')
print(df)
print('shape:', df.shape)
print('index:', df.index)
print('columns:', df.columns)
print(df['a'])  # DataFrame에서 컬럼 선택
# pd.read_csv()는 타입 추론 기능이 있음. (데이터 타입을 자동으로 맞춤.)
print(df['message'])  # dtype: object -> 문자열

# DataFrame의 데이터 타입 변환(type casting)
df['a'] = df['a'].astype('int16')
print(df['a'])

# ../exmples/ex2.csv 파일: 헤더 정보(컬럼 이름들)이 없음.
df = pd.read_csv('../examples/ex2.csv', header=None)
print(df)

col_names = ['a', 'b', 'c', 'd', 'msg']
df = pd.read_csv('../examples/ex2.csv',
                 header=None, names=col_names)
print(df)

# csv 파일의 특정 컬럼을 index(row label)로 사용
df = pd.read_csv('../examples/ex2.csv',
                 header=None, names=col_names, index_col='msg')
print(df)
print('shape:', df.shape)
print('index:', df.index)

# ../examples/ex3.csv 파일: 공백으로 구분. 컬럼이름과 인덱스가 같이 있음.
# 구분자(separator)가 공백인데, 공백이 하나일 수도 있고, 여러개 있을 수도 있음.
# -> sep 옵션(argument)을 정규 표현식(regular expression)으로 작성.
# 헤더의 개수와 본문의 데이터 개수가 다르면, 인덱스를 자동으로 찾음.
df = pd.read_csv('../examples/ex3.csv', sep=r'\s+')
print(df)

# txt 파일이 csv와 같은 (또는 비슷한) 구조이면, read_csv를 사용하면 됨.
df = pd.read_csv('../examples/ex3.txt', sep=r'\s+')
print(df)

# pd.read_table() 함수는 read_csv()와 동일한 기능을 가지고 있음.
# 다른 점은 default separator가 '\t'(탭).

# ../examples/ex4.csv 파일:
# 데이터와 데이터가 아닌 주석(#으로 시작하는 줄)이 포함된 파일
# 특정 라인 번호를 생략하고 데이터를 읽을 때, skiprows 사용
df = pd.read_csv('../examples/ex4.csv', skiprows=(0, 2, 3))
print(df)

df = pd.read_csv('../examples/ex4.csv',
                 skiprows=(0, 2, 3), index_col='message')
print(df)

# ../examples/ex5.csv 파일: NA(Not Available)가 포함(NA 문자열, 빈문자열)
# read_csv() 함수는 빈 문자열과 'NA'를 자동으로 결측치(Missing Value) 처리를 함.
df = pd.read_csv('../examples/ex5.csv')
print(df)
print(df['message'].value_counts())

df = pd.read_csv('../examples/ex5_null.csv')
print(df)
print(df['message'].value_counts())

# 'NA' 이외의 다른 문자열들(예: Null, None 등)을 결측치 처리하고 싶을 때
df = pd.read_csv('../examples/ex5_null.csv',
                 na_values=['Null', 'None'])
print(df)

# 컬럼 별로 Missing Value 처리할 문자열을 다르게 지정할 때
df = pd.read_csv('../examples/ex5_null.csv',
                 na_values={'c': ['Null', 'None']})
print(df)
print(df.dtypes)

# row가 많은 CSV 파일 읽을 때
df = pd.read_csv('../examples/ex6.csv')
print('shape:', df.shape)
print(df.iloc[-5:])  # df.tail()

# CSV 파일에서 몇개의 row만 읽을 때
df = pd.read_csv('../examples/ex6.csv', nrows=10)
print(df)

# 파일을 조각조각 잘라서 반복적으로 읽을 때
chunk = pd.read_csv('../examples/ex6.csv', chunksize=1000)
print('chunk:', chunk)
# read_csv() 함수에서 chunksize를 지정하면, TextFileReader 객체를 반환함.
# TextFileReader 객체를 for-in 구문에서 사용하면,
# 파일에서 chunksize만큼씩 라인을 읽어서 DataFrame을 생성해줌.
for piece in chunk:
    print('piece shape:', piece.shape)


# ../examples/ex7.csv 파일: 모든 값들이 ""로 감싸져 있음.
df = pd.read_csv('../examples/ex7.csv')
print(df)
print(df.dtypes)

df = pd.read_csv('../examples/ex7_test.csv')
print(df)

