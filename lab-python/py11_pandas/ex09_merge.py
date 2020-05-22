import numpy as np
import pandas as pd

# 여러개의 컬럼들 또는 MultiIndex를 이용한 merge/join
left_df = pd.DataFrame(data={'key1': ['a', 'a', 'a', 'b', 'b'],
                             'key2': [2000, 2001, 2002, 2001, 2002],
                             'data1': np.random.randn(5)})
print(left_df)

right_df = pd.DataFrame(data={'data2': np.random.randint(0, 10, 5)},
                        index=[['a', 'a', 'a', 'b', 'b'],
                               [2000, 2001, 2002, 2001, 2002]])
print(right_df)

# df = pd.merge(left_df, right_df,
#               left_on=['key1', 'key2'], right_index=True)
# df = left_df.merge(right_df,
#                    left_on=['key1', 'key2'], right_index=True)
df = left_df.join(right_df, on=['key1', 'key2'])
print(df)

# df2 = pd.merge(right_df, left_df,
#                left_index=True, right_on=['key1', 'key2'])
df2 = right_df.merge(left_df,
                     left_index=True, right_on=['key1', 'key2'])
print(df2)

# df3 = right_df.join(left_df, on=['key1', 'key2'])
# ValueError 발생
# df1.join(df2, on=...) 메소드는
# 1) df1, df2 모두 index를 사용해서 join하거나,
# 2) df1은 컬럼을 사용하고, df2은 index를 사용해서 join할 수 있음.
