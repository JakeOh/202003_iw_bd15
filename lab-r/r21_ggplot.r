install.packages("ggthemes")
library(ggthemes)
library(tidyverse)

# geom_line(): 선 그래프
# 시계열 데이터(시간에 따라 변하는 데이터)에서 자주 사용.
# 주식, 환율, 고용률/실업률

?economics
head(economics)
tail(economics)

ggplot(data = economics) +
  geom_line(mapping = aes(x = date, y = unemploy)) +
  theme_wsj()

# economics 데이터 프레임에서
# 1) 개인저축률(psavert) 시계열 그래프
ggplot(data = economics) +
  geom_line(mapping = aes(x = date, y = psavert)) +
  theme_economist()

# 2) 실업률(실업자수/전체인구) 시계열 그래프
economics <- as.data.frame(ggplot2::economics)

economics <- economics %>% 
  mutate(unemp_rate = (unemploy / pop) * 100)
# economics$unemp_rate <- (economics$unemploy / economics$pop) * 100

head(economics)

ggplot(data = economics) +
  geom_line(mapping = aes(x = date, y = unemp_rate))

ggplot(data = economics) +
  geom_line(mapping = aes(x = date,
                          y = (unemploy / pop) * 100)) +
  ylab("Unemployment Rate")
 
# 하나의 plot에 두개의 line 그래프
ggplot(data = economics, mapping = aes(x = date)) +
  geom_line(mapping = aes(y = psavert), 
            color = "red") +
  geom_line(mapping = aes(y = unemp_rate), 
            color = "blue")


# box plot: 기술 통계량을 요약해서 보여주는 그래프
summary(mpg)
b <- boxplot(mpg$hwy)
b
b$stats

# IQR(Inter-Quartile Range) = 3rd Qu. - 1st Qu.
IQR(mpg$hwy)

# ggplot2 패키지를 이용한 box plot
# 구동방식별 고속도로 연비의 box plot
ggplot(data = mpg) +
  geom_boxplot(mapping = aes(x = drv, y = hwy))

# 자동차 class별 cty의 box plot
ggplot(data = mpg) +
  geom_boxplot(mapping = aes(x = class, y = cty))


df_test <- data.frame(v1 = 1:3, v2 = 1:3 * 2, v3 = 1:3 * 3)
df_test
ggplot(data = df_test, mapping = aes(x = v1)) +
  geom_line(mapping = aes(y = v2), color = "red") +
  geom_line(mapping = aes(y = v3), color = "blue")

df_pivot <- df_test %>% 
  pivot_longer(cols = -v1,  # cols = c("v2", "v3")
               names_to = "kind", values_to = "rate")
df_pivot

ggplot(data = df_pivot) +
  geom_line(mapping = aes(x = v1, y = rate, 
                          color = kind))

economics %>% 
  mutate(unemp_rate = (unemploy / pop) * 100) %>% 
  select(date, psavert, unemp_rate) %>% 
  pivot_longer(-date) %>% 
  ggplot() + geom_line(mapping = aes(x = date, y = value,
                                     color = name))

  
  
  
  
