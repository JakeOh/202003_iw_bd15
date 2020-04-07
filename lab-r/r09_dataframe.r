rm(list = ls())

# data/csv_exam.csv 파일에서 데이터 프레임을 생성.
exam <- read.csv(file = "data/csv_exam.csv")

# 데이터 프레임의 처음 몇개의 라인만 출력.
head(exam, n = 3)  # n: 출력할 라인 수
# 데이터 프레임의 마지막 몇개의 라인만 출력.
tail(exam, n = 5)
# 데이터 프레임의 차원(dimension: 행과 열의 개수) 확인.
dim(exam)
# 데이터 프레임의 observation의 개수만 출력.
# dim(exam)[1]
d <- dim(exam)
d[1]
NROW(exam)  # number of rows(행의 개수)
NCOL(exam)  # number of columns(열의 개수)

v <- c(1, 2, 3)
nrow(v)  # 벡터는 행/열의 차원이 없기 때문에 NULL이라고 출력.
NROW(v)  # 벡터에서 원소의 개수.
NCOL(v)

# 데이터 프레임의 구조(structure)를 출력.
str(exam)

# 데이터 프레임의 기술 통계(descriptive statistics) 
# 정보 출력.
summary(exam)

df <- data.frame(var1 = c(4, 3, 8),
                 var2 = c(2, 6, 1))
df
# 데이터 프레임에 새로운 컬럼을 추가
# 파생 변수 추가: 기존 변수(컬럼)를 사용해서 만든 변수
df$sum <- df$var1 + df$var2
df
df$average <- df$sum / 2
df

# exam 데이터 프레임에 세과목 총점을 새로운 변수로 추가.
exam$total <- exam$english + exam$math + exam$science
exam
# exam 데이터 프레이메 세과목 평균을 새로운 변수로 추가.
exam$mean <- exam$total / 3
exam

# 데이터 프레임에서 변수(column)만 접근
exam$math
# 데이터 프레임에서 특정 행(row, observation)을 접근
exam[1, ]
exam[11:13,]
# 데이터 프레임에서 특정 행/열을 선택
exam[1:5, c(1, 3, 5)]
exam[1:3, -4]
exam[1:3, c("science", "id")]

