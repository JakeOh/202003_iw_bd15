import csv
import cx_Oracle
import py07_database.oracle_config as cfg


def to_int(x):
    # '1,048 ' 형태의 문자열을 1048 정수 타입으로 변환 리턴
    x = x.strip().replace(',', '')
    # strip(): 문자열 앞/뒤의 공백들을 제거
    # replace(',', ''): 쉼표를 없앰
    return int(x)


# 파일 열기
with open('서울교통공사_역간거리_20190831.csv', mode='r', encoding='euc-kr') as f:
    # csv.reader 생성
    reader = csv.reader(f)
    # CSV 파일에서 한줄씩 읽으면서 리스트에 append
    records = [rec for rec in reader]
    # 첫번째 줄은 컬럼 이름이므로 데이터에 제외
    # 마지막 줄은 빈 데이터(,,,,)이므로 데이터세 제외
    records = records[1:len(records) - 1]
    # print(records[-1])

    # print(records[0])
    # print(to_int(records[0][4]))

    # records에서 0, 1, 4번 컬럼의 값들을 숫자(int) 타입으로 변환
    for rec in records:
        rec[0] = to_int(rec[0])
        rec[1] = to_int(rec[1])
        rec[4] = to_int(rec[4])

    # 변환된 records 확인
    print(records[0:5])

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn:
    with conn.cursor() as cursor:
        sql = '''
        insert into subway
        values (:no, :line, :s_stn, :e_stn, :dist)
        '''
        for rec in records:
            cursor.execute(sql,
                           no=rec[0], line=rec[1], s_stn=rec[2],
                           e_stn=rec[3], dist=rec[4])
        conn.commit()

