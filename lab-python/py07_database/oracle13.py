import csv
import cx_Oracle
import py07_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn:
    with conn.cursor() as cursor:
        cursor.execute('select * from emp')
        employees = [row for row in cursor]
        col_names = [col[0] for col in cursor.description]

with open('emp2.csv', mode='w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(col_names)
    for emp in employees:
        writer.writerow(emp)
