# txt 파일 쓰기(write)

# 1) 파일 열기(open)
# open(file, mode, encoding, ...)
#   file: 파일 이름(경로)
#   mode: r(읽기, 기본값), w(쓰기), a(추가), t(텍스트, 기본값), b(이진)
#   encoding: 기본값은 OS의 기본 인코딩(e.g. 한글 Windows인 경우 euc-kr)
f = open('test.txt', mode='w', encoding='utf-8')

# 2) 파일에 컨텐트 쓰기(write)
# write() 함수의 리턴값의 의미는 파일에 쓴 글자 수
# write() 함수는 줄바꿈(new line, '\n')을 자동으로 추가하지 않음!
result = f.write('hello\n')
print('write result =', result)
result = f.write('안녕하세요!')
print('write result =', result)

# 3) 파일 닫기(close)
f.close()

# test2.txt 파일에 10개 라인을 write
# Line 1
# Line 2
# ...
# Line 10
f = open('test2.txt', mode='wt', encoding='utf-8')
for i in range(1, 11):
    f.write(f'Line {i}: hello\n')
f.close()


