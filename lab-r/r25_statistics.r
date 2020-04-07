library(tidyverse)

# 통계 - 데이터
# 정형 데이터 - 행(observation)/열(variable)
patients <- data.frame(id = 1:3,
                       gender = c("m", "f", "m"),
                       date = c("2019-12-03", NA, "2020-03-31"),
                       weight = c(68, 55, 89))
patients

# 변수
# 1) 연속형(continuous) 변수
# 2) 범주형(categorical) 변수

# 연속형 변수 요약하기:
# 1) 순서대로 세우기 - 최솟값, 최댓값, 분위수
#    min(), max(), median(), quantile()
#    boxplot(상자 그림), histogram

runif(n = 5, min = 0, max = 10)  # random number uniform distribution
round(runif(n = 5, min = 0, max = 10))

score <- round(runif(n = 11, min = 50, max = 100))
score
sort(score)  # 정렬해서 보여주기
min(score)
max(score)
summary(score)
quantile(score, seq(0, 1, 0.25))  # 4분위수 찾기
quantile(score, seq(0, 1, 0.1))  # 10분위수

score2 <- round(runif(n = 10, min = 50, max = 100))
score2
sort(score2)
quantile(score2, seq(0, 1, 0.25))

boxplot(score2)
hist(score2, breaks = seq(50, 100, 5))

# 연속형 변수 요약하기:
# 2) 평균(mean)
v1 <- c(7500, 8000, 10000, 11000, 13500)
mean(v1)
v2 <- c(9000, 9500, 10000, 10500, 11000)
mean(v2)

# 3) 분산(variance):
# 평균에 숨어 있는 불합리함을 해결하기 위해서.
# 각 관측값들이 평균에서 얼마나 떨어져 있는지를 계산. (거리)
v1 - mean(v1)
v2 - mean(v2)
sum((v2 - mean(v2)) ** 2) / 4
var(v2)
var(v1)

# 4) 표준편차(standard deviation)
# 분산을 계산하면 숫자가 너무 커지고, 단위가 제곱이 되는 
# 문제가 발생 -> 분산의 제곱근(squared root)을 계산
sd(v1)
sd(v2)

# 5) 평균과 표준편차만으로는 그룹 간의 비교가 힘듦.
# -> 표준화(standardiztion)
#    (1) 중심화(centering): 각 관측치에서 평균을 뺌.
#    (2) 척도화(scaling): 관측치에서 평균을 뺀 값을 표준편차로 나눔.
# 표준화된 데이터는 평균이 0이 되고, 표준편차는 1이 됨.
v1_std <- (v1 - mean(v1)) / sd(v1)  # v1 표준 점수
v2_std <- (v2 - mean(v2)) / sd(v2)  # v2 표준 점수
v1_std
v2_std
mean(v1_std)
sd(v1_std)
mean(v2_std)
sd(v2_std)

# 범주형 데이터 요약하기:
# 각 수준(level)별로 몇 개의 관측치가 있는지 개수를 셈 & 비율 계산.
# 막대 그래프(bar plot), 파이 차트(pie chart)
# table(): 빈도수, prop.table(): 비율
gender <- c("m", "f", "f", "m", "m")
table(gender)
prop.table(table(gender))
qplot(gender)


# 확률
# 이론적 확률: 이상적인(ideal) 상황의 확률
#   (예) 동전 앞/뒷면 확률: 1/2, 주사위 눈 확률: 1/6
# 실험적 확률: 실험을 통해서 측정한 확률

# 사고 실험
coins <- round(runif(n = 10000))
table(coins)
prop.table(table(coins))

# 기댓값(expectation value):
# 확률을 고려했을 때 평균적으로 나올 수 있을 것 같은 값.
# 동전 앞(0), 뒤(1)
# 동전 한개를 던졌을 때 기댓값 (0 * 1/2 + 1 * 1/2) = 0.5
# 주사위 한개를 던졌을 때 기댓값.
sum(1:6 * 1/6)

# 동전을 던졌을 때의 기댓값 사고 실험.
coin_value = c(0, 1)
coins <- round(runif(1000))
coin_prop <- prop.table(table(coins))
coin_prop
e <- sum(coin_value * coin_prop)
e








