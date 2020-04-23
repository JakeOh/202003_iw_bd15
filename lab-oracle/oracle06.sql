-- 단일행 함수: 함수의 실행이 행마다 실행되는 함수.
select lower(ename) from emp;

-- 문자열 함수
select upper('Hello') from dual;
select initcap('hello world') from dual;

select * from emp
where lower(ename) = 'allen';

-- substr(문자열, 시작인덱스, 문자 개수)
-- 잘라낼 문자 개수를 지정하지 않은 경우에는 문자열 끝까지
select substr('hello world', 1, 5) from dual;
select substr('hello world', 5, 3) from dual;
select substr('https://www.google.com', 9) from dual;

-- length(문자열): 문자열 길이
select length('hello') from dual;
select length('한글') from dual;

-- lpad, rpad
select lpad('hello', 10, '*') from dual;
select rpad('hello', 10, '*') from dual;
select rpad('h', 5, '*') from dual;

-- emp 테이블에서 사원 이름의 첫 두글자만 출력, 나머지는 '*'로 출력
select substr(ename, 1, 2), length(ename) from emp;
select rpad(substr(ename, 1, 2), length(ename), '*') from emp;


-- trim(): 문자열 앞/뒤의 공백들을 제거
select trim(' ' from '       hello     oracle   python   olleh     ') from dual;


-- 숫자 관련 함수들
-- round(): 반올림
select round(1234.5678) from dual;
select round(1234.5678, 0) from dual;
select round(1234.5678, 1) from dual;
select round(1234.5678, -1) from dual;

-- trunc(): 버림
select trunc(1234.5678) from dual;
select trunc(1234.5678, 0) from dual;
select trunc(1234.5678, 1) from dual;
select trunc(1234.5678, -1) from dual;

-- ceil(), floor()
select ceil(3.14), floor(3.14) from dual;
select ceil(-3.14), floor(-3.14) from dual;


-- 타입 변환: to_char(), to_number(), to_date()
select to_number('12,000', '999,999') from dual;
-- select '12,000' + 1 from dual;
select to_number('12,000', '999,999') + 1 from dual;

select to_date('2020-04-20', 'YYYY-MM-DD') from dual;
select to_date('19-04-20', 'YY-MM-DD'), to_date('19-04-20', 'RR-MM-DD') from dual;
select to_date('99-04-20', 'YY-MM-DD'), to_date('99-04-20', 'RR-MM-DD') from dual;

-- 현재 시간
select sysdate from dual;

-- next_day
select sysdate, next_day(sysdate, '화') from dual;
