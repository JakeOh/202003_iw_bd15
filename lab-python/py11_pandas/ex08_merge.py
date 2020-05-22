import pandas as pd
import numpy as np

# merge() 함수/메소드의 argument들
# how: merge 방법. inner(기본값), left, right, outer
# on: 두 개의 DataFrame을 merge하는 기준이 되는 컬럼(들).
#   두 DF이 같은 이름의 컬럼을 가지고 있는 경우.
# left_on, right_on: 두 DF에서 다른 이름의 컬럼으로 merge할 때. 컬럼(들) 이름.
# left_index, right_index: 인덱스로 merge할 때. True/False(기본값)

# merge/join을 하는 데이터 프레임의 컬럼 이름이 다른 경우: left_on, right_on
employees = pd.DataFrame({'empno': [1234, 1235, 1236, 1237, 1240],
                          'deptno': [10, 10, 20, 30, np.nan]})
print(employees)

departments = pd.DataFrame({'dno': [10, 20, 30, 40],
                            'dname': ['HR', 'ACC', 'SAL', 'RES']})
print(departments)

emp_dept = pd.merge(employees, departments,
                    left_on='deptno', right_on='dno')
print(emp_dept)  # inner join: 두 DF에서 공통으로 존재하는 데이터들

emp_dept2 = pd.merge(employees, departments,
                     left_on='deptno', right_on='dno', how='outer')
# how의 값을 'left', 'right', 'outer'로 테스트
print(emp_dept2)

# index로 merge/join: left_index, right_index
df_left = pd.DataFrame(data={'data1': np.arange(6)},
                       index=['a', 'b', 'c'] * 2)
print(df_left)

df_right = pd.DataFrame(data={'data2': [11, 22, 33, 44]},
                        index=['a', 'b', 'c', 'd'])
print(df_right)

# df = pd.merge(df_left, df_right,
#               left_index=True, right_index=True, how='outer')
df = df_left.merge(df_right,
                   left_index=True, right_index=True, how='outer')
print(df)

df_left2 = pd.DataFrame(data={'key': ['a', 'b', 'c'] * 2,
                              'data1': np.arange(6)})
print(df_left2)
print(df_right)

# left DF은 컬럼으로, right DF은 인덱스로 merge
df = pd.merge(df_left2, df_right,
              left_on='key', right_index=True, how='outer')
print(df)

# pandas.merge(left, right, ...) 함수
# pandas.DataFrame.merge(right, ...) 메서드
# merge 함수/메서드는 컬럼-컬럼/인덱스-인덱스/컬럼-인덱스/인덱스-컬럼으로 merge 가능

# panas.DataFrame.join(right, ...) 메서드
# 인덱스-인덱스/컬럼-인덱스로 join 가능.
print(df_left)
print(df_right)
# df = pd.merge(df_left, df_right, left_index=True, right_index=True)
# df = df_left.merge(df_right, left_index=True, right_index=True)
df = df_left.join(df_right)  # index-index join
print(df)

print(df_left2)
df = df_left2.join(df_right, on='key')  # column-index join
# df = df_left2.merge(df_right,
#                     left_on='key', right_index=True, how='left')
# df = pd.merge(df_left2, df_right,
#               left_on='key', right_index=True, how='left')
print(df)
