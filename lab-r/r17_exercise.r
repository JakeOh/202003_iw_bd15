# ggplot2::midwest 데이터 프레임 - 미국 중서부 지역의 인구 통계.
?midwest

# 데이터 프레임을 전역 변수로 복사.
midwest <- as.data.frame(ggplot2::midwest)
str(midwest)
head(midwest)

# Q1) poptotal: 전체 인구, popadults: 성인 인구
# midwest 데이터에 '전체 인구 대비 미성년 인구 백분율' 변수 추가.
# midwest$perc_child = ...
midwest <- midwest %>% 
  mutate(perc_child = (poptotal - popadults) / poptotal * 100)
midwest %>% 
  select(county, perc_child) %>% 
  head()

# Q2) 미성년 인구 비율이 가장 높은 상위 5개 county의 이름과
# 미성년 인구 백분율을 출력
midwest %>% 
  arrange(desc(perc_child)) %>% 
  head(n = 5) %>% 
  select(county, perc_child)

# Q3) 아래와 같은 기준의 grade 변수를 추가.
# 미성년 비율    | 등급(grade) 
#  40% 이상      | large
#  30 ~ 40% 미만 | middle
#  30% 미만      | small
# 각 등급의 지역 숫자(빈도수)를 출력
# midwest$grade = ...
midwest <- midwest %>% 
  mutate(grade = ifelse(perc_child >= 40, "large", 
                        ifelse(perc_child >= 30, "middle", 
                               "small")))
midwest %>% 
  select(county, perc_child, grade) %>% 
  head(n = 10)
midwest %>% 
  group_by(grade) %>% 
  summarise(cnt = n())

table(midwest$grade)

# Q4) popasian - 아시아 인구수
# midwest에 '전체 인구 대비 아시아 인구 백분율' 변수를 추가.
# 아시아 인구 비율 하위 10개 지역의 state, county,
# 아시아 인구 비율을 출력
# midwest$percasian
# midwest$perc_asian = ...
midwest %>% 
  mutate(perc_asian = popasian / poptotal * 100)
midwest %>% 
  arrange(perc_asian) %>% 
  head(n = 10) %>% 
  select(state, county, perc_asian, percasian)
