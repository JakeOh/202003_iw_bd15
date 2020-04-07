dan <- 1
while (dan < 10) {
  n <- 1  # 1부터 시작.
  while (n < 10) {
    cat(dan, "x", n, "=", dan * n, "\n")  # 출력
    n <- n + 1  # n(곱하는 숫자)를 1 증가시킴.
  }
  cat("---------------\n")
  dan <- dan + 1  # 단을 1 증가시킴.
}
