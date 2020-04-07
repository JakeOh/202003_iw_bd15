# rm() 함수: remove. 메모리의 변수들을 삭제.
# ls() 함수: list. 변수 목록을 반환.

x <- 1  # 변수 x에 값 1을 저장.
y = 2  # 변수 y에 값 2를 저장.
ls()
rm(x)  # 변수 x를 메모리에서 삭제.

# Global Environment에 있는 모든 변수를 삭제.
rm(list = ls())

?rm  # rm의 설명(help 페이지)를 출력.
?mean


