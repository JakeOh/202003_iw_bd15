class Stock:
    def __init__(self, code, price, n):
        self.code = code  # 주식 종목 코드(이름)
        self.price = price  # 주식 가격
        self.n = n  # 주식 수량

    def get_total_price(self):
        return self.price * self.n


class Trade:
    def __init__(self):
        self.stock_list = []

    def buy(self, stock):
        self.stock_list.append(stock)

    def get_stock(self, code):
        my_stocks = [stock.get_total_price()
                    for stock in self.stock_list
                    if code == stock.code]
        total_num = [stock.n for stock in self.stock_list
                     if code == stock.code]
        return sum(my_stocks), sum(total_num)


if __name__ == '__main__':
    trade = Trade()
    trade.buy(Stock('SS', 100, 10))
    trade.buy(Stock('AAPL', 1000, 1))
    trade.buy(Stock('SS', 150, 10))
    trade.buy(Stock('AAPL', 1100, 10))

    print(trade.stock_list)
    print(trade.get_stock('SS'))
    print(trade.get_stock('AAPL'))





