# 연속형 변수를 카테고리 변수로 변경
import numpy as np
import pandas as pd

ages = pd.Series(np.random.randint(10, 70, 10))
print(ages)

bins = range(10, 80, 20)  # pd.Series(np.arange(10, 80, 20))
print(bins)

ages_cut = pd.cut(ages, bins, right=False)
print(ages_cut)

bins = [10, 30, 60, 70]
ages_cut2 = pd.cut(ages, bins, right=False)
print(ages_cut2)

print(ages_cut.value_counts())
print(ages_cut2.value_counts())

