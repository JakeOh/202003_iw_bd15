class HamburgerStore:
    # 모든 햄버거 가게들이 공유할 변수
    burgers = {"basic": 1000, "cheese": 1500}

    def __init__(self, money):
        self.money = money  # 햄버거 가게의 현금 보유


class Customer:
    def __init__(self, money):
        self.money = money  # 고객이 보유하고 있는 현금

    def order(self, store, burger):
        self.money -= burger  # 고객의 현금에서 버거 금액을 뺌
        store.money += burger  # 가게의 현금에 버거 금액을 더함

    def __repr__(self):
        return f'{self.money}원 소유'


if __name__ == '__main__':
    # 햄버거 가게 생성
    mcdonald = HamburgerStore(0)

    # 고객 생성
    cust1 = Customer(10000)
    print('cust1 =', cust1)

    cust2 = Customer(10000)
    print('cust2 =', cust2)

    cust1.order(mcdonald, HamburgerStore.burgers['basic'])
    print('cust1 =', cust1)
    print('mcdonald =', mcdonald.money)

    cust2.order(mcdonald, HamburgerStore.burgers['cheese'])
    print('cust2 =', cust2)
    print('mcdonald =', mcdonald.money)
