# 함수(function):

# 함수 정의(definition)
# parameter(파라미터, 매개변수, 인자):
# 전달받은 argument를 저장하기 위해 선언하는 변수.
subtract <- function(x, y) {
  return(x - y)  # 실행 결과 반환
}

result <- subtract(1, 2)  # 함수 호출(call, invoke)
# argument(인수): 함수를 호출할 때 함수에 전달하는 값.

subtract()  # 에러 발생
subtract(1)  # 에러 발생
# 함수를 정의할 때, 기본값이 설정되지 않은 argument는 
# 반드시 함수를 호출할 때 전달해야 함.

subtract(1, 2, 3)  # 에러 발생
# 함수에 정의된 파라미터 개수보다 더 많은 argument를
# 전달할 수는 없음.

# argument를 전달하는 방법:
# 1) positional argument: 순서대로 전달.
subtract(1, 2)
subtract(2, 1)
# 2) argument 이름(파라미터)를 명시.
# -> 순서대로 전달하지 않아도 됨.
subtract(x = 1, y = 2)
subtract(y = 2, x = 1)
subtract(1, y = 2)
subtract(1, x = 1)

# default argument:
# 함수를 정의할 때 파라미터에 기본값을 설정하는 것.
add <- function(x, y = 0) {
  return(x + y)
}

add(1, 2)
add(1)
add(x = 1)
add(y = 1)  # 에러 발생

# 변수 범위(scope)
x <- "테스트"  # global(전역) 변수

test <- function() {
  cat(x, "\n")
  x <- 100  # 지역 변수(local variable)
  cat(x, "\n")
}

test()
x

test_even <- function(x) {
  return(ifelse(x %% 2 == 0, "even", "odd"))
}

test_even(3)

# 가변 길이 인수(variable-length argument)
add_all <- function(...) {
  args <- list(...)
  sum <- 0
  for (x in args) {
    sum <- sum + x
  }
  return(sum)
}

add_all(1, 2, 3)

sum(1, 2)

