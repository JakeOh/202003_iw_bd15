# DataFrame을 CSV 파일 저장

import pandas as pd

df = pd.read_csv('../examples/ex5.csv', index_col='something')
print(df)
print(df.dtypes)
# NA(missing value)를 처리하기 위해서 숫자 타입이 float 타입이 됨!

# ./: 현재 폴더(current working directory) - 생략 가능
# ../: 상위 폴더
df.to_csv('./ex5_out.csv')

# 인덱스를 제외하고 파일에 씀
df.to_csv('ex5_out2.csv', index=False)

# 컬럼 이름들(헤더 정보)을 제외하고 파일 씀
df.to_csv('ex5_out3.csv', header=False)

# 헤더 정보를 다른 값들로 바꿀 때
df.to_csv('ex5_out4.csv', index=False,
          header=['A', 'B', 'C', 'D', 'MSG'])

# DataFrame에서 일부 컬럼들만 선택해서 csv 파일에 씀.
df.to_csv('ex5_out5.csv', index=False,
          columns=['a', 'b'])
