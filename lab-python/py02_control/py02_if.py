import random   # random 모듈의 기능을 사용

# random.random(): 0 <= r < 1 난수
# random.randint(a, b): a <= r <= b을 만족하는 정수 난수
# print(random.randint(1, 3))

# 1: 가위, 2: 바위, 3: 보
rps = {1: '가위', 2: '바위', 3: '보'}

computer = random.randint(1, 3)
print(f'컴퓨터({computer}) = {rps[computer]}')

print('=== 가위/바위/보 게임 ===')
print('[1] 가위')
print('[2] 바위')
print('[3] 보')
print('선택 >>>')
# 사용자가 입력한 숫자를 저장
user = int(input())
print(f'유저({user}) = {rps[user]}')

# if-elif-else를 이용해서 computer:user의 승패 결과를 출력
if user == 1:  # user=가위
    if computer == 1:  # com=가위
        print('Tie')
    elif computer == 2:  # com=바위
        print('You Lose ㅠ.ㅠ')
    else:  # com=보
        print('You won ^___^')
elif user == 2:  # user=바위
    if computer == 1:  # com=가위
        print('You won ^___^')
    elif computer == 2:  # com=바위
        print('Tie')
    else:  # com=보
        print('You lose ㅠ.ㅠ')
else:  # user=보
    if computer == 1:  # com=가위
        print('You lose ㅠ.ㅠ')
    elif computer == 2:  # com=바위
        print('You won ^___^')
    else:  # com=보
        print('Tie')


if user == computer:  # 비긴 경우(가:가, 바:바, 보:보)
    print('Tie')
else:  # 승패가 있는 경우
    if user == 1:  # user=가위
        if computer == 2:  # com=바위
            pass
        else:  # com=보
            pass
    elif user == 2:  # user=바위
        if computer == 1:  # com=가위
            pass
        else:  # com=보
            pass
    else:  # user=보
        if computer == 1:  # com=가위
            pass
        else:  # com=바위
            pass


# 논리 연산자(boolean operator): and, or, not
# 비트 연산자(bitwise operator): &, |, ^
if user == 1 and computer == 1:
    pass
elif user == 1 and computer == 2:
    pass
# TODO: 나머지 7가지 경우 추가...

score = user - computer
if score == 0:  # 비긴 경우
    pass
elif score == 1 or score == -2:  # user win
    pass
else:  # computer win
    pass
