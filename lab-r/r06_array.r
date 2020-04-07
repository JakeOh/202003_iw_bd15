rm(list = ls())

# 배열(array):
# 같은 타입의 원소 여러개를 3차원 이상으로 저장하는 타입.
# array(data, dim, dimnames)
a1 <- array(data = 1:24, dim = c(2, 3, 4))
a1

# 배열(array)의 원소 접근: [x, y, z] 인덱스 사용.
a1[1, 2, 1]
a1[2, 2, 4]
a1[1, 1, ]
a1[, -3,]  # a1[1:2, 1:2,]


