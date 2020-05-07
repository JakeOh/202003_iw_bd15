# dept테이블에서 부서 번호와 부서 위치를 입력받아서 해당 부서의 위치를 update
# update dept set ??? = ??? where ??? = ???

import cx_Oracle
import py07_database.oracle_config as cfg

# Oracle DB 서버와 접속(connection)
with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn:
    # cursor 객체 생성 <- SQL 문장 실행
    with conn.cursor() as cursor:
        # SQL 문장
        sql = 'update dept2 set loc = :loc where deptno = :deptno'

        # :loc와 :deptno에 값을 binding하기 위해서
        dno = int(input('부서 위치를 옮길 부서의 번호를 입력>>> '))
        dloc = input('옮길 위치를 입력>>> ')

        # SQL 문장 binding & 실행(execute)
        cursor.execute(sql, loc=dloc, deptno=dno)
        # update 후 commit
        conn.commit()

        # update 결과를 select로 확인
        sql_select = 'select * from dept2 order by deptno'
        cursor.execute(sql_select)
        for row in cursor:
            print(row)





