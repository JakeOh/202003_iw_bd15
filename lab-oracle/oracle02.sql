-- Alt + F10: SQL 워크시트 새로 만들기
-- 조건을 만족하는 레코드 추출
-- select 컬럼, ... from 테이블 where 조건;

-- 10번 부서에서 일하는 직원들의 모든 정보
select * from emp where deptno = 10;

-- sal >= 2500인 직원들의 모든 정보
select * from emp where sal >= 2500;

-- sal이 1500 이상 3000 이하인 직원들의 모든 정보
-- and, or, not 키워드 사용
select * from emp
where sal >= 1500 and sal <= 3000;

select * from emp
where sal between 1500 and 3000;

-- 10 또는 20번 부서에서 근무하는 직원들의
-- 사번, 이름, 직책, 부서 번호를 검색
select empno, ename, job, deptno
from emp
where deptno = 10 or deptno = 20;

select empno, ename, job, deptno
from emp
where deptno in (10, 20);

-- 30번 부서가 아닌 직원들의 사번, 이름, 직책, 부서번호 검색
select empno, ename, job, deptno
from emp
where deptno != 30;

-- job이 'SALESMAN'인 직원들의 모든 정보
select * from emp where job = 'SALESMAN';
-- 테이블에 저장된 문자열 값들은 대/소문자를 구분함!

-- job이 'SALES'로 시작하는 직원들의 모든 정보
select * from emp where job like 'SALES%';

-- 이름이 'A'로 시작하는 직원들의 사번, 이름 출력
select empno, ename from emp 
where ename like 'A%';

-- 이름이 'S'로 끝나는 직원들의 사번, 이름 출력
select empno, ename from emp
where ename like '%S';

-- job이 'MAN'을 포함하는 직원들의 사번, 이름, 직책을 출력
select empno, ename, job
from emp
where job like '%MAN%';

select * from emp
where job like '_LERK';  -- 4개의 레코드가 검색됨


select * from emp
where job like '_ERK';  -- 0개의 레코드가 검색됨
-- _는 해당 위치의 1글자가 어떤 글자여도 된다는 의미.

-- comm 변수의 값이 null인 직원들의 모든 정보
select * from emp where comm is null;

-- comm 변수의 값이 null이 아닌 직원들의 모든 정보
select * from emp where comm is not null;

-- 수당(comm)이 있고, 급여가 1500 이상인 직원들의
-- 사번, 이름, 직책, 급여, 수당, 총급여(급여+수당)을 출력
select empno, ename, job, sal, comm, sal + comm as total_sal
from emp
where comm is not null and sal >= 1500;

-- 수당을 받지 않는 직원들 중 급여가 1500 초과인 직원들의
-- 사번, 이름, 급여, 부서번호를 출력
select empno, ename, sal, deptno
from emp
where comm is null and sal > 1500;

-- 20번, 30번 부서에서 근무하는 직원들 중 급여가 2000을 초과하는
-- 직원들의 사번, 이름, 급여, 부서번호를 출력
select empno, ename, sal, deptno
from emp
where deptno in (20, 30) and sal > 2000;

-- 수당(comm)이 없고, 매니저는 있고, 직책이 'MANAGER' 또는 'CLERK'인
-- 직원들의 모든 정보를 출력
select *
from emp
where comm is null
    and mgr is not null
    and job in ('MANAGER', 'CLERK');


-- scott 계정이 가지고 있는 테이블 이름들 확인
select table_name from user_tables;

-- 테이블의 구조 확인
desc emp;
