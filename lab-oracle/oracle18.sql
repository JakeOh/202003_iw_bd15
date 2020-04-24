-- delete, truncate, drop
select * from emp_copy;

delete from emp_copy;
-- delete는 DML의 한 종류 --> commit 전에는 rollback을 할 수 있음.
rollback;

truncate table emp_copy;
rollback;
-- truncate는 DDL의 한 종류 
-- --> DDL은 자동 commit이 되기 때문에 rollback을 할 수 없음!
select * from emp_copy;  -- 테이블 자체는 남아 있는 상태

drop table emp_copy;
-- drop은 DDL의 한 종류 --> rollback 불가
select * from emp_copy;  -- 에러
