import numpy as np

# NumPy의 통계 관련 함수: 합계, 평균, 표준편차, 최솟값, 최댓값, ...
#   sum, mean, std, var(분산), min, max, ...
# np.함수(ndarray)
# ndarray.메서드()

a = np.arange(10)
print(a)

print(np.sum(a))  # np.함수(array)
print(a.sum())  # array.메서드()

print(np.mean(a), a.mean())
print(np.max(a), a.max())
print(np.median(a))  # median() 함수는 numpy 모듈에만 있음!

# np.max()/min() VS np.maximum()/minimum() 차이
# np.max(array): array의 원소들 중에서 최댓값
# np.maximum(arr1, arr2): 두 array의 원소들을 비교해서 최댓값을 찾음
a = np.random.randint(10, size=5)
b = np.random.randint(10, size=5)
print(a)
print(b)
print(np.maximum(a, b))

# np.argmax(array), array.argmax(): array의 최댓값의 인덱스를 반환
# np.argmin(array), array.argmin(): array의 최솟값의 인덱스를 반환
print(np.argmax(a), a.argmax())

a = np.random.randint(10, size=(2, 3))
print(a)
print(np.sum(a), a.sum())  # 2-d array의 모든 원소들의 합
print(np.sum(a, axis=0), a.sum(axis=0))  # axis=0 축을 따라서 합계를 계산
print(np.sum(a, axis=1), a.sum(axis=1))  # axis=1 축을 따라서 합계 계산
print(np.argmax(a))
print(np.argmax(a, axis=0))
print(np.argmax(a, axis=1))
