import numpy as np
import pandas as pd

# NumPy의 concatenate:
# 배열(ndarray)의 축(row 방향, column 방향)을 따라서 데이터를 합치는 것.
arr = np.arange(12).reshape((3, 4))
print(arr)

arr2 = np.arange(12, 24).reshape((3, 4))
print(arr2)

result = np.concatenate((arr, arr2))  # axis=0(기본값)
print(result)

result = np.concatenate((arr, arr2), axis=1)
print(result)

# arr: (3, 4) 배열
arr3 = np.arange(6).reshape((2, 3))  # (2, 3) 배열
# result = np.concatenate((arr, arr3))
# arr과 arr3은 컬럼의 개수(차원)이 다르기 때문에 concatenate를 할 수 없음!

# pandas.Series의 concat
s1 = pd.Series(data=[1, 2], index=['a', 'b'])
print(s1)

s2 = pd.Series(data=[3, 4, 5], index=['c', 'd', 'e'])
print(s2)

result = pd.concat((s1, s2))  # axis=0(기본값)
print(result)  # Series

result = pd.concat((s1, s2), axis=1)
print(result)  # DataFrame

s3 = pd.Series(data=[3, 4, 5], index=['a', 'c', 'd'])
print(s3)

result = pd.concat((s1, s3), axis=0)
print(result)

result = pd.concat((s1, s3), axis=1)
print(result)  # outer join

# pandas.DataFrame의 concat
df1 = pd.DataFrame(data=np.arange(6).reshape((3, 2)),
                   index=['a', 'b', 'c'],
                   columns=['data1', 'data2'])
print(df1)

df2 = pd.DataFrame(data=np.arange(4).reshape((2, 2)),
                   index=['a', 'c'],
                   columns=['data3', 'data4'])
print(df2)

# df1, df2을 axis=0 방향으로 합치기(concat)
result = pd.concat((df1, df2))  # axix=0
print(result)

# df1, df2을 axis=1 방향으로 합치기(concat)
result = pd.concat((df1, df2), axis=1)  # outer join
print(result)

df1 = pd.DataFrame(data=np.arange(12).reshape((3, 4)))
df2 = pd.DataFrame(data=np.arange(12, 24).reshape((3, 4)))
# df1, df2을 axis=0으로 붙이기
result = pd.concat((df1, df2), ignore_index=True)
print(result)
