-- emp 테이블을 복사해서 emp2를 생성
create table emp2
as select * from emp;
-- create table ~ as select 구문은 데이터는 복사하지만,
-- 제약조건까지 생성하지는 않는다.

select * from emp2;

-- dept 테이블을 복사해서 dept2를 생성
create table dept2
as select * from dept;

-- salgrade 테이블을 복사해서 salgrade2를 생성
create table salgrade2
as select * from salgrade;

select * from dept2;

-- dept2 테이블에 새로운 레코드 insert
insert into dept2 (deptno, dname, loc)
values (50, 'Oracle', 'Seoul');

-- 테이블의 모든 컬럼에 insert하는 경우 컬럼 이름 생략 가능.
insert into dept2 
values (60, 'SQL', 'Jeju');

-- 컬럼의 순서와 values에서 값들의 순서가 같아야 함.
insert into dept2 (dname, loc, deptno)
values ('Database', 'Dokdo', 70);

select * from dept2;

-- emp2 테이블에 새로운 레코드 insert
insert into emp2
values(8001, 'test1', 'CLERK', 7839, 
        to_date('2020-04-24', 'YYYY-MM-DD'),
        4500, null, 50);

insert into emp2
values(8002, 'test2', 'CLERK', 7839, 
        to_date('2019-04-24', 'YYYY-MM-DD'),
        1500, null, 50);

insert into emp2
values(8004, 'test4', 'CLERK', 7839, 
        to_date('1992-04-24', 'YYYY-MM-DD'),
        3000, null, 60);

insert into emp2
values(8005, 'test5', 'CLERK', 7839, 
        to_date('1999-04-24', 'YYYY-MM-DD'),
        3500, null, 60);
        
insert into emp2
values(8006, 'test6', 'CLERK', 7839, 
        to_date('2010-04-24', 'YYYY-MM-DD'),
        2000, null, 70);
        
insert into emp2
values(8007, 'test7', 'CLERK', 7839, 
        to_date('2010-04-24', 'YYYY-MM-DD'),
        2800, null, 70);
        
select * from emp2;

-- 20번 부서에서 근무하는 사원들의 평균 급여
select avg(sal) from emp2
group by deptno
having deptno = 20;

select avg(sal) from emp2
where deptno = 20;

-- 부서번호 update
update emp2
set deptno = 70
where sal > (
    select avg(sal) from emp2 where deptno = 20
);

select * from emp2 order by deptno desc;

-- 10번 부서의 사원 중 가장 늦은 입사일
-- max(date_type): 가장 늦은 날짜, min(date_type): 가장 빠른 날짜
select max(hiredate) from emp2 where deptno = 70;

-- 급여를 10% 인상하고, 부서를 70번으로 이동
update emp2
set sal = sal * 1.1, deptno = 70
where hiredate > (
    select max(hiredate) from emp2 where deptno = 10
);

commit;

-- 급여 등급이 5인 사원들의 사번
select e.empno, s.grade
from emp2 e, salgrade2 s
where e.sal between s.losal and s.hisal
    and s.grade = 5;
    
select e.empno, s.grade
from emp2 e inner join salgrade2 s
    on e.sal between s.losal and s.hisal
where s.grade = 5;

-- 급여 등급이 5인 사원들 삭제
delete from emp2
where empno in (
    select e.empno
    from emp2 e inner join salgrade2 s
        on e.sal between s.losal and s.hisal
    where s.grade = 5
);

select * from emp2 order by sal desc;

-- 바로 직전의 commit 상태로 되돌림.
rollback;

select * from emp2 order by sal desc;

delete from emp2
where sal between 
            (select losal from salgrade2 where grade = 5)
        and 
            (select hisal from salgrade2 where grade = 5);

commit;


