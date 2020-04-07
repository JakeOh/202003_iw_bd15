rm(list = ls())

# 데이터 프레임(data frame):
# 엑셀의 스프레드시트와 같은 표 형식의 데이터 구조.
# 행(row)과 열(column)을 갖는 2차원 구조.
# row = observation(관측치, 관찰값), sample(표본)
# column = variable(변수), attribute(속성)
# 같은 컬럼에는 같은 타입의 데이터만 저장.
# 데이터 분석에서 가장 많이 사용하는 데이터 구조.

english <- c(90, 60, 80, 70)  # 영어 점수
math <- c(50, 60, 100, 20)  # 수학 점수
class <- c(1, 1, 2, 2)  # 반(class)

midterm <- data.frame(eng = english,
                      math = math,
                      cls = class)
midterm

# 데이터 프레임에서 열(column)을 접근:
midterm$eng

midterm_noname <- data.frame(class, english, math)
midterm_noname

midterm2 <- data.frame(c(1, 1, 1, 1),
                       c(10, 20, 30, 40),
                       c(11, 21, 41, 51))
midterm2

# 데이터 프레임에 새로운 컬럼 추가
midterm
midterm$kor <- c(99, 88, 0, 77)
midterm

# 엑셀 파일 형식(xls, xlsx)의 파일 읽을 수 있는 패키지 설치
install.packages("readxl")
# 설치한 패키지를 사용하려면, 패키지를 검색 경로에 추가.
search()  # 검색 경로에 있는 패키지 이름들을 출력.
library(readxl)  # 검색 경로에 패키지 추가.

# data/excel_exam.xlsx 파일 읽어서 데이터 프레임 생성.
exam <- read_excel("data/excel_exam.xlsx")
exam

exam2 <- read_excel("data/excel_exam_novar.xlsx")
# read_excel() 함수는 엑셀 파일의 첫번째 행을
# 컬럼 이름으로 생각함.
# argument col_names의 기본값이 TRUE인데,
# col_names = FALSE로 설정하면, 첫번째 행을 데이터로 생각.
exam3 <- read_excel("data/excel_exam_novar.xlsx",
                    col_names = FALSE)
exam3

# 엑셀 파일에서 Sheet3에 있는 표를 데이터 프레임으로 생성.
exam4 <- read_excel("data/excel_exam_sheet.xlsx",
                    sheet = 3)  # sheet = "Sheet3"
exam4

# Global Environment(메모리)에 있는 데이터를
# RData 타입으로 저장 후 불러오는 방법:
# 데이터 프레임을 파일로 저장.
save(exam, file = "exam.rda")  
rm(list = ls())
# RDdata 파일에서 데이터 프레임을 로드.
load("exam.rda")

# CSV(Comma-Separated Values) 파일:
# 값(데이터)들이 쉼표(,), 공백( ), 탭 등으로 분리된 
# 텍스트 파일.
# CSV 파일에서 데이터 프레임 생성.
exam_csv <- read.csv(file = "data/csv_exam.csv")
exam_csv


