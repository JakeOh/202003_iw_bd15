import numpy as np
import pandas as pd

# pandas.DataFrame <==> numpy.ndarray
# 2차원 ndarray
arr = np.arange(12).reshape((3, 4))
print(arr)

# 2-d ndarray를 DataFrame으로 변환
df = pd.DataFrame(data=arr,
                  columns=['A', 'B', 'C', 'D'],
                  index=[100, 200, 150])
print(df)

# DataFrame을 2d ndarry로 변환
arr2 = df.values
print(arr2)

df['E'] = pd.Series(['aaa', 'bbb', 'ccc'],
                    index=[100, 200, 150])
print(df)

arr3 = df.values
print(arr3)
print(arr3[0, 0], type(arr3[0, 0]))
print(arr3[0, 4], type(arr3[0, 4]))

print(np.array([1, 'ab']))
