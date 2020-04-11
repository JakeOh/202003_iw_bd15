# try-except 구문 활용

while True:  # 무한 루프
    try:
        num = int(input('정수 입력 >>> '))
        print(f'num = {num}')
        break  # 무한 루프 while을 종료
    except ValueError as e:
        print('정수로 입력해 주세요... please...')

print('end of process')