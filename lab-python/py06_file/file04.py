# 파일 읽기

with open('test2.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        # for 변수 in 파일: 구문을 사용하면,
        # 파일 객체의 readline() 함수를 반복적으로 호출함.
        print(line.strip())
