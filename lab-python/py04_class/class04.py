# 클래스 이름: 대문자 시작. Camel 표기법.
# 변수, 메소드 이름: 전부 소문자. var_name, method_name


class BasicTv:
    """
    TV 가져야할 속성(데이터): 채널, 음량, 전원 상태
    TV 가져야할 기능: 채널 변경, 음량 조절, 전원 on/off, ...
        channel과 volume 변경은 TV power == True인 경우에만.
        channel 변경은 값이 0 ~ 5 사이의 값이 계속 순환되도록.
        volume_down은 최솟값(0)에서 멈출 수 있도록.
        volume_up은 최댓값(5)에서 멈출 수 있도록.
    """
    def __init__(self, power=False, channel=0, volume=0):
        print('Basic TV 생성...')
        self.power = power  # bool (True/False)
        self.channel = channel  # int
        self.volume = volume  # int

    def show(self):
        print(f'TV(power={self.power}, channel={self.channel}, volume={self.volume})')

    def power_on_off(self):
        # TV가 켜져 있으면 TV를 끄고, TV가 꺼져 있으면 TV를 켬.
        if self.power:  # TV가 켜져 있으면
            self.power = False  # TV를 끔
            print('TV OFF')
        else:  # TV가 꺼져 있으면
            self.power = True  # TV를 켬
            print('TV ON')

    def channel_up(self):
        if self.power:  # TV가 켜져 있을 때
            if self.channel < 5:  # 채널 최댓값보다 작을 때
                self.channel += 1  # channel 값 1 증가
            else:  # self.channel >= 5
                self.channel = 0  # 첫번째 채널로 순환
            print('channel:', self.channel)

    def channel_down(self):
        if self.power:
            if self.channel > 0:
                self.channel -= 1  # channel 값 1 감소
            else:  # channel 최솟값(0)일 때
                self.channel = 5  # 가장 마지막 채널로 순환
            print('channel:', self.channel)

    def volume_up(self):
        if self.power:
            if self.volume < 5:
                # volume 값 1 증가
                self.volume += 1
            print('volume:', self.volume)

    def volume_down(self):
        if self.power:
            if self.volume > 0:
                # volume 값 1 감소
                self.volume -= 1
            print('volume:', self.volume)


if __name__ == '__main__':
    tv = BasicTv()
    tv.show()
    tv.power_on_off()

    for _ in range(10):
        tv.channel_up()

    for _ in range(10):
        tv.channel_down()

    for _ in range(10):
        tv.volume_up()

    for _ in range(10):
        tv.volume_down()

    tv.power_on_off()
