import pandas as pd

df = pd.read_csv('ex_pivot.csv')
print(df)

# DataFrame에서 variable 컬럼의 값이 'A'인 모든 row 데이터
df_a = df[df['variable'] == 'A']
print(df_a)

# DataFrame에서 variable 컬럼의 값이 'B'인 모든 row 데이터
df_b = df[df.variable == 'B']
print(df_b)

# pivot: row -> column: Long -> Wide
pivoted = df.pivot(index='date', columns='variable', values='value')
# pivot() 메서드의 arguments
#   index: DataFrame에서 index로 사용할 컬럼(들)의 이름
#   columns: pivoting할 컬럼(들)의 이름
#   values: pivoting된 컬럼의 값으로 사용할 컬럼(들)의 이름
print(pivoted)

wide = pivoted.reset_index()
print(wide)

# melt: column -> row: Wide -> Long
melted = wide.melt(id_vars=['date'])
print(melted)
