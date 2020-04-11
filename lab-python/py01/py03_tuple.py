"""
tuple: 여러개의 값들을 저장할 수 있는,
저장된 원소들을 변경할 수 없는(immutable) 데이터 타입
"""

numbers = (1, 2, 3, 4, 5)
print(numbers, type(numbers))
print(numbers[1:3])
# numbers[0] = 123  # TypeError - tuple은 값 변경 불가

# decomposition(unpack)
x, y, z = (11, 22, 33)
print(x, y, z)




