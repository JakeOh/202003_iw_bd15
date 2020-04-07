# 제어문: 조건문, 반복문.
# for 반복문
# for (변수 in 벡터/리스트/...) { 
#   반복할 문장들.
# }
v <- 1:5
v
for (i in v) {
  print(i)
}

print(i)
cat(i)  # concatenate and print
cat("i =", i)
a <- 1
cat(a, "x", 2, "=", a * 2)

# 구구단 9단을 출력:
# 9 x 1 = 9
# 9 x 2 = 9
# ...
# 9 x 9 = 81
for (i in 1:9) {
  cat(9, "x", i, "=", 9 * i, "\n")
}

for (i in 1:9) {
  for (j in 1:9) {
    cat(i, "x", j, "=", i * j, "\n")
  }  # end for(j)
  cat("----------\n")
}  # end for(i)

# 구구단 출력:
# 2단은 2x2까지, 3단은 3x3까지, ...
for (i in 1:9) {
  for (j in 1:i) {
    cat(i, "x", j, "=", i * j, "\n")
  }  # end for(j)
  cat("----------\n")
}  # end for(i)

# 벡터의 원소가 짝수인지 홀수인지 출력
# a %% b: a를 b로 나눈 나머지 계산
# a %/% b: a를 b로 나눈 몫 계산
1:6 %% 2
1:6 %/% 2
v <- c(10, 21, 55, 98)
for (i in v) {
  if (i %% 2 == 0) {
    cat(i, "= 짝수\n")
  } else {
    cat(i, "= 홀수\n")
  }
}

# break: 반복문을 중간에 종료할 때 사용.
for (i in 1:10) {
  if (i >= 5) {
    break
  }
  cat(i, "\n")
}

# 2중 반복문 안에서 break는, 
# break가 포함된 가장 가까운 반복문만 종료함.
# break를 사용한 구구단 출력
for (i in 1:9) {
  for (j in 1:9) {
    cat(i, "x", j, "=", i * j, "\n")
    if (j == i) {
      break
    }
  }
  cat("----------\n")
}

# next: 반복하던 블록을 멈추고, 그다음 반복을 위해서
# 반복문 처음으로 돌아감.
for (i in 1:5) {
  if (i == 3) {
    next
  }
  cat(i, "\n")
}

# 1 ~ 10까지 정수들 중에서 짝수만 출력
for (i in 1:5) {
  cat(i * 2, " ")
}

for (i in 1:10) {
  if (i %% 2 == 0) {
    cat(i, " ")
  }
}

for (i in seq(2, 10, 2)) {
  cat(i, " ")
}

for (i in 1:10) {
  if (i %% 2 == 1) {
    next
  }
  cat(i, " ")
}



