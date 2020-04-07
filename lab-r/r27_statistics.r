# 변수 간의 관계
# 관심 변수:데이터의 여러 변수들 중에서 차이를 확인하고 설명하려는 변수.
# 설명 변수:관심 변수의 차이를 설명해줄 수 있는 변수
# (예) 연비 ~ 배기량, 키 ~ 유전, 가격 ~ cut, 성격 ~ 혈액형

library(tidyverse)

# 두 연속형 변수들 사이의 상관 관계 - 공분산, 상관 계수
students <- read.csv(file = "data/studentlist.csv",
                     fileEncoding = "utf-8")
head(students)
str(students)
summary(students)

# height(키) - 관심 변수(종속 변수), 단위(cm)
# weight(몸무게) - 설명 변수(독립 변수), 단위(kg)
# height ~ weight
# 산점도 그래프(scatter plot)를 그려서, 두 변수의 관계 대략 파악
library(tidyverse)
ggplot(data = students) +
  geom_point(mapping = aes(x = weight, y = height)) +
  geom_vline(xintercept = mean(students$weight), color = "blue") +
  geom_hline(yintercept = mean(students$height), color = "blue")

# 1사분면: 키, 몸무게 모두 평균 이상
# 2사분면: 키는 평균 이상, 몸무게 평균 이하
# 3사분면: 키, 몸무게 모두 평균 이하
# 4사분면: 키 평균 이하, 몸무게 평균 이상
# 1,3사분면이 다른 평면보다 데이터가 많다면, 양의 상관 관계
# 2,4사분면이 다른 평면보다 데이터가 많다면, 음의 상관 관계
# 모든 데이터들이 두 변수의 평균과 얼마나 떨어져 있는 지의 평균
# -> 공분산(covariance): 두 변수를 함께 사용한 분산
# covariance = sum_i_to_n[(x_i - x_bar)*(y_i - y_bar)]/(n-1)
# 공분산의 부호를 보면, 양의 상관관계인 지, 음의 상관관계인 지 알 수 있음.
# 공분산의 크기(절대값)로 상관관계의 크기를 정의할 수 있을까?
# 공분산에는 단위가 포함되기 때문에 숫자 크기의 비교가 의미가 없다.
# 키와 몸무게의 상관관계에서 공분산은 cm * kg 단위
# 또는 m * kg 등 어떤 단위를 쓰느냐에 따라서 결과가 달라짐.

n <- NROW(students)  # observation 개수
h <- students$height  # height
w <- students$weight  # weight
h_bar <- mean(students$height)  # height의 평균(cm)
w_bar <- mean(students$weight)  # weight의 평균(kg)
covarianc <- sum((h - h_bar) * (w - w_bar)) / (n - 1)

cov(h, w)      # cm * kg
cov(h/100, w)  # m * kg

# 공분산의 문제를 해결하기 위해서
# 표준화(평균 0, 표준편차 1)된 변수들의 공분산을 계산
# -> 상관계수(correlation coefficient)
# correlation = covariance(x, y) / (sd(x) * sd(y))
# -1 <= correlation <= 1
# 상관계수가 0이면, 아무 상관이 없다.
# 상관계수가 +/-1에 가까울 수록 강한 양/음의 상관관계가 있다.

correlation <- cov(h, w) / (sd(h) * sd(w))
cor(h, w)

# ggplot2::mpg 데이터 프레임에서
# 산점도 그래프
# 연비(hwy)와 배기량(displ)의 공분산, 상관계수
# 직접 계산, 함수 이용
ggplot(data = mpg, mapping = aes(x = displ, y = hwy)) +
  geom_point() +
  geom_vline(xintercept = mean(mpg$displ), color = "darkgray") +
  geom_hline(yintercept = mean(mpg$hwy), color = "darkgray") +
  geom_smooth(method = "lm", formula = y ~ x)

cov(mpg$hwy, mpg$displ)
cor(mpg$hwy, mpg$displ)


# 두 범주형 변수의 관계
head(students)
# 성별(sex)
table(students$sex)
addmargins(table(students$sex))

prop.table(table(students$sex))
addmargins(prop.table(table(students$sex)))

# 혈액형(bloodtype)
tbl_blood <- table(students$bloodtype)
tbl_blood
addmargins(tbl_blood)

prop.table(tbl_blood)
addmargins(prop.table(tbl_blood))

# 성별 혈액형 차이/관계
tbl_sex_blood <- table(students$sex, students$bloodtype)
tbl_sex_blood  # 분할표(contingency table), 교차표(cross table)
addmargins(tbl_sex_blood)
addmargins(tbl_sex_blood, margin = 1)
# margin = 1: 같은 변수(컬럼)별 합계를 "row"로 추가

addmargins(tbl_sex_blood, margin = 2)
# margin = 2: 같은 관측치(행)별 합계를 "column"에 추가

ptbl_sex_blood <- prop.table(tbl_sex_blood)
ptbl_sex_blood
addmargins(ptbl_sex_blood)

prop.table(tbl_sex_blood, margin = 1)
# prop.table() 함수의 margin = 1 argument -> 행(row) 백분율
# 같은 행(row) 안에서 각 변수들의 비율

prop.table(tbl_sex_blood, margin = 2)
# prop.table() 함수의 margin = 2 argument -> 열(column) 백분율
# 같은 컬럼(column) 안에서 각 변수들의 비율


# 건강보험 데이터 프레임 treat
treat_org <- read.csv(file = "data/treat.csv")
head(treat_org)

treat <- treat_org  # 전처리하기 전에 데이터 프레임을 복사
str(treat)

treat$MONTH <- factor(treat$MONTH)
class(treat$MONTH)
levels(treat$MONTH)

treat$SEX <- factor(treat$SEX)
class(treat$SEX)
levels(treat$SEX) <- c("male", "female")
levels(treat$SEX)

# 나이 ~ 성별 table, prop.table - 백분율, 행/열 백분율
tbl_age_sex <- table(treat$AGE, treat$SEX)
tbl_age_sex
addmargins(tbl_age_sex)

prop.table(tbl_age_sex)
addmargins(prop.table(tbl_age_sex))

prop.table(tbl_age_sex, margin = 1)
# row 백분율 - 같은 나이 대에서의 성비

prop.table(tbl_age_sex, margin = 2)
addmargins(prop.table(tbl_age_sex, margin = 2), margin = 1)
# column 백분율 - 같은 성별에서 나이대의 비율

# 진료과목 ~ 성별 table, prop.table - 백분율, 행/열 백분율
tbl_dsbjt_sex <- table(treat$DSBJT, treat$SEX)
tbl_dsbjt_sex
addmargins(tbl_dsbjt_sex)

# 같은 진료 과목 내에서의 환자들의 성비
row_prop <- round(prop.table(tbl_dsbjt_sex, margin = 1), 
                  digits = 2)
row_prop
addmargins(row_prop, margin = 2)

# 같은 성별에서 각 진료과목별 환자 비율
col_prop <- prop.table(tbl_dsbjt_sex, margin = 2)
col_prop
addmargins(col_prop, margin = 1)
round(addmargins(col_prop, margin = 1), digits = 2)


# heights.csv 파일을 읽어서 데이터 프레임
heights <- read.csv("data/heights.csv")
str(heights)
head(heights)

# 각 변수의 요약
summary(heights)
boxplot(heights)
ggplot(data = heights) +
  geom_boxplot(mapping = aes(x = "father", y = father)) +
  geom_boxplot(mapping = aes(x = "son", y = son)) +
  ylab("height")

# 산점도 그래프 - vline, hline, smooth(method="lm")
# son ~ father
ggplot(data = heights, mapping = aes(x = father, y = son)) +
  geom_point() +
  geom_smooth(formula = y ~ x, method = "lm") +
  geom_vline(xintercept = mean(heights$father), color="green") +
  geom_hline(yintercept = mean(heights$son), color="green")

# 공분산, 상관계수 계산
cov(heights$father, heights$son)
cor(heights$father, heights$son)

# 전체 son의 숫자
n = NROW(heights)  # 1,078명

# son들 중에서 평균보다 키가 큰 son들의 비율
# -> son이 평균보다 키가 클 확률
n_taller <- heights %>% 
  filter(son > mean(son)) %>% 
  NROW()

p1 <- n_taller / n
p1  # 48.9%

# 아들의 키가 180 이상인 아들들의 비율
# -> 아들의 키가 180 이상이 될 확률
ggplot(data = heights, mapping = aes(x = father, y = son)) +
  geom_point() +
  geom_smooth(formula = y ~ x, method = "lm") +
  geom_vline(xintercept = mean(heights$father), color="green") +
  geom_hline(yintercept = mean(heights$son), color="green") +
  geom_hline(yintercept = 180, color="red")

n_ge180 <- heights %>% 
  filter(son >= 180) %>% NROW()
n_ge180  # greater than or equal to 180
n_ge180 / n  # 22.2%

# 아버지 키가 평균 이상인 경우, 아들의 키가 180이상인 비율
# 키가 평균 이상인 아버지 숫자
n_father <- heights %>% 
  filter(father > mean(father)) %>% NROW()
n_father
# 아버지 키가 평균 이상 & 180 이상인 아들들의 숫자
n_son <- heights %>% 
  filter(father >= mean(father) & son >=180) %>% NROW()
n_son
n_son / n_father  # 35.6%

# 조건부 확률 P(A|B):
# 사건 B가 일어났을 때, 사건 A가 일어날 확률
# P(A|B) = P(A & B) / P(B)

# Titanic 표를 보면서
# 1) 생존자 비율 - 생존 확률 = (생존자)/(전체 탑승자)
p1 <- 711 / (1490 + 711)  # 32.3%

# 2) 남자의 생존율 - 남자 중에서 생존한 비율
# (남자 생존자 숫자)/(남자 숫자)
p2 <- (29 + 338) / (35 + 1329 + 29 + 338)  # 21.2%
# 3) 여자의 생존율 - 여자 중에서 생존한 비율
# (여자 생존자 숫자)/(여자 숫자)
p3 <- (28 + 316) / (17 + 109 + 28 + 316)  # 73.2%
  
# 4) 아이의 생존율 = (아이 생존자 숫자) / (아이 숫자)
p4 <- 57 / (52 + 57)  # 52%
# 5) 성인의 생존율 = (성인 생존자 숫자) / (성인 숫자)
p5 <- 654 / (1438 + 654)  # 31%

# 6) 3등석 탑승자의 생존율 
# (3등석 생존자 숫자) / (3등석 탑승자 숫자) = 25%
p6 <- (13+14+75+76) / (35+17+387+89+13+14+75+76)
# 7) 3등석이 아닌 탑승자(1, 2, 선원)의 생존율 
# (1,2,선원 생존자 숫자) / (1,2,선원의 전체 숫자) = 36%
p7 <- (5+1+57+140+11+13+14+80+192+20)/(118+4+154+13+670+3+5+1+57+140+11+13+14+80+192+20)

# 8) 여자 & 3등석 승객의 생존 비율
# (여자 3등석 생존자 숫자)/(여자 3등석 탑승자 숫자)
p8 <- (14+76)/(17+89+14+76)  # 46%
# 9) 여자 & 3등석이 아닌 승객 생존 비율
#(여자 & 3등석이 아닌 생존자 숫자)/(여자 & 3등석이 아닌 승객)
p9 <- (1+140+13+80+20)/(4+13+3+1+140+13+80+20)  # 93%








