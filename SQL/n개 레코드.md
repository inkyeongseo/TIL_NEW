## n개 레코드 조회

MySQL과 Oracle의 조회 방법이 다르며 문제를 해결하며 차이점을 확인한다.

문제는 프로그래머스 __상위 n개 레코드__ 이다.

[문제 바로가기](https://programmers.co.kr/learn/courses/30/lessons/59405?language=oracle)

<br>

__MySQL__

```sql
SELECT NAME 
FROM ANIMAL_INS 
ORDER BY DATETIME ASC LIMIT 1
```
MySQL은 LIMIT를 사용해 출력할 레코드 개수를 정할 수 있다.

<br>

__Oracle__

```sql
SELECT NAME
FROM (SELECT * FROM ANIMAL_INS ORDER BY DATETIME)
WHERE ROWNUM < 2
```
Oracle은 MySQL과 다르게 ROWNUM를 이용해 출력할 레코드를 정한다.

Oracle에서 ROWNUM을 사용할 때 출력할 서브쿼리를 따로 지정해야하며 아래에 자세한 설명을 작성하겠다.

<br>

__Oracle 사용 시 주의사항__

```sql
SELECT NAME
FROM ANIMAL_INS 
WHERE ROWNUM < 2
ORDER BY DATETIME
```
ROWNUM은 이전의 위치를 기억한다. 

따라서 ORDER BY를 통해 정렬을 하여도 이전의 ROWNUM을 기억하여 원하지 않는 정보가 출력된다.
