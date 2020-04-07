# 인터랙티프 그래프(interactive graph)
install.packages("plotly")

# 패키지를 검색 경로에 추가
library(tidyverse)
library(plotly)
search()

# ggplot2::mpg 데이터 프레임에서
# 배기량(displ), 구동방식(drv), 고속도로연비(hwy) 간의 관계
g <- ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy, color = drv))

g

ggplotly(g)

# 구동방식(drv)별 고속도로연비(hwy) boxplot
g <- ggplot(data = mpg) +
  geom_boxplot(mapping = aes(x = drv, y = hwy))

ggplotly(g)


# ggplot2::diamonds 데이터 프레임에서
# cut 변수의 막대 그래프.
str(diamonds)
table(diamonds$cut)

g <- ggplot(data = diamonds) +
  geom_bar(mapping = aes(x = cut))

ggplotly(g)


# cut, clarity 변수의 막대 그래프
table(diamonds$cut, diamonds$clarity)

g <- ggplot(data = diamonds) +
  geom_bar(mapping = aes(x = cut, fill = clarity),
           position = "dodge")

ggplotly(g)

# economics 데이터 프레임에서 
# 시간(date)에 따른 개인저축률(psavert)의 시계열 그래프
g <- ggplot(data = economics) +
  geom_line(mapping = aes(x = date, y = psavert))

ggplotly(g)

# psavert가 최댓값인 date
economics %>% 
  filter(psavert == max(psavert, na.rm = TRUE)) %>% 
  select(date)

g


# dygraphs: 시계열 그래프인 경우 더 많은 기능을 가지고 있음.
install.packages("dygraphs")
library(xts)
library(dygraphs)
search()

eco_psavert <- xts(x = economics$psavert,  # 시계열 데이터
                   order.by = economics$date)  # 시간
str(eco_psavert)
dygraph(eco_psavert) %>% dyRangeSelector()


