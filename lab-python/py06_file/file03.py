# 파일 읽기(read): open -> read -> close

with open('test2.txt', mode='rt', encoding='utf-8') as f:
    # mode='rt': read text
    while True:  # 무한 루프
        line = f.readline()  # 파일에서 한줄을 읽음
        if line:  # 읽은 내용이 있다면
            print(line.strip())
            # str.strip(): 문자열 앞뒤에 있는 공백 문자들(' ', '\t', '\n')을 제거.
        else:  # 읽은 내용이 없다면
            break  # 무한 루프 종료

