# 행렬(matrix): 한가지 타입의 원소들 여러개를 저장하는 
# 2차원 벡터.
# -> 행(row), 열(column) 인덱스 2개가 있음.
# matrix(data, nrow, ncol, byrow) 함수: 행렬 생성.
# data: 행렬의 원소들.
# nrow: 행의 개수
# ncol: 열의 개수
# byrow: 행의 원소들부터 채울 것인지 아닌지. 
#   FALSE가 기본값 -> 세로방향부터 데이터를 채움.
#   byrow = TRUE -> 가로방향부터 데이터를 채움.
m <- matrix(data = 1:12, nrow = 3)
m

m2 <- matrix(data = 1:12, nrow = 3, byrow = FALSE)
m2

m2 <- matrix(data = 1:12, nrow = 3, byrow = TRUE)
m2

zero_matrix <- matrix(data = 0, nrow = 2, ncol = 2)
zero_matrix

# 항등 행렬(identity matrix)
# 정사각행렬에서 대각선의 원소는 1이고, 
# 대각선 이외의 원소들은 0인 행렬.
identity_matrix <- diag(nrow = 3, ncol = 3)
identity_matrix

# 대각 행렬: 대각선 이외에는 0으로 채워진 행렬.
diag_matrix <- diag(x = 5, nrow = 2, ncol = 3)
diag_matrix
diag_matrix2 <- diag(x = c(1, 2), nrow = 2, ncol = 3)
diag_matrix2

# 행렬 +,-,*,/ 스칼라:
# 행렬의 각 원소에 스칼라 값을 사칙연산함.
A <- matrix(data = 1:4, nrow = 2, byrow = TRUE)
A
A + 1

# 행렬 +,-,*,/ 행렬:
# 같은 위치의 원소들끼리 사칙연산함.
B <- matrix(data = c(1, 1, 2, 2), nrow = 2, 
            byrow = TRUE)
B
A * B

# 내적(inner product): 행렬 %*% 행렬
A %*% B

A <- matrix(data = c(1, 2, 3, 2, 3, 4),
            nrow = 2,
            byrow = TRUE)
A
B <- matrix(data = c(1, 0, 1, 0, 1, 1),
            nrow = 3)
B
A %*% B
B %*% A

# 전치 행렬(transpose): 행과 열을 바꾼 행렬
A
t(A)

# 역행렬(reverse matrix): 
# inner product의 결과가 항등행렬이 되는 행렬.
# A %*% X = I, X %*% A = I를 만족하는 행렬
A <- matrix(data = 1:4, nrow = 2)
A
X <- solve(A)
X
A %*% X
X %*% A

# 행렬의 원소 접근: [row index, col index] 형식을 사용.
A <- matrix(data = 1:12, nrow = 3)
A
A[1, 1]
A[2, 3]
A[1:2, 2:3]
A[2:3, 2:4]
A[-1, -1]

