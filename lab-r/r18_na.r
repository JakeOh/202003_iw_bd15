# Missing Value(결측치): 데이터 프레임에서 빠져있는 값.
# NA(Not Available): 결측치를 표기하는 예약어.

df <- data.frame(gender = c("F", "M", NA, "M", "F"),
                 age = c(25, 31, 29, 34, NA))
df
str(df)
summary(df)

is.na(df)
is.na(df$gender)

table(is.na(df))
table(is.na(df$age))

# age 변수의 평균
mean(df$age)  # NA
mean(df$age, na.rm = TRUE)  # 29.75
# argument na.rm: NA를 제거할 것인지(TRUE), 아닌지(FALSE).
# sum(), mean(), sd(), min(), max(), ... 과 같은 함수들은
# na.rm argument를 가지고 있음.

sum(df$age)
sum(df$age, na.rm = TRUE)

# missing value(NA) 제거
# age 변수의 NA를 제거한 데이터 프레임을 출력
library(tidyverse)
df %>% 
  filter(!is.na(age))
# ! 연산자: NOT (TRUE -> FALSE, FALSE -> TRUE)

# gender, age 모두 NA 아닌 값들을 출력
df %>% 
  filter(!is.na(gender) & !is.na(age))

df_omit <- na.omit(df)
df_omit

# missing value 처리
# 1) missing value 제거 -> 데이터의 개수가 작아질 수 있음.
# 2) missing value를 대푯값으로 대체
#    평균, 최빈값(가장 자주 등장하는 값), 중앙값, ...

exam <- read.csv(file = "data/csv_exam.csv")

# NA를 삽입.
exam[c(3, 8, 15), "math"] <- NA
exam

# 수학 점수 평균
mean(exam$math, na.rm = TRUE)

# exam 데이터 프레임에서 수학/영어/과학 평균 출력.
exam %>% 
  summarise(m_math = mean(math, na.rm = TRUE),
            m_eng = mean(english),
            m_sci = mean(science))

# exam 데이터 프레임에서 수학 점수의 합계, 평균, 표준편차
exam %>% 
  summarise(total = sum(math, na.rm = TRUE),
            average = mean(math, na.rm = TRUE),
            stddev = sd(math, na.rm = TRUE))

# exam 데이터 프레임에서 math의 NA를 평균값으로 대체.
average <- mean(exam$math, na.rm = TRUE)
average <- round(average)
# floor(): 내림, ceiling(): 올림, round(): 반올림
exam$math <- ifelse(is.na(exam$math), average, exam$math)
exam
table(exam$english)


exam <- read.csv(file = "data/csv_exam.csv")
exam[c(3, 8, 15), "math"] <- NA
exam
# 각 반(class)의 수학 평균 점수로 NA를 대체
grouped_mean <- exam %>% 
  group_by(class) %>% 
  summarise(avg = mean(math, na.rm = TRUE))

grouped_mean
grouped_mean[1, "avg"]  # tibble(data frame)
grouped_mean$avg[1]  # 숫자(scalar)

grouped_mean$avg <- round(grouped_mean$avg)
grouped_mean

exam$math <- ifelse(!is.na(exam$math), exam$math,
                ifelse(exam$class == 1, grouped_mean$avg[1],
                       ifelse(exam$class == 2, grouped_mean$avg[2],
                              ifelse(exam$class == 3, grouped_mean$avg[3],
                                     ifelse(exam$class == 4, grouped_mean$avg[4], 
                                            grouped_mean$avg[5])))))

exam

# ifelse(!NA, math, 
#        ifelse(cls==1, avg[1], 
#               ifelse(cls==2, avg[2], 
#                      ifelse(cls==3, avg[3], 
#                             ifelse(cls==4, avg[4], 
#                                    avg[5])))))

exam[c(3, 8, 15), "math"] <- NA
for (c in 1:5) {
  if (is.na(exam[c, "math"])) {
    exam[c, "math"] <- grouped_mean$avg[exam[c, "class"]]
  }
}
exam

# ggplot2::mpg 데이터 이용
library(tidyverse)

# 65, 124, 131, 153, 212행의 hwy 값을 NA로 만듦.
mpg <- as.data.frame(ggplot2::mpg)
mpg[c(65, 124, 131, 153, 212), "hwy"] <- NA
summary(mpg)
table(is.na(mpg$hwy))

# 구동방식(drv)별 고속도로연비(hwy) 평균을 계산하기 위해
# Q1) drv, hwy 변수의 NA 개수를 확인
table(is.na(mpg$drv))  # drv 변수의 NA 개수
table(is.na(mpg$hwy))  # hwy 변수의 NA 개수

# Q2) 모든 NA를 제거하고, drv별 hwy 평균을 계산
mpg %>% 
  group_by(drv) %>% 
  summarise(mean_hwy = mean(hwy, na.rm = TRUE))

mpg %>% 
  filter(!is.na(hwy)) %>% 
  group_by(drv) %>% 
  summarise(mean_hwy = mean(hwy))




