import numpy as np
import pandas as pd

np.random.seed(1)

s = pd.Series(data=list('ABCD') * 2)
# list('ABCD') = ['A', 'B', 'C', 'D']
print(s)  # object를 원소로 갖는 Series

# astype('category'): Series -> Category 타입 변환
s2 = s.astype('category')
print(s2)  # category

# Series객체.str 속성: str 클래스의 속성, 메소드를 사용할 수 있음.
#   df['name'].str.contains(...), df['name'].str.lower(),
# Category객체.cat 속성: Category 클래스의 속성, 메소드를 사용할 수 있도록 해주는 속성.
# .cat accessor는 Series에서는 사용할 수 없고, category에서만 사용할 수 있음.
print(s2.cat.categories)
print(s2.cat.codes)

# astype()을 사용하면 unique(중복되지 않는) 값들로만 Category를 생성함.
# 데이터에 없는 값을 Category에 포함시키려면 set_categories()를 사용함.
# s.astype('category').cat.set_categories([])
s3 = s2.cat.set_categories(list('ABCDF'))
print(s3)

print(s2.value_counts())
print(s3.value_counts())

# remove_unused_categories(): 사용되지 않는 category를 삭제
s4 = s3.cat.remove_unused_categories()
print(s4)

# remove_categories(removals): 기존에 있는 category들 중 일부를 삭제.
# 해당 category에 속한 값들은 NA로 설정
s5 = s4.cat.remove_categories(removals=['A'])
print(s5)
