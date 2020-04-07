# Control Statement(제어문)
# 1) 조건문
# if (조건식) {
#   조건식이 참일 때 실행할 문장들.
# } else {
#   조건식이 거짓일 때 실행할 문장들.  
# }
x <- 10
if (x > 0) {  # x가 0보다 클 때 할 기능들.
  print("양수")
} else { # x가 0보다 크지 않을 때 할 기능들.
  print("Not positive")
}

if (x > 0) {
  print("positive")
} else if (x < 0) {
  print("negative")
} else {
  print("zero")
}

v <- c(1, -2, 0)
v != 0
# 비교 연산자(>, <, ==, !=)
if (v > 0) {
  print("P")
} else if (v == 0) {
  print("N")
} else {
  print("Z")
}

# if - else 문에서 조건식에 벡터가 사용되면,
# 벡터의 첫번째 원소만 조건 검사에 사용됨.

# ifelse(조건식, 참일 때 값, 거짓일 때 값)
t <- ifelse(v > 0, "YES", 
            ifelse(v < 0, "NO", "zero"))
t

# data/csv_exam.csv 파일에서 데이터 프레임 생성.
exam <- read.csv(file = "data/csv_exam.csv")
# 데이터 프레임에 세과목 총점/평균 컬럼(변수)을 추가.
colnames(exam)
exam$tot <- exam$math + exam$english + exam$science
exam$mean <- exam$tot / 3
head(exam)
colnames(exam)[6] <- "total"
head(exam)
# 데이터 프레임에 grade 컬럼(변수)를 추가
#   - 평균 >= 80이면, "A"
#   - 평균 >= 60이면, "B"
#   - 평균 < 60이면, "F"
exam$grade <- ifelse(exam$mean >= 80, "A",
                     ifelse(exam$mean >= 60, "B", "F"))
tail(exam)
head(exam)

