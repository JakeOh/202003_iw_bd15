rm(list = ls())

# 리스트(list): 객체들의 집합.
# key(name)-value의 쌍으로 데이터를 저장할 수 있음.

student <- list(no = 1, name = "오쌤", 
                age = 16, gender = "M")
student

# 리스트에서 원소를 접근하는 방법: list$key
student$no
student$name

student2 <- list(2, "홍길동", 20, "F")
student2
student2[[1]]
student2[[2]]

s1 <- student2[[1]]  # [[]]는 값만 리턴.
s2 <- student2[1]  #[]는 리스트(key-value)를 리턴

contact <- list(no = 100,
                name = "오쌤",
                phone = c('010-1111-2222', '02-1234-5678', '02-0000-2222'),
                email = list(office = 'jake@itwill.co.kr',
                             personal = 'jake@gamil.com'))
contact
# contact에서 name값만 출력
contact$name
contact[[2]]
# contact의 전화번호(phone) 중에서 2번째 번호만 출력
contact$phone[2]
# contact$phone[[2]]
# contact에서 office 이메일만 출력
contact$email$office




