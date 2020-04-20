# open -> write -> close
# 열기(open) 이후에 반드시 닫기(close)를 호출해야 하는 객체 - file
# with ... as 구문 -> close() 함수가 자동으로 호출

with open('test.txt', mode='a', encoding='utf-8') as f:
    f.write('append 테스트')
    # f.close() 호출할 필요가 없음 - with as 구문이 자동으로 호출
