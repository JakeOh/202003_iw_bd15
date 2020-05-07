import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# seaborn 패키지에 포함되 tips 샘플 DataFrame을 로드
tips = sns.load_dataset('tips')
print(type(tips))
print(tips.shape)  # 244 rows x 7 columns
print(tips.iloc[:5])  # tips.head()
print(tips.iloc[-5:])  # tips.tail()

# total_bill 컬럼의 평균, 표준편차, 최솟값, 최댓값을 찾아보세요.
print(type(tips['total_bill']))
bill = tips['total_bill']  # 컬럼 선택
print('mean:', bill.mean())
print('standard deviation:', bill.std())
print('min:', bill.min())
print('max:', bill.max())

# total_bill의 최댓값 row를 찾아 출력
# 1) boolean indexing
print(tips[tips['total_bill'] == bill.max()])
# select * from tips where total_bill == max(total_bill);
# 2) iloc 사용
# print(bill.argmax())
print(tips.iloc[bill.argmax()])

sns.boxplot(y='total_bill', data=tips)
plt.show()

# smoker/non-smoker 빈도수
freq_smoker = tips['smoker'].value_counts()
print(freq_smoker)

sns.countplot(x='smoker', data=tips)
plt.show()

# 히스토그램: 연속형 변수를 일정한 구간으로 나눠서 그 구간에 포함되는 빈도수를
# 나타낸 그래프
sns.distplot(tips['total_bill'], hist=True, kde=True)
# distribution plot
#   hist: 히스토그램을 그릴지 여부(True/False)
#   kde(Kernel Density Estimation): 커널 밀도 추정 함수를 그릴지 여부
plt.show()

# 요일별 tip의 평균을 찾아보세요.
# 1) day == 일요일 부분집합
sunday = tips[tips['day'] == 'Sun']
print(sunday)
# 2) 부분집합에서 tip 컬럼 선택 -> 평균
tip_sunday = sunday['tip'].mean()
print(tip_sunday)

# 3) 1, 2 과정을 다른 요일에 대해서도 반복
saturday = tips[tips['day'] == 'Sat']
print(saturday.shape)
tip_saturday = saturday['tip'].mean()
print(tip_saturday)

friday = tips[tips['day'] == 'Fri']
print(friday.shape)
tip_friday = friday['tip'].mean()
print(tip_friday)

thursday = tips[tips['day'] == 'Thur']
print(thursday.shape)
tip_thursday = thursday['tip'].mean()
print(tip_thursday)

# 성별 tip의 평균을 찾아보세요.
male_tip = tips[tips['sex'] == 'Male']['tip'].mean()
print('남성 tip 평균:', male_tip)
female_tip = tips[tips['sex'] == 'Female']['tip'].mean()
print('여성 tip 평균:', female_tip)

# 일요일에 식사한 non-smoker 여성들의 자료에서 tip의 평균과 최댓값을 찾으세요.
subset = tips[(tips['day'] == 'Sun') &
              (tips['sex'] == 'Female') &
              (tips['smoker'] == 'No')]
print(subset)
print('tip 평균:', subset['tip'].mean())
print('tip 최댓값:', subset['tip'].max())
