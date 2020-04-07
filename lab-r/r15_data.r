# 데이터 전처리(pre-processing) - dplyr 패키지
# filter(): 조건에 맞는 observation(행)을 추출.
# select(): 원하는 variables(변수들)을 선택.
# arrange(): 오름차순/내림차순 정렬.

exam <- read.csv(file = "data/csv_exam.csv")
exam

# arrange(데이터 프레임, 정렬 기준 컬럼)
# 데이터 프레임 %>% arrange(정렬 기준 컬럼)
arrange(exam, math)
exam %>% arrange(math)

# arrange의 기본 정렬 방식은 오름차순.
# 내림차순으로 보려면 desc(컬럼)을 사용 - descending
exam %>% arrange(desc(math))
exam %>% arrange(-math)

# 각 class에서 수학 점수를 기준으로 오름차순 정렬.
exam %>% arrange(class, math)

# 정렬 기준: 1) class 오름차순, 2) math 내림차순.
exam %>% arrange(class, desc(math))


# dplyr::mutate() - 파생 변수 생성.
# mutate(데이터 프레임, 파생 변수)
# 데이터 프레임 %>% mutate(파생 변수)
mutate(exam, total = math + english + science)
exam %>% mutate(total = math + english + science)
# mutate() 함수는 컬럼이 추가된 새로운 데이터 프레임을 리턴.

# 주의: 아래의 코드는 exam 데이터 프레임을 수정함.
exam$total <- exam$math + exam$english + exam$science

# rowSums(): 행 별로 합계 계산
rowSums(select(exam, math, english, science))
exam %>% 
  select(math, english, science) %>% 
  rowSums()

# rowMeans(): 행 별로 평균 계산
rowMeans(select(exam, math, english, science))
exam %>% 
  select(math, english, science) %>% 
  rowMeans()


# 총점(total), 평균(mean) 컬럼 2개를 추가.
exam %>% 
  mutate(total = math + english + science,
         mean = total / 3)


# ggplot2::mpg 데이터 프레임에서
# 1) audi에서 생산한 자동차를 추출
# 2) audi 자동차 중에서, hwy를 내림차순 정렬
# 3) audi 자동차 중에서, hwy 순위 5위까지만 출력
mpg <- as.data.frame(ggplot2::mpg)  # 복사본을 메모리에.
mpg %>% 
  filter(manufacturer == "audi") %>% 
  arrange(desc(hwy)) %>% 
  head(n = 5)

# exam 데이터 프레임에서 
# science가 50점 이상이면 "pass", 그렇지 않으면 "fail"
# 컬럼(result)를 추가
exam %>% 
  mutate(result = ifelse(science >= 50, "pass", "fail"))

# mpg 데이터 프레임에서
# 1) avg_mpg 변수를 추가 - hwy와 cty의 평균
# 2) result 변수를 추가 - 
# avg_mpg(평균 연비)가 25이상이면 Good, 그렇지 않으면 Bad
# 3) avg_mpg를 내림차순 정렬
# 4) avg_mpg 1 ~ 5위까지를 출력
mpg %>% 
  mutate(avg_mpg = (hwy + cty) / 2, 
         result = ifelse(avg_mpg >= 25, "Good", "Bad")) %>% 
  arrange(desc(avg_mpg)) %>% 
  head(n = 5)


# 그룹별 통계 처리: group_by() %>% summarize()
# 비교) summary()
summary(exam)

# exam 데이터 프레임에서 class별 수학 점수 평균 계산.
exam %>% 
  group_by(class) %>% 
  summarise(mean_math = mean(math))
# summarise() 함수 안에서 사용할 수 있는 통계 함수들:
# sum(): 합계
# mean(): 평균
# sd(): 표준편차(standard deviation)
# min(): 최솟값
# max(): 최댓값
# n(): 빈도수

# exam 데이터 프레임에서 class별 과학 점수의 최솟값/최댓값
exam %>% 
  group_by(class) %>% 
  summarise(min_sci = min(science), max_sci = max(science))

# mpg 데이터 프레임에서,
# 제조사(manufacturer)별, 구동방식(drv)별
# 도시연비(cty)의 평균을 계산, 해당 자동차 대수
mpg %>% 
  group_by(manufacturer, drv) %>% 
  summarise(mean_cty = mean(cty), n = n())

# mpg 데이터 프레임에서
# 제조사별 "suv" 자동차의 도시/고속도로 평균 연비를 계산 후
# 내림차순 정렬, 1 ~ 5위까지 출력.
mpg %>% 
  group_by(manufacturer) %>%  # 제조사별 그룹
  filter(class == "suv") %>%   # suv만 추출
  mutate(mean_mpg = (cty + hwy) / 2) %>%  # 파생변수 생성
  summarise(avg = mean(mean_mpg)) %>%  # 그룹별 계산
  arrange(desc(avg)) %>%   # 내림차순 정렬
  head(n = 5)

mpg %>% 
  filter(class == "suv") %>% 
  mutate(tot = (cty + hwy) / 2) %>% 
  group_by(manufacturer) %>% 
  summarise(avg = mean(tot)) %>% 
  arrange(desc(avg)) %>% 
  head(5)

# mpg 데이터 프레임에서
# Q1) class 별 도시 연비(cty)의 평균을 출력.
# Q2) 1번의 결과를 cty 평균이 높은 순으로 정렬해서 출력.
# Q3) 어떤 회사의 고속도로 연비(hwy)가 좋을까요? 1 ~ 5위 출력.
# Q4) 어떤 회사에서 "compact" 차종을 가장 많이 생산할까요?
# 회사별 compact 차종의 수를 내림차순으로 출력.
library(tidyverse)
mpg <- as.data.frame(ggplot2::mpg)
head(mpg)
tail(mpg)
# Q1)
mpg %>% 
  group_by(class) %>% 
  summarise(mean_cty = mean(cty))

# Q2)
mpg %>% 
  group_by(class) %>% 
  summarise(mean_cty = mean(cty)) %>% 
  arrange(desc(mean_cty))

# Q3)
mpg %>% 
  group_by(manufacturer) %>% 
  summarise(mean_hwy = mean(hwy)) %>% 
  arrange(desc(mean_hwy)) %>% 
  head(n = 5)

# Q4)
mpg %>% 
  filter(class == "compact") %>% 
  group_by(manufacturer) %>% 
  summarise(cnt = n()) %>% 
  arrange(desc(cnt))
