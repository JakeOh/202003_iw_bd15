class Score:
    def __init__(self, computer=0, science=0, geoscience=0):
        # field(attribute, instance variable) 초기화
        self.computer = computer
        self.science = science
        self.geoscience = geoscience

    def calc_total(self):
        # 세 과목의 총점을 계산해서 리턴하는 함수
        return self.computer + self.science + self.geoscience

    def calc_mean(self):
        # 세 과목의 평균을 계산해서 리턴하는 함수
        return self.calc_total() / 3

    def info(self):
        # Score 내용을 출력
        # print('----- score -----')
        print('computer =', self.computer)
        print('science =', self.science)
        print('geoscience =', self.geoscience)
        print('total =', self.calc_total())
        print('average =', self.calc_mean())
        # print('-' * 20)


class Student:
    # attribute: 이름, 시험점수(class Score)
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # functionality: 학생 정보 출력
    def info(self):
        print('name:', self.name)
        print('computer:', self.score.computer)
        print('science:', self.score.science)
        print('geoscience:', self.score.geoscience)
        print('total:', self.score.calc_total())
        print('average:', self.score.calc_mean())


if __name__ == '__main__':
    # Score 클래스의 인스턴스 생성
    score1 = Score(100, 90, 80)
    print(score1.computer)
    # score의 총점 출력
    total = score1.calc_total()
    print('총점:', total)
    # score의 평균 출력
    average = score1.calc_mean()
    print('평균:', average)
    # score의 전체 정보 출력
    score1.info()

    score2 = Score(99, 77, 15)
    score2.info()

    student1 = Student('오쌤', score2)
    student1.info()

    student2 = Student('이승기', Score(100, 99, 98))
    student2.score.info()
