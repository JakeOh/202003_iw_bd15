import numpy as np
import matplotlib.pyplot as plt

# NumPy universal functions
# NumPy의 거의 모든 함수들은 반복문 없이 array의 각 원소들 별(element-wise)로
# 계산을 수행할 수 있는 기능을 가지고 있음.

a = np.arange(10)
print(a)
print(np.sqrt(a))
print(np.exp(a))

x = np.arange(-5, 5, 0.01)
y = np.exp(x)
plt.plot(x, y)
plt.show()

y = 1 / (1 + np.exp(-x))  # sigmoid 함수
plt.plot(x, y)
plt.show()




