## Oracle 날짜 변환

형 변환을 통해 날짜를 비교하는 쿼리를 작성할 때 필요한 개념이다.

<br>

__TO_CHAR__

DATETIME 타입을 String 타입으로 변환한다.

```sql
SELECT TO_CHAR(DATETIME,'YYYY-MM-DD') as 날짜
from ANIMAL_INS
```

<br>
<br>


__TO_DATE__

String 타입을 Date 타입으로 변환한다.

```sql
SELECT TO_DATE('20210730', 'YYYY-MM-DD')
FROM dual
```

<br>

__날짜 서식__

TO_DATE('2021-05-08 15:00:00', 'YYYY-MM-DD HH24:MI:SS') 

|||
|------|---|
|YYYY|연도 4자리|
|MM|월|
|DD|일|
|HH|시|
|HH24|시 24시 표시|
|MI|분|
|SS|초|
