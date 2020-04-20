class Account:
    # 은행 계좌: 속성(잔고, 계좌번호) + 기능(입금, 출금, 이체, 정보출력)
    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.balance = balance

    def info(self):
        print('Account No.:', self.account_no)
        print('Balance:', self.balance)

    def deposit(self, amount):
        self.balance += amount
        # print(f'{amount} 입금 성공')
        # return self.balance

    def withdraw(self, amount):
        self.balance -= amount

    def transfer(self, amount, to):
        # 이체 = 내통장 출금 + 다른 통장 입금
        self.withdraw(amount)  # self.balance -= amount
        to.deposit(amount)  # to.balance += amount


if __name__ == '__main__':
    account1 = Account('123-4567', 10000)
    # print(account1)
    account1.info()

    account1.deposit(1000)
    account1.info()

    account1.withdraw(500)
    account1.info()

    account2 = Account('123-7890')
    account2.info()
    account1.transfer(10000, account2)
    account1.info()
    account2.info()

