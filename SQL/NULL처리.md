## NULL처리 [ Oracle vs MySQL ]

어떤 값이 null인 경우 다른 값을 출력하는 경우에 필요하며 MySQL과 Oracle 각각 차이점이 있다.

<br>

__Oracle__

```sql
SELECT NVL(NAME, 'No name') as NAME
FROM ANIMAL_INS
```
NVL(expr1, expr2)

expr1가 null이면 expr2를 출력한다.

<br>

__MySQL__

```sql
SELECT IFNULL(NAME, 'No name') as NAME 
FROM ANIMAL_INS
```
IFNULL(expr1, expr2)

expr1가 null이면 expr2를 출력한다.

<br>
<br>

__주의__

IFNULL과 NVL를 헷갈리지 않도록 주의해야 한다!