# MNIST 데이터 로드
# Train(60,000)/Test(10,000)로 분리
# Random Forest 알고리즘에 Train 셋을 훈련 - fit
# 훈련 시간을 측정, 출력
# 훈련된 모델로 Test 셋의 성능 측정 - 정확도 계산

# explained variance ratio의 누적값이 95%이상이 되는 주성분 축만큼 선택
# PCA(주성분 분석)를 적용해서 Train 셋을 변환 - 차원 축소
# 차원이 축소된 훈련 셋에서 Random Forest를 훈련.
# Random Forest 훈련 시간 측정
# 훈련된 모델로 Test 셋의 성능(정확도)를 계산

# LogisticRegression 모델을 선택해서 위의 과정 반복
# PCA를 적용했을 때와 PCA를 적용하지 않았을 때의 훈련시간/정확도 차이 비교

