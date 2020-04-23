-- 다중행 함수(multi-row function, group function):
-- 여러 행을 입력받아서 값 하나를 리턴하는 함수. 
-- e.g. 평균, 합계, 최솟값, 최댓값, 표준편차
select sum(sal) as 합계,
        round(avg(sal), 2) as 평균,
        min(sal) as 최솟값,
        max(sal) as 최댓값,
        round(variance(sal), 2) as 분산,
        round(stddev(sal), 2) as 표준편차
from emp;

-- 단일행 함수: 행 별로 함수가 값을 리턴
select trunc(sal, -2) from emp;


-- count(): 레코드 개수를 리턴
select count(*) from emp;  -- 테이블의 row 개수
select count(empno) from emp;
select count(mgr), count(comm) from emp;  -- 컬럼에서 null이 아닌 row의 개수

-- (주의) 다중행 함수와 변수(컬럼) 혹은 단일행 함수를 함께 select할 수 없다!
select empno, count(empno) from emp;  -- ORA-00937 에러 발생

-- 날짜 타입의 컬럼(변수)는 min, max를 사용할 수 있음
-- 크기 비교 가능, 정렬 가능
select min(hiredate), max(hiredate)
from emp;

-- 10번 부서 사원들의 급여의 최솟값, 최댓값, 평균, 표준편차를 출력
select 10 as DEPTNO,
    min(sal) as MIN,
    max(sal) as MAX,
    round(avg(sal), 1) as AVG,
    round(stddev(sal), 1) as STD_DEV
from emp
where deptno = 10;

-- 집합 연산: 합집합, 교집합, 차집합
select 10 as DETPNO, avg(sal) from emp where deptno = 10
union
select 20 as DETPNO, avg(sal) from emp where deptno = 20
union
select 30 as DETPNO, avg(sal) from emp where deptno = 30;

-- 부서별 급여 평균
select deptno, round(avg(sal), 1) as AVG_SAL
from emp
group by deptno
order by deptno;

-- JOB별 SAL의 평균과 사원수
select job, 
    round(avg(sal), 1) as AVG_SAL,
    count(job) as COUNT
from emp
group by job;

-- 부서별 급여 평균, 급여 평균이 2000 이상인 경우를 출력
select deptno, round(avg(sal), 1)
from emp
group by deptno
having avg(sal) >= 2000
order by deptno;

-- JOB별 급여 평균과 사원수, 급여 평균이 2000 이상인 경우만 출력
select job,
    round(avg(sal), 1) as AVG_SAL,
    count(job) as COUNT
from emp
group by job
having avg(sal) >= 2000;

-- JOB별 SAL의 평균과 사원수, JOB별 사원수가 3명 이상인 JOB에 대해서,
select job,
    round(avg(sal), 1) as AVG_SAL,
    count(job) as COUNT
from emp
group by job
having count(job) >= 3;

-- deptno별, job별 평균 급여
select deptno, job, avg(sal)
from emp
group by deptno, job;

select deptno, job, avg(sal)
from emp
group by job, deptno
order by job;

-- 부서번호, 부서별 평균 급여, 부서별 급여 최솟값, 최댓값, 사원수 출력
-- 부서번호 오름차순으로 출력. 소숫점 한자리까지 출력
select deptno,
    round(avg(sal), 1) as AVG_SAL,
    min(sal) as MIN_SAL,
    max(sal) as MAX_SAL,
    count(deptno) as COUNT
from emp
group by deptno
order by deptno;

-- 같은 JOB을 같는 사원수가 3명 이상인 JOB에 대해서, JOB별 사원수 출력
select job, count(job) as CNT
from emp
group by job
having count(job) >= 3;
-- select에서 사용한 별명(alias)를 group by 또는 having 절에서 사용할 수 없음!
-- group by 또는 having 절에서는 별명(alias)을 정의할 수 없음

-- 입사 연도별 급여 평균, 급여 최솟값, 최댓값을 출력.
-- 입사 연도는 YYYY 형식으로 출력.
select to_char(hiredate, 'YYYY') as HIREDATE,
    round(avg(sal), 1) as AVG_SAL,
    min(sal) as MIN_SAL,
    max(sal) as MAX_SAL
from emp
group by to_char(hiredate, 'YYYY')
order by HIREDATE;

-- 입사 연도별, 부서별 몇 명이 입사했는지 출력.
select to_char(hiredate, 'YYYY') as YEAR,
    deptno,
    count(*) as COUNT
from emp
group by to_char(hiredate, 'YYYY'), deptno
order by YEAR;

-- comm을 받는 직원수와 받지 않는 직원수를 출력(comm=0도 comm을 받는 직원으로 생각)
select nvl2(comm, 'O', 'X') as COMM,
    count(nvl2(comm, 'O', 'X')) as COUNT
from emp
group by nvl2(comm, 'O', 'X');


-- 오라클의 그룹 함수들은 기본적으로 null 값을 제외하고 계산함.
select avg(comm), avg(nvl(comm, 0))
from emp;

-- 매니저(mgr)별 평균 급여
select mgr, avg(sal)
from emp
where mgr is not null
group by mgr
order by mgr;
