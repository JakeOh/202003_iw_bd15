# 데이터 전처리(pre-processing)
# tidyverse 패키지: ggplot2, dplyr, tidyr, readr, ...
install.packages("tidyverse")
library(tidyverse)
search()

# mpg 데이터 프레임
mpg
head(mpg)
str(mpg)  # data frame 구조
summary(mpg)  # 기술 통계량

ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy, 
                           color = class))

# dplyr::filter()
# 조건에 맞는 데이터(observation)을 추출.
exam <- read.csv(file = "data/csv_exam.csv")
head(exam)
tail(exam)

# filter(데이터 프레임, 조건)
filter(exam, class == 1)


# 데이터 프레임 %>% filter(조건)
exam %>% filter(class == 2)

# exam 데이터 프레임에서 class가 2인 데이터를 class2에 저장.
class2 <- filter(exam, class == 2)
class2
# class2 데이터 프레임에서 math가 80 이상인 데이터만 추출.
filter(class2, math >= 80)

exam %>%
  filter(class == 2) %>%
  filter(math >= 80)

# %>%: pipe 연산자.
# 데이터 프레임 %>% 함수()
# 데이터 프레임을 함수의 첫번째 argument로 전달.
# Ctrl + Shift + M

# class 값이 1이 아닌 데이터만 추출.
filter(exam, class != 1)
exam %>% filter(class != 1)

# 수학 점수가 50점 이상인 데이터 추출.
filter(exam, math >= 50)
exam %>% filter(math >= 50)

# 과학 점수가 50점 미만인 데이터 추출.
filter(exam, science < 50)
exam %>% filter(science < 50)

# 논리 연산자: &, |
# A & B: A와 B가 모두 TRUE이면 TRUE, 그 이외에는 FALSE.
# A | B: A 또는 B 중 적어도 하나가 TRUE이면 TRUE, 아니면 FALSE.

# class가 1이고, math가 50 이상인 데이터 추출.
exam %>% 
  filter(class == 1 & math >= 50)

# class가 2이고, english가 80점 이상인 데이터 추출.
exam %>% 
  filter(class == 2 & english >= 80)

# 수학 점수가 90점 이상이거나 또는 영어 점수가 90점 이상인
# 데이터 추출.
exam %>% 
  filter(math >= 90 | english >= 90)

# 영어 점수가 90점 미만이거나, 과학 점수가 50점 미만인 경우.
exam %>% 
  filter(english < 90 | science < 50)

summary(exam)
mean(exam$math)  # 평균 계산

# 세 과목의 점수가 모두 평균 이상인 학생들 추출.
exam %>% 
  filter(math >= mean(math) &
           english >= mean(english) &
           science >= mean(science))

# 1, 3, 5반 학생들 추출.
exam %>% 
  filter(class == 1 | class == 3 | class == 5)

exam %>% filter(class %in% c(1, 3, 5))


# dplyr:: select()
# 필요한 컬럼(변수)들을 추출
exam$math
# select(데이터 프레임, 컬럼 이름들, ...)
select(exam, math)
# 데이터 프레임 %>% select(컬럼 이름들, ...)
exam %>% select(math)

# id와 수학 점수 선택.
select(exam, id, math)
exam %>% select(id, math)

# 특정 컬럼(변수)를 제외.
select(exam, -class)
exam %>% select(-class)

# english와 science 컬럼 제외
exam %>% select(-english, -science)

# 1반(class==1) 학생들의 id, class, math를 출력.
exam %>% 
  filter(class == 1) %>% 
  select(id, class, math)

# 수학 점수가 평균 이상인 학생들의 id, math를 출력.
exam %>% 
  filter(math >= mean(math)) %>% 
  select(id, math)


head(mpg)
# ggplot2::mpg 데이터 프레임에서
# 1) displ(배기량)이 4이하인 자동차와 5이상인 자동차의
# hwy(고속도로 연비) 평균을 계산.
# 배기량 4이하인 자동차들
# df1 <- filter(mpg, displ <= 4)
df1 <- mpg %>%  filter(displ <= 4)
# 고속도로 연비 평균
mean(df1$hwy)

df2 <- mpg %>% filter(displ >= 5)  # 배기량 5이상
mean(df2$hwy)  # 고속도로 연비 평균

# 2) "audi"와 "toyota" 중 어느 manufacturer의 
# cty(도시 연비)의 평균이 더 높은지.
df_audi <- mpg %>% filter(manufacturer == "audi")
mean(df_audi$cty)
df_toyota <- mpg %>% filter(manufacturer == "toyota")
mean(df_toyota$cty)

# 3) "chevrolet", "ford", "honda" 자동차를 추출해서
# hwy의 전체 평균을 계산.
df <- mpg %>% 
  filter(manufacturer == "chevrolet" | 
           manufacturer == "ford" |
           manufacturer == "honda")
df <- mpg %>%
  filter(manufacturer %in% c("chevrolet", "ford", "honda"))
mean(df$hwy)
count(df)
str(mpg)
mpg$manufacturer

# 4) class와 cty 변수로만 이루어진 데이터 프레임을 생성.
# class가 "suv"인 자동차와 "compact"인 자동차 중
# 어떤 클래스가 cty 평균이 더 높은지.
df_cls_cty <- mpg %>% select(class, cty)

df_suv <- df_cls_cty %>% filter(class == "suv")
mean(df_suv$cty)

df_compact <- df_cls_cty %>% filter(class == "compact")
mean(df_compact$cty)

names <- c("a", "a", "b", "b", "b", "c", "c")
names
names == "a"
names == c("a", "b")
mpg$manufacturer == c("ford", "honda")

numbers <- 1:10
numbers + c(1, 2)

