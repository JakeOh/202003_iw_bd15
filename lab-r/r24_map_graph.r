# 지도 위에 통계 데이터 보여주기

# ggplot2::map_data() 함수가 지도 데이터를 처리하기 위해서
install.packages("maps")
# ggplot2::coord_map() 함수가 사용하는 패키지
install.packages("mapproj")

library(tidyverse)

asia_map <- map_data(map = "world",  # 지도 종류
                     region = c("North Korea",  # 지도에서 선택할
                                "South Korea",  # 지역 리스트
                                "Japan",
                                "China",
                                "India"))
str(asia_map)
# longitude(경도): 영국 그리니치 천문대를 기준으로 동/서 방향 좌표.
# latitude(위도): 적도를 기준으로 남/북 방향 좌표.
# group: 함께 연결할 위도/경도 점들의 그룹(나라, 주, 도시, ...).
# order: 위/경도 점들을 선으로 연결할 순서.
# region: 지역 이름.

table(asia_map$group)
table(asia_map$region)

head(asia_map)
tail(asia_map)

ggplot(data = asia_map) +
  geom_polygon(mapping = aes(x = long,
                             y = lat,
                             group = group,
                             fill = region)) +
  coord_map("polyconic")


# 우리 나라 지도
korea_map <- map_data(map = "world",
                      region = c("South Korea" ,"North Korea"))
head(korea_map)
tail(korea_map)
table(korea_map$group)
table(korea_map$subregion)

# 테두리선 검은색, 채움색 없이 지도 작성
ggplot(data = korea_map) +
  geom_polygon(mapping = aes(x = long, y = lat, group = group),
               color = "black", fill = NA) +
  coord_map()


# 미국 지도
us_map <- map_data(map = "state")
head(us_map)
tail(us_map)
table(us_map$region)
table(us_map$subregion)

ggplot(data = us_map) +
  geom_polygon(mapping = aes(x = long, y = lat, group = group),
               color = "black", fill = NA) +
  coord_map()

# 미국 주별 범죄율 그래프
str(USArrests)  # 4개 변수(3개 강력범죄 + 인구수)
head(USArrests) # 주 이름들이 데이터 프레임의 행 이름으로 설정.

# 지도 데이터와 합치기 위해서 주 이름이 필요하므로,
# 주 이름들을 USArrests 데이터 프레임의 컬럼으로 생성.
us_crime <- rownames_to_column(USArrests, var = "state")
head(us_crime)

# 지도 데이터의 주 이름은 모두 소문자, 
# 범죄 데이터의 주 이름은 대문자가 포함되어 있음.
table(us_map$region)
us_crime$state

# 범죄 데이터의 주 이름들을 모두 소문자로 변환
us_crime$state <- tolower(us_crime$state)
us_crime$state
# toupper(): 모든 영문자를 대문자로 변환
# 영문자 문자열 비교를 할 때는 모두 대문자 또는 모두 소문자로
# 변환 후에 비교하는 것이 좋을 때가 있음.

# 주별 살인 범죄율
# 지도 데이터와 범죄 데이터를 join
# join의 기준: 지도 - region 변수, 범죄 - state 변수
us_map_crime <- left_join(us_map, us_crime,
                          by = c("region" = "state"))
head(us_map_crime)
tail(us_map_crime)

ggplot(data = us_map_crime) +
  geom_polygon(mapping = aes(x = long, y = lat, 
                             group = group, fill = Murder),
               color = "black") +
  coord_map("polyconic") +
  scale_fill_continuous(low = "white", high = "darkred")

  
# 단계 구분도(choropleth map)
# 지도 위에 통계 값들을 색깔 등으로 구분해서 표현한 그래프.
# 인구, 질병, 범죄, ...
# ggiraphExtra 패키지: 단계 구분도를 쉽게 그릴 수 있는 패키지.
install.packages("ggiraphExtra")
library(ggiraphExtra)
search()

ggChoropleth(data = us_crime,
             mapping = aes(fill = Murder,
                           map_id = state),
             map = us_map,
             interactive = TRUE)
# ggChoropleth() 함수의 arguments:
# data = 통계값이 들어있는 데이터 프레임(미국 주별 범죄율)
# map = 지도(위도, 경도, 그룹, 순서, ...) 데이터 프레임.
# mapping = aes()
#   map_id = data와 map을 join할 수 있는 data의 변수 이름.
#            map의 region과 동일한 정보를 가지고 있는 변수 이름.
#   fill = 지도의 각 그룹을 색깔로 채우기 위한 변수.


# Kormaps 패키지 설치
# CRAN(Central R Archive Network)에 등록되어 있지 않음.
# github(소스 코드 저장소)에만 있음.
# github의 오픈 소스 패키지를 설치하기 위해서 
# Rtools.exe, devtools 패키지가 필요.
# https://cran.r-project.org/bin/windows/Rtools/에서 다운로드
install.packages("devtools")
# library(devtools)
# install_github("cardiomoon/Kormaps")
devtools::install_github("cardiomoon/kormaps2014")

# 필요한 라이브러리(패키지)를 검색 경로에 추가
library(tidyverse)
library(kormaps2014)
search()

# 지도 데이터: kormap1(시/도), kormap2(시/군/구), kormap3(읍/면/동)
# 인구 데이터: korpop1, korpop2, korpop3
str(kormap1)
ggplot(data = kormap1) +
  geom_polygon(mapping = aes(x = long, y = lat, 
                             group = group),
               color = "black", fill = NA) +
  coord_map()

str(kormap2)
ggplot(data = kormap2) +
  geom_polygon(mapping = aes(x = long, y = lat, 
                             group = group),
               color = "black", fill = NA) +
  coord_map()

# 인구 데이터 확인
str(korpop1)
# 에러 발생 - 컬럼 이름에 포함된 한글 때문에
# kormap2014::changeCode() 함수:
# 데이터 프레임의 컬럼 이름에 한글이 있을 때, 제대로 표현.
str(changeCode(korpop1))

# 데이터 프레임의 변수들 중에서 필요한 변수의 이름만
# 영어로 변경
korpop1 <- korpop1 %>% 
  rename(pop = 총인구_명, name = 행정구역별_읍면동)
korpop1$name
kormap1$name

kor_map_pop <- left_join(kormap1, korpop1,
                         by = "name")
kor_map_pop %>% 
  select(name, pop) %>% head()
  
ggplot(data = kor_map_pop) +
  geom_polygon(mapping = aes(x = long, y = lat,
                             group = group, fill = pop)) +
  coord_map() +
  scale_fill_continuous(low = "white", high = "darkred")


library(ggiraphExtra)
search()

kor_map <- changeCode(kormap1)
str(kormap1)
ggChoropleth(data = korpop1, # 인구 통계 데이터
             map = kor_map1,  # 지도 데이터
             mapping = aes(fill = pop,  # 채우는 색깔 
                           map_id = code, # data와 map을 join
                           tooltip = name),  
             interactive = TRUE)

