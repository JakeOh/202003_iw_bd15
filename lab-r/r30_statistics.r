rm(list = ls())
library(tidyverse)

df <- data.frame(type = rep(c("A", "B"), 3),
                 y = c(10, 11, 7, 17, 20, 21))
df

# 전체 y값의 평균
y_bar <- mean(df$y)

# deviance
# sum of squares
# 각 관측치들이 전체 평균과 얼마나 떨어져 있는 지의 정도 - 분산
ss1 <- sum((df$y - y_bar) ** 2)

# 그룹별 평균(type별 y의 평균)
grouped_mean <- df %>% 
  group_by(type) %>% 
  summarise(yg = mean(y))
grouped_mean

df <- left_join(df, grouped_mean, by = "type")
df

# (각각의 y - 해당 그룹 y평균)**2 들의 합
# 그룹 안에서의 개인들의 차이
ss2 <- sum((df$y - df$yg) ** 2)

# (해당 그룹 y평균 - 전체평균)**2 들의 합
# 그룹 안의 개인차는 무시하고 그룹 간의 차이
ss3 <- sum((df$yg - y_bar) ** 2)

# ss1 == ss2 + ss3
# sum [(y_i - ybar)**2] = sum [(y_i - yg)**2] + sum [(yg - ybar)**2]
# a**2 = b**2 + c**2

?InsectSprays  # datasets::InsectSpray
insect_sprays <- InsectSprays  # 데이터 복사
str(insect_sprays)
head(insect_sprays)
tail(insect_sprays)

# count ~ spray boxplot
ggplot(data = insect_sprays) +
  geom_boxplot(mapping = aes(x = spray, y = count))

# count의 전체 평균
count_bar <- mean(insect_sprays$count)

# count의 spray 타입 별 평균
grouped_mean <- insect_sprays %>% 
  group_by(spray) %>% 
  summarise(yg = mean(count))
grouped_mean

insect_sprays <- left_join(insect_sprays, grouped_mean, 
                           by = "spray")
head(insect_sprays, n = 10)
tail(insect_sprays)

# a**2 = b**2 + c**2 확인
a <- sum((insect_sprays$count - count_bar)**2)
b <- sum((insect_sprays$count - insect_sprays$yg)**2)
c <- sum((insect_sprays$yg - count_bar)**2)
b + c



