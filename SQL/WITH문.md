## WITH문

* 오라클 9i R2부터 사용할 수 있는 기능이다.
* 반복되는 서브쿼리에 이름을 부여하여 쉽게 재사용할 수 있도록하는 기능이다.

<BR>

```sql
WITH TEST(서브쿼리 명) AS(
    SELECT *
    FROM 테이블 명
)

SELECT *
FROM TEST
```
다음과 같은 형태로 WITH문을 사용할 수 있다.

WITH문으로 정의한 서브쿼리를 하나의 가상 테이블처럼 사용할 수 있다.

주의할 점은 WITH문은 꼭 ()안에 작성해야 한다.

<BR>

__사용 예시__

문제 : 프로그래머스 - 보호소에서 중성화한 동물

```sql
WITH A AS (
    SELECT * 
    FROM ANIMAL_INS
    WHERE SEX_UPON_INTAKE LIKE 'Intact%'
)
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM A LEFT JOIN ANIMAL_OUTS AS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.SEX_UPON_OUTCOME IN ('Spayed Female','Neutered Male')
```

<BR>

__여러 개의 WITH문 선언하기__

```sql
WITH A(서브쿼리 명) AS(
    SELECT *
    FROM 테이블 명
),
B(서브쿼리 명) AS(
    SELECT *
    FROM 테이블 명
)
SELECT ... (메인 쿼리 작성)
```
여러개의 서브쿼리를 한번에 선언할 수 있다.

WITH는 맨 앞에 한 번만 선언하면 되고 서브쿼리는 , 로 구분하여 작성한다.

