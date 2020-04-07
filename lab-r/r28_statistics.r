# 조건부 확률, Mosacit Plot, Decision Tree
?Titanic
Titanic  # 4-dimensional array
# 4-d array를 data.frame으로 변환
df_titanic <- as.data.frame(Titanic)
df_titanic

# 4-d array를 이용한 mosaic plot
mosaicplot(~ Class, data = Titanic)
mosaicplot(~ Class + Sex, data = Titanic)
mosaicplot(~ Class + Sex + Age, data = Titanic)
mosaicplot(~ Class + Sex + Age + Survived, 
           data = Titanic, color = TRUE)

mosaicplot(~ Age + Sex + Class + Survived,
           data = Titanic, color = TRUE)

# decision tree
df_titanic
# 전체 탑승객 숫자
n_total <- sum(df_titanic$Freq)
# 생존자 숫자
n_survived <- df_titanic %>% 
  filter(Survived == "Yes") %>% 
  summarise(sum(Freq))
n_survived / n_total

df_titanic %>% 
  filter(Class != "3rd") %>% 
  summarise(sum(Freq))

# 1) 성별(Sex)로 분할한 경우
# 남자인 경우 생존 비율
n <- df_titanic %>% 
  filter(Survived == "Yes" & Sex == "Male") %>% 
  summarise(sum(Freq))
N <- df_titanic %>% 
  filter(Sex == "Male") %>% 
  summarise(sum(Freq))
n/N  # 21%
# 여자인 경우 생존 비율
n <- df_titanic %>% 
  filter(Survived == "Yes" & Sex != "Male") %>% 
  summarise(sum(Freq))
N <- df_titanic %>% 
  filter(Sex != "Male") %>% 
  summarise(sum(Freq))
n/N  # 73%

# 2) 나이(Age)로 분할한 경우
# 아이인 경우 생존 비율
n <- df_titanic %>% 
  filter(Survived == "Yes" & Age != "Adult") %>% 
  summarise(sum(Freq))
N <- df_titanic %>% 
  filter(Age != "Adult") %>% 
  summarise(sum(Freq))
n/N  # 52%
# 성인인 경우 생존 비율
n <- df_titanic %>% 
  filter(Survived == "Yes" & Age == "Adult") %>% 
  summarise(sum(Freq))
N <- df_titanic %>% 
  filter(Age == "Adult") %>% 
  summarise(sum(Freq))
n/N  # 31%

# 3) 좌석등급(Class)로 분할한 경우
# 3등급인 경우 생존 비율
n <- df_titanic %>% 
  filter(Survived == "Yes" & Class == "3rd") %>% 
  summarise(sum(Freq))
N <- df_titanic %>% 
  filter(Class == "3rd") %>% 
  summarise(sum(Freq))
n/N  # 25%
# 3등급이 아닌 경우 생존 비율
n <- df_titanic %>% 
  filter(Survived == "Yes" & Class != "3rd") %>% 
  summarise(sum(Freq))
N <- df_titanic %>% 
  filter(Class != "3rd") %>% 
  summarise(sum(Freq))
n/N  # 35%

# 웹 서버에 저장된 CSV 파일을 다운로드하지 않고 직접
# 데이터 프레임으로 변환
# https://raw.githubusercontent.com/jbryer/CompStats/master/Data/titanic3.csv
titanic3 <- read.csv(url("https://raw.githubusercontent.com/jbryer/CompStats/master/Data/titanic3.csv"),
                     na.strings = "")
# read.csv() 함수의 na.strings = "" argument는
# csv 파일에 있는 빈 문자열("")을 NA로 처리함.
str(titanic3)

# titanic3$home.dest <- ifelse(titanic3$home.dest == "", NA,
#                              titanic3$home.dest)
# 빈 문자열("")을 NA로 처리하는 것은 이미 끝남.

head(titanic3)
summary(titanic3)

# pclass 변수를 categorical 변수로 변환(factor)
titanic3$pclass <- factor(titanic3$pclass)
class(titanic3$pclass)
levels(titanic3$pclass)
table(titanic3$pclass)

# survived 변수를 categorical 변수로 변환, 
# levels를 "no"(0), "yes"(1)로 지정.
titanic3$survived <- factor(titanic3$survived)
class(titanic3$survived)
levels(titanic3$survived) <- c("no", "yes")
levels(titanic3$survived)
table(titanic3$survived)

# mosaic plot
mosaicplot(~ sex + pclass + survived, data = titanic3,
           color = TRUE)

# titanic3 데이터 프레임에 adult 변수를 추가
# age <= 10 이하이면 "no", 그렇지 않으면 "yes"
titanic3 <- titanic3 %>% 
  mutate(adult = ifelse(age <= 10, "no", "yes"))

table(titanic3$adult)

# adult 변수를 포함한 mosaic plot
mosaicplot(~ sex + pclass + adult + survived,
           data = titanic3,
           color =TRUE)

# rpart 패키지: recursive partitioning & regression tree
# -> R을 설치할 때 포함되어 있음.
# rpart.plot 패키지: rpart의 내용을 tree로 시각화
install.packages("rpart.plot")
library(rpart.plot)
# rpart.plot을 로딩하면 rpart도 함께 로딩됨.
search()

titanic3$survived <- ifelse(titanic3$survived == "yes",
                            "survived", "dead")
table(titanic3$survived)

rp_titanic3 <- rpart(formula = survived ~ sex + adult + pclass,
                     data = titanic3)
rp_titanic3
rpart.plot(rp_titanic3)

# formula = survived ~ sex + adult + pclass + sibsp + parch
# formula = survived ~ sex + age + pclass + sibsp + parch





