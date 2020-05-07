import numpy as np
# NumPy(Numerical Python):
# 배열을 쉽고, 빠르게 연산
# 대부분의 함수들이 반복문의 기능을 가지고 있음.
# numpy.ndarray: NumPy에서 사용하는 데이터 타입(클래스)
#   n-dimensional array

nums1 = np.array([1, 2, 3])
nums2 = np.array([4, 5, 6])
print(nums1)
print(nums2)
print(type(nums1))

add = nums1 + nums2
print(add)
# numpy.ndarry에서 산술 연산은 원소별(element-wise)로 덧셈을 함.
print(nums1 - nums2)
print(nums1 * nums2)
print(nums1 / nums2)
print(nums1 @ nums2)  # Python 3.5 이상에서만 가능
print(np.dot(nums1, nums2))
print(nums1.dot(nums2))

mat_a = np.array([[1, 2],
                  [3, 4]])
mat_b = np.array([[1, 2],
                  [4, 3]])
print(mat_a)
print(mat_b)
print(mat_a + mat_b)
print(mat_a @ mat_b)

print(nums1 * 3)


