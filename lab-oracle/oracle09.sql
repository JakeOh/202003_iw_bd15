-- SQL(Structured Query Language)
--- sub query

-- 전체 emp 중에서 평균 이상의 급여를 받는 직원들의 정보
select avg(sal) from emp;
select * from emp where sal >= 2073.2;
select * from emp where sal >= (
    select avg(sal) from emp
);

-- ALLEN 보다 많은 급여를 받는 직원들
select sal from emp where ename = 'ALLEN';
select * from emp where sal > (
    select sal from emp where ename = 'ALLEN'
);

-- ALLEN의 comm보다 더 많은 comm을 받는 직원들
select comm from emp where ename = 'ALLEN';
select * from emp where comm > (
    select comm from emp where ename = 'ALLEN'
);

-- ALLEN과 같은 매니저를 갖는 직원들의 정보
select mgr from emp where ename = 'ALLEN';
select * from emp where mgr = (
    select mgr from emp where ename = 'ALLEN'
);

-- ALLEN의 매니저 정보
select * from emp where empno = (
    select mgr from emp where ename = 'ALLEN'
);

-- 각 부서에서 급여 최솟값을 받는 직원의 정보
select deptno, min(sal)
from emp
group by deptno;

select * from emp where sal in (
    select min(sal) from emp
    group by deptno
);

select * from emp
where (deptno, sal) in (
    select deptno, min(sal) from emp
    group by deptno
);


-- 매니저인 직원들의 정보
select distinct mgr from emp where mgr is not null;
select * from emp
where empno in (
    select distinct mgr from emp 
    where mgr is not null
);

-- 매니저가 아닌 직원들의 정보
select * from emp
where empno not in (
    select distinct mgr from emp 
    where mgr is not null
);
