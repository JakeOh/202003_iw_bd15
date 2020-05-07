import numpy as np

# Broadcast: 크기가 다른 array끼리 산술 연산(+, -, *, /, ...)을 하는 방법
# 행 또는 열의 갯수 둘 중 하나가 같은 경우에만 broadcast가 가능

a = np.arange(1, 7).reshape((2, 3))
print(a)
b = np.arange(7, 10)
print(b)

print(a + b)

b = np.array([[7], [8]])
print(b)

print(a + b)


