# install.packages("tidyverse")  # 패키지 설치
# library(tidyverse)  # 패키지 로드

# base 패키지의 column/row bind 기능
?cbind
?rbind

# dplyr 패키지: left_join, right_join, bind_rows
midterm_test <- data.frame(id = 1:5,
                           midterm = c(60, 80, 70, 90, 50))
midterm_test

final_test <- data.frame(id = 1:5,
                         final = c(70, 83, 65, 95, 88))
final_test

# left_join(DF1, DF2, by = 기준)
test1 <- left_join(midterm_test, final_test, by = "id")
test1

test2 <- right_join(midterm_test, final_test, by = "id")
test2

midterm_test <- data.frame(id = 1:4,
                           midterm = c(11, 22, 33, 44))
midterm_test

final_test <- data.frame(id = 2:5,
                         final = c(22, 33, 44, 55))
final_test

test1 <- left_join(midterm_test, final_test, by = "id")
test1
# NA: Not Available(결측치), missing value

test2 <- right_join(midterm_test, final_test, by = "id")
test2

test1 <- data.frame(id = 1:3,
                    score = c(10, 20, 30))
test1

test2 <- data.frame(id = 4:6,
                    score = c(40, 50, 60))
test2

test_all <- bind_rows(test1, test2)
test_all

# class, name 변수를 갖는 데이터 프레임(teachers)을 생성
# class = 1:6
teachers <- data.frame(class = 1:6,
                       name = c("a", "b", "c", "d", "e", "f"))
teachers
# data/csv_exam.csv 파일에서 데이터 프레임(exam) 생성
exam <- read.csv(file = "data/csv_exam.csv")
exam
# exam과 teachers를 left/right-join 결과 비교
exam_left <- left_join(exam, teachers, by = "class")
exam_left

exam_right <- right_join(exam, teachers, by = "class")
exam_right
