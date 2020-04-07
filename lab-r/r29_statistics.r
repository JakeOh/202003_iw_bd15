# call_chicken.csv 파일을 읽어서, 데이터 프레임을 생성
call_chicken <- read.csv(file = "data/call_chicken.csv")

# 데이터 프레임 대략적인 구조 파악
str(call_chicken)
head(call_chicken)
tail(call_chicken)

# 변수 이름들을 영문으로 변경
library(tidyverse)
search()
call_chicken <- rename(call_chicken,
                       date = 기준일, weekday = 요일,
                       gu = 시군구, ages = 연령대,
                       gender = 성별, calls = 통화건수)
tail(call_chicken)

boxplot(call_chicken$calls)
# 구(gu)별 통화건수(calls)의 boxplot
g <- ggplot(data = call_chicken, mapping = aes(y =calls))
g + geom_boxplot(mapping = aes(x = gu))

# 성별(gender)별 통화건수(calls)의 boxplot
g + geom_boxplot(mapping = aes(x = gender))

# 연령대(ages)별 통화건수(calls)의 boxplot
g + geom_boxplot(mapping = aes(x = ages))

# 요일(weekday)별 통화건수(calls)의 boxplot
g + geom_boxplot(mapping = aes(x = weekday))

# 통화건수(calls)의 최솟값/최댓값에 해당하는 observation을 출력
call_chicken %>% 
  filter(calls == min(calls) | calls == max(calls))

# recursive partition & regression tree
# install.packages("rpart.plot")
library(rpart.plot)
search()

rp_call <- rpart(formula = calls ~ weekday + ages,
                 data = call_chicken)
rp_call

rpart.plot(rp_call)

# 가장 오른쪽 leaf(terminal node)의 yval = 122.465
call_chicken %>% 
  filter(ages %in% c("30대", "40대") & 
           weekday %in% c("금", "토", "일")) %>% 
  summarise(mean(calls))

# deviance = 오차들의 제곱의 합
#          = sum [(측정값 - 예측값) ** 2]
y_real <- call_chicken$calls  # 측정값
y_pred <- mean(call_chicken$calls)  # 예측값

deviance_call <- sum((y_real - y_pred) ** 2)
deviance_call


rp_call <- rpart(formula = calls ~ weekday + gu + ages + gender,
                 data = call_chicken)
rp_call
rpart.plot(rp_call, cex = 0.5)

# datasets::iris 데이터 프레임
?iris
str(iris)
head(iris)
tail(iris)
# 산점도 그래프(scatter plot)
# Sepal.Length ~ Sepal.Width, color = Species
ggplot(data = iris) + 
  geom_point(mapping = aes(x = Sepal.Length, y = Sepal.Width,
                           color = Species),
             size = 3)
# Petal.Length ~ Petal.Width, color = Species
ggplot(data = iris) + 
  geom_point(mapping = aes(x = Petal.Length, y = Petal.Width,
                           color = Species),
             size = 3)
# 품종(Species) 별 Petal.Length의 boxplot
ggplot(data = iris) +
  geom_boxplot(mapping = aes(x = Species, y = Petal.Length))

# rpart, rpart.plot 사용해서 regression tree 작성
rp_iris <- rpart(formula = Species ~ Sepal.Length + Sepal.Width + Petal.Length + Petal.Width,
                 data = iris)
rp_iris
rpart.plot(rp_iris)

# ggplot2::mpg 데이터 프레임에서
# hwy ~ displ + drv + class (reression tree 작성)
rp_mpg <- rpart(formula = hwy ~ displ + drv + class,
                data = mpg)
rp_mpg
rpart.plot(rp_mpg)

# 상관관계(Correlation) 그래프
plot(iris)

cor(iris$Petal.Length, iris$Petal.Width)  # 상관계수
correlations <- cor(iris[1:4])  # Species 변수 제외(숫자가 아니기 때문에)

# correlation plot 그려주는 패키지
install.packages("corrplot")
library(corrplot)

corrplot(correlations)
corrplot(correlations, method = "color")
corrplot(correlations, method = "number")

install.packages("psych")
library(psych)

pairs.panels(iris[1:4])
