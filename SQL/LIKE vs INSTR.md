## LIKE절

특정 문자가 포함된 레코드를 조회할 때 사용한다.

작성 방법 : __WHERE 컬럼 LIKE (%) 검색 조건 (%)__

```sql
SELECT NAME
FROM STUDENT 
WHERE NAME LIKE 'A%'   // A로 시작하는 이름

WHERE NAME LIKE '%A'   // A로 끝나는 이름

WHERE NAME LIKE '%A%'  // 이름에 A가 포함된 경우

WHERE NAME LIKE 'A_B%' // A_B로 시작하는 이름
                       // _ 자리는 아무거나 상관없음
```
<BR>

문제 해결 : 프로그래머스 __이름에 el이 들어가는 동물 찾기__

[문제 바로가기](https://programmers.co.kr/learn/courses/30/lessons/59047)

```sql
SELECT ANIMAL_ID, NAME 
FROM ANIMAL_INS 
WHERE NAME LIKE '%el%'
```

테이블의 규모가 작고 검색 조건이 간단한 경우는 빠르게 조회가 가능하나 대규모 데이터베이스에서 LIKE절을 사요하면 조회하는데 오래걸린다는 단점이 있다.

이 문제를 해결하기위해 INSTR()을 사용할 것이다.


<BR>
<BR>

## INSTR

문자열에서 특정 문자의 위치를 찾을 때 사용한다.

찾는 문자가 없는 경우 0을 반환한다.

작성 방법 : __INSTR(컬럼, 찾는 문자, 시작 위치,몇 번째 결과를 반환할 것인지)__

```sql
SELECT ANIMAL_ID, NAME 
FROM ANIMAL_INS 
WHERE INSTR(NAME, 'el') > 0
```
찾는 문자가 있는 경우 그 위치 번호를 반환한다.

반환된 숫자가 0보다 큰 문자열에서 찾는 문자가 있다는 뜻이므로 LIKE절과 같은 조회 결과를 낸다.

위와 같은 SQL를 작성하여 속도를 개선할 수 있다.

