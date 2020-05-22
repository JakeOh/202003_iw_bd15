import numpy as np
import pandas as pd

np.random.seed(1)
ages = [10, 15, 13, 12, 23, 25, 28, 33, 59, 60]
df = pd.DataFrame({'age': ages,
                   'data1': np.random.randn(10)})

print(df)

c = pd.cut(df['age'], bins=[0, 18, 35, 70])
print(c)

counts = df.groupby(c).size()
print(counts)

mean_by_ages = df.groupby(c)['data1'].mean()
print(mean_by_ages)

c2 = pd.cut(df['age'], bins=np.arange(10, 80, 10), right=False)
print(c2)

mean_by_ages = df.groupby(c2).mean()
print(mean_by_ages)
