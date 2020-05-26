import pandas as pd
import seaborn as sns

# category(범주형) 변수: 성별, 지역, ...
# R - factor 변수
# category 타입이 생긴 이유: 성능을 빠르게, 메모리 절약

# category 변수와 category 변수가 아닐 때 차이점.
fruits = pd.Series(['apple', 'banana', 'cherry', 'apple', 'banana'] * 10)
print(fruits)  # 중복되는 값들 모두 출력
# dtype: object(문자열)

# fruits에서 중복되지 않은 값들
print(fruits.unique())
# fruits의 중복되지 않는 값들이 각각 몇개씩 있는지
print(fruits.value_counts())

# 중복되지 않는 값들을 코드화: apple(0), banana(1), cherry(2)
values = pd.Series([0, 1, 2, 0, 1] * 10)
dim = pd.Series(['apple', 'banana', 'cherry'])
print(dim.take(values))

print('object Series memory:', fruits.memory_usage())

# fruits Series를 catetory 타입으로 변환
fruits_cat = fruits.astype('category')
print(fruits_cat)  # dtype: category
print('category series memory:', fruits_cat.memory_usage())

# seaborn 패키지에서 tips 데이터 프레임을 로드
tips = sns.load_dataset('tips')
tips.info()
print(tips.iloc[:5, 2:6])

# ../examples/tips.csv 파일을 데이터 프레임을 생성
tips2 = pd.read_csv('../examples/tips.csv')
tips2.info()
# object 타입의 컬럼들을 category 타입으로 변환
tips2['smoker'] = tips2['smoker'].astype('category')
tips2['day'] = tips2['day'].astype('category')
tips2['time'] = tips2['time'].astype('category')
tips2.info()
