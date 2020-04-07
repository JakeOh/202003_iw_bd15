# geom_bar(): 막대 그래프

# mpg$class의 빈도수.
table(mpg$class)

ggplot(data = mpg) +
  geom_bar(mapping = aes(x = class))

table(mpg$drv)
ggplot(data = mpg) +
  geom_bar(mapping = aes(x = drv), fill = "pink")
# geom_bar()의
#  color argument: 테두리 색깔
#  fill argument: 막대를 채우는 색깔

table(mpg$class, mpg$drv)
ggplot(data = mpg) +
  geom_bar(mapping = aes(x = class, fill = drv))

# geom_bar()의 position argument:
#  1) stack - 누적
#  2) dodge - 옆으로 나란히
#  3) fill - 비율
ggplot(data = mpg) +
  geom_bar(mapping = aes(x = class, fill = drv),
           position = position_dodge2(preserve = "single"))

ggplot(data = mpg) +
  geom_bar(mapping = aes(x = class, fill = drv),
           position = "fill") + 
  coord_flip()

?diamonds
# ggplot2::diamonds 데이터 프레임
head(diamonds)
str(diamonds)

# cut 변수의 빈도수
table(diamonds$cut)

# cut 변수의 막대 그래프
ggplot(data = diamonds) +
  geom_bar(mapping = aes(x = cut),
           fill = "pink", width = 0.5)

# cut 변수의 막대 그래프 + clarity 변수로 막대 색깔을 채움.
table(diamonds$clarity)
table(diamonds$cut, diamonds$clarity)

ggplot(data = diamonds) +
  geom_bar(mapping = aes(x = cut, fill = clarity))

# cut 변수의 막대 그래프 + clarity 변수로 비율.
ggplot(data = diamonds) +
  geom_bar(mapping = aes(y = cut, fill = clarity),
           position = "fill")

# table(): 빈도수(개수)
# prop.table(): 빈도수(개수)의 비율
table(diamonds$cut)
prop.table(table(diamonds$cut))

table(diamonds$cut, diamonds$clarity)
prop.table(table(diamonds$cut, diamonds$clarity))

# geom_col(): 데이터를 요약한 정보를 막대 그래프로 생성.
# bar 그래프와 다르게 x축과 y축 모두 변수를 mapping함!

# 자동차 종류(class)별 평균 고속도로 연비(hwy)
hwy_by_class <- mpg %>% 
  group_by(class) %>% 
  summarise(mean_hwy = mean(hwy))
hwy_by_class

ggplot(data = hwy_by_class) +
  geom_col(mapping = aes(x = class, y = mean_hwy))

# 자동차 구동방식(drv)별 평균 고속도로 연비(hwy)
hwy_by_drv <- mpg %>% 
  group_by(drv) %>% 
  summarise(mean_hwy = mean(hwy))
hwy_by_drv

ggplot(data = hwy_by_drv) +
  geom_col(mapping = aes(x = drv, y = mean_hwy))

# 막대를 내림/오름차순으로 정렬해서 보여주기.
# reorder(축에 사용할 변수, 정렬 기준 변수)
ggplot(data = hwy_by_drv) +
  geom_col(mapping = aes(x = reorder(drv, -mean_hwy), 
                         y = mean_hwy))

# 어떤 회사에서 생산한 SUV가 도시 연비가 좋은 지.
# SUV 차종의 평균 cty가 가장 높은 제조사 1 ~ 5위 col()
df <- mpg %>% 
  filter(class == "suv") %>%  # suv만 추출
  group_by(manufacturer) %>%  # 제조사별 그룹핑
  summarise(mean_cty = mean(cty)) %>%  # 평균 연비 계산
  arrange(desc(mean_cty)) %>%  # 내림차순 정렬
  head(n = 5)
df

ggplot(data = df) +
  geom_col(mapping = aes(x = reorder(manufacturer, -mean_cty), 
                         y = mean_cty))





  
  
  