import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({'data': np.arange(6)})
print(df)

result = df.rolling(2).sum()
print(result)

result = df.rolling(2).mean()
print(result)

result = df.rolling(3).sum()
print(result)

rng = pd.date_range(start='2020-1-29', periods=100)
s = pd.Series(data=np.arange(100), index=rng)
print(s)

# resample
result = s.resample('M').sum()
print(result)

result = s.rolling(30).sum()
print(result)

# ../examples/stock_px_2.csv
df = pd.read_csv('../examples/stock_px_2.csv',
                 index_col=0,
                 parse_dates=True)
print(df.iloc[:5])
print(df.iloc[-5:])
print(df.index)

df['AAPL'].plot()
df['AAPL'].rolling(60).mean().plot()
plt.show()
