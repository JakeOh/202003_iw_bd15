import pandas as pd

# pandas: Series(1차원), DataFrame(2차원)을 쉽게 다룰 수 있는 패키지

s = pd.Series([1, 3, -5, 9])
print(s)
print(s.index)
print(s.values)

# Series의 원소 접근: index를 사용
print(s[2])
print(s[:3])  # 범위 연산자
print(s[-2:])
print(s > 0)
print(s[s > 0])  # boolean indexing

print(s.loc[2])  # label-base location
print(s.iloc[2])  # integer-base location
print(s.loc[0:3])  # 0 <= loc <= 3
print(s.iloc[0:3])  # 0 <= loc < 3
# iloc는 음수 인덱스가 가능. loc는 음수 인덱스 불가능.
print(s.iloc[-1])
# print(s.loc[-1])  # KeyError

s2 = pd.Series([1, 3, -5, 9],
               index=['a', 'd', 'c', 'b'])
print(s2)
print(s2.loc['a':'d'])
print(s2.iloc[0:2])
print(s2['a'], s[0])

# pd.Series 객체는 index와 values를 속성으로 갖는 데이터 타입.
# pd.Series는 Python의 list 보다는 dict와 더 비슷한 타입.
city_pop = {'서울': 10_000_000, '경기': 1_000_000, '제주': 10_500_000}
s3 = pd.Series(city_pop)
print(s3)
print(s3.loc[['서울', '제주', '경기']])
print(s3.sort_index())  # index의 오름차순으로 정렬: 경기 < 서울 < 제주
print(s3.sort_values(ascending=False))  # values의 내림차순으로 정렬
print(s3.argmax())  # integer-base index를 리턴함.
