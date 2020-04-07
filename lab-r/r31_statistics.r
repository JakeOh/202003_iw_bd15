rm(list = ls())
library(tidyverse)

# ggplot2::mpg 데이터 프레임에서
# compact 자동차와 suv 자동차의 연비 차이
mpg_df <- mpg %>% 
  filter(class %in% c("compact", "suv")) %>% 
  select(class, hwy)
head(mpg_df)
tail(mpg_df)

ggplot(data = mpg_df) +
  geom_boxplot(mapping = aes(x = class, y = hwy))

mpg_df %>% group_by(class) %>% summarise(mean(hwy))

# t-검정(T-test)
t.test(formula = hwy ~ class, data = mpg_df)

# 가설
# 영가설, 귀무가설(null hypothesis)
# 대립가설(alternative hypothesis)
# p-value: 대립가설이 우연히도 발생할 수 있는 확률
# 보통 p-value < 0.05 이면, 
# 대립가설이 우연히 발생할 확률이 작다는 의미이므로,
# 대립가설을 채택함(영가설을 기각)
# p-value > 0.05 이면,
# 대립가설이 우연히 발생할 확률이 크다는 의미이므로,
# 영가설을 기각할 수 없다.(영각설 채택)

x <- c(7.4, 1.4, 5.7, 2.5, 8.5, 9.7, 6.6, 9.3, 3.7, 7.8)
mean(x)

sample <- round(runif(n = 10, min = 0, max = 10), digits = 1)
sample
mean(sample)

# 표본(sample)들의 평균을 저장하기 위한 변수
samples <- c()
for (i in 1:10000) {
  samples[i] <- mean(runif(n = 10, min = 0, max = 10), digits = 1)
}
samples
hist(samples)


