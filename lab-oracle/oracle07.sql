-- 1)
select empno, 
    rpad(trunc(empno, -2) / 100, 4, '*') as empno_maks,
    ename,
    rpad(substr(ename, 1, 1), 5, '*') as enamp_mask
from emp
where length(ename) = 5;

select rpad(substr(to_char(empno), 1, 2), 4, '*')
from emp;

-- 2)
select empno, ename, sal,
    trunc(sal / 21.5, 2) as day_pay,
    round(sal / (21.5 * 8), 1) as time_pay
from emp;

-- 3)
select empno, ename, 
    to_char(hiredate, 'YYYY/MM/DD') as hiredate,
    to_char(next_day(add_months(hiredate, 3), '월'), 'YYYY-MM-DD') as regular,
    to_char(next_day(add_months(hiredate, 3) - 1, '월'), 'YYYY-MM-DD') as regular2
from emp;


-- null value 처리 함수
-- nvl(변수, null을 대체할 값)
-- nvl2(변수, null이 아닐 때 대체할 값, null일 때 대체할 값)
select comm, nvl(comm, 0), nvl2(comm, 'True', 'False')
from emp;

select sal, comm, 
    sal * 12 + nvl(comm, 0) as annual_sal
from emp;


