texts = '''2020-04-01\tAAA\t1200
2020-04-01\tABAB\t100
2020-04-02\tAAA\t1500
2020-04-02\tABAB\t200'''
# print(texts)

with open('prices.tsv', mode='w', encoding='utf-8') as f:
    f.write(texts)

# prices.tsv 파일을 오픈해서 한줄씩 읽으면서,
# 탭('\t')으로 구분된 데이터들의 (2차원) 리스트를 작성
prices = []
with open('prices.tsv', mode='r', encoding='utf-8') as f:
    for line in f:
        # print(line)
        row = line.strip().split('\t')
        prices.append(row)
print(prices)


class Product:
    def __init__(self, date, code, price):
        self.date = date  # 문자열(str)
        self.code = code  # 문자열(str)
        self.price = price  # 정수(int)

    def __repr__(self):
        return f'Product(date={self.date}, code={self.code}, price={self.price})'


p = Product('2020-04-17', 'ABC', 10000)  # 인스턴스 생성
print(p)

# prices.tsv 파일을 읽기 모드로 열어서,
# 각각의 라인에 있는 데이터들을 Product 타입의 인스턴스로 변환한 후
# 1차원 리스트에 저장
products = []
with open('prices.tsv', mode='r', encoding='utf-8') as f:
    for line in f:  # 파일에서 한줄씩 읽기를 반복하면서
        data = line.strip().split('\t')  # 탭으로 구분된 문자열 리스트
        proudct = Product(data[0],  # date
                          data[1],  # code
                          int(data[2]))  # price
        products.append(proudct)
print(products)


# def test(x):
#     print(x)
#     return x.price


# products 리스트를 price 내림차순으로 정렬해서 출력
products.sort(key=lambda x: x.price, reverse=True)
print(products)

