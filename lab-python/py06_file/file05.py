# csv_exam.csv 파일의 내용을 한줄씩 읽어서 콘솔 출력
# 각 컬럼의 이름(id,class,math,...)은 제외하고 출력
# 2차원 리스트 data를 아래와 같은 모습으로 생성
# [[1,1,50,98,50],
#  [2,1,60,97,60],
#  ...]

data = []  # empty 리스트
with open('csv_exam.csv', mode='r', encoding='utf-8') as f:
    f.readline()
    # 파일의 첫번째 줄이 컬럼 이름이므로, 읽은 후 아무 동작도 하지 않음.
    for line in f:
        # print(line.strip())
        # 각 줄의 내용을 쉼표(,)를 구분자로 해서 5개의 원소를 갖는 리스트로 만듦.
        row = line.strip().split(',')
        # print(row)
        # 1차원 리스트를 data에 append
        data.append(row)

print(data)

# 3번째 컬럼(컬럼 인덱스 = 2)이 수학(math) 점수.
# 수학 점수로만 이루어진 1차원 리스트를 생성
# 수학 점수의 총점, 평균을 계산, 출력
length = len(data)  # 20
math = [int(data[x][2]) for x in range(length)]
print(math)
print('수학 총점:', sum(math))
print('수학 평균:', sum(math) / length)

# class가 1인 학생들의 수학 점수를 찾아서 총점, 평균, 최솟값, 최댓값
math1 = [int(data[i][2]) for i in range(length)
         if data[i][1] == '1']
print(math1)
print('1반 수학 총점:', sum(math1))
print('1반 수학 평균:', sum(math1) / len(math1))
print('1반 수학 최솟값:', min(math1))
print('1반 수학 최댓값:', max(math1))

