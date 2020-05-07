import csv

import cx_Oracle
import py07_database.oracle_config as cfg


def to_int(num_str):
    try:
        # int 타입으로 변환할 때 에러가 발생하지 않으면, 숫자(int)를 리턴
        return int(num_str)
    except:
        # int 타입으로 변환 시도하다가 에러가 발생한 경우에는 None을 리턴
        return None


# 파일 읽기 모드 열기(open)
with open('서울도서관 새로 들어온 도서정보.csv',
          mode='r', encoding='cp949') as f:
    # cp949 인코딩: 한글 Windows의 텍스트 파일 기본 인코딩(MS949)
    # csv 파일을 읽기 위해서 reader 객체 생성
    reader = csv.reader(f)
    # csv 파일의 내용을 한줄씩 읽으면서 리스트에 데이터를 append
    records = [line for line in reader]
    # 리스트에서 앞에서 3번째까지 데이터를 출력
    print(records[:3])
    # 리스트에서 마지막 3개의 데이터를 출력
    print(records[-3:])

    # records의 첫번째 데이터는 컬럼 이름이므로 제외
    records = records[1:]

    # records에서 발행년도 컬럼의 값들을 int로 변환
    for rec in records:
        rec[3] = to_int(rec[3])
    print(records[:5])

# Oracle DB 연결
with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn:
    # cursor 객체 생성
    with conn.cursor() as cursor:
        sql = '''insert into books
        values (:title, :author, :publisher, :pub_year, :book_type, :library, 
            to_date(:reg_date, 'YYYYMMDD'))
        '''
        # records의 각 행마다 insert 문장을 실행
        for rec in records:
            cursor.execute(sql,
                           title=rec[0], author=rec[1],
                           publisher=rec[2], pub_year=rec[3],
                           book_type=rec[4], library=rec[5],
                           reg_date=rec[6])
        # 모든 행을 insert 성공하면 DB에 영구적으로 반영(commit)
        conn.commit()

        # books 테이블에서 2020년 1월에 새로 등록된 책들의 제목, 저자, 등록일을 검색, 출력
        sql_select = """
        select title, author, reg_date
        from books
        where reg_date between to_date('2020/01/01', 'YYYY/MM/DD')
                and to_date('2020/01/31', 'YYYY/MM/DD')
        """
        cursor.execute(sql_select)
        for row in cursor:
            print(row)








