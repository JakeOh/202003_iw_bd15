# 연속형 변수 요약
# data/salary_data.csv 파일 읽어서 데이터 프레임 생성
salary <- read.csv("data/salary_data.csv")
head(salary)
str(salary)

# 1) 정렬하기 -> min, max, quantile(4분위수)
# 소득 하위 70%에 해당하는 소득이 얼마인지 찾아보세요.
summary(salary)
boxplot(salary$salary)
max(salary$salary)
quantile(salary$salary, seq(0, 1, 0.25))
quantile(salary$salary, 0.7)

# dplyr 패키지의 전처리 함수들을 이용해서
# 1) 하위 소득 70% 이하 소득자들의 숫자는 7000명명
library(tidyverse)
salary %>% 
  filter(salary <= quantile(salary, 0.7)) %>% 
  summarise(pop = n())
# 2) 중위 소득의 150% 이하 소득자들의 숫자?
salary %>% 
  filter(salary <= quantile(salary, 0.5) * 1.5) %>% 
  summarise(pop = n())

# salary의 히스토그램을 그려보세요.
# hist()
# geom_histogram()

# 평균, 분산, 표준편차 계산
# salary를 표준화(standardization)하고,
# 표준화된 변수들의 평균은 0, 표준편차는 1임을 확인하세요.
m <- mean(salary$salary)
m
variance <- var(salary$salary)
variance
std_dev <- sd(salary$salary)
std_dev

# salary 표준화
salary_std <- (salary$salary - m) / std_dev
head(salary_std)
tail(salary_std)
mean(salary_std)
sd(salary_std)

df <- data.frame(v1 = 1:5,
                 v2 = 6:10)
df
quantile(df$v1, seq(0, 1, 0.25))
quantile(df, seq(0, 1, 0.25), na.rm = TRUE)


# 범주형 변수 요약
treat_org <- read.csv(file = "data/treat.csv",
                      fileEncoding = "euc-kr")
str(treat_org)
# DSBJT: 진료과, MAIN_SICK: 증상(질병) 코드

summary(treat_org)
head(treat_org)

treat <- treat_org  # 데이터 프레임 복사

# 월별 환자수
class(treat$MONTH)  # 변수 데이터 타입 - integer(정수)
# 정수 데이터(연속형 변수)를 범주형 변수로 변환
treat$MONTH <- factor(treat$MONTH)
class(treat$MONTH)  # factor
levels(treat$MONTH)  # 12개 레벨

t <- table(treat$MONTH)
t
barplot(t)  # 변수의 도수분포표(table)를 argument로 줌.
pie(t)

library(tidyverse)
ggplot(data = treat) +
  geom_bar(mapping = aes(x = MONTH))

ggplot(data = treat) +
  geom_bar(mapping = aes(x = MONTH, fill = MONTH)) +
  coord_polar()

# 성별
class(treat$SEX)
table(treat$SEX)

# SEX 변수를 범주형 변수로 변환
treat$SEX <- factor(treat$SEX)
class(treat$SEX)
levels(treat$SEX) <- c("남자", "여자")
levels(treat$SEX)
table(treat$SEX)

head(treat)
str(treat)

# AGE, DSBJT, MAIN_SICK 범주형 변수들의 table, plot
table(treat$AGE)
ggplot(data = treat) +
  geom_bar(mapping = aes(x = AGE))

table(treat$DSBJT)
ggplot(data = treat) +
  geom_bar(mapping = aes(x = DSBJT))

table(treat$MAIN_SICK)
ggplot(data = treat) +
  geom_bar(mapping = aes(x = MAIN_SICK))

# MAIN_SICK 환자수 상위 10개의 막대 그래프를 내림차순 정렬
treat %>% 
  group_by(MAIN_SICK) %>%  # MAIN_SICK 변수별로 그룹핑
  summarise(n = n()) %>%   # 각 질병 코드의 환자수를 셈
  arrange(desc(n)) %>%     # 환자수의 내림차순으로 정렬
  head(10) %>%             # 상위 10개 질병 코드
  ggplot() + geom_col(mapping = aes(x = reorder(MAIN_SICK, -n), 
                                    y = n))
  



