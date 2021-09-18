## 순위 함수

<br>

1.RANK

중복 값은 동일 순위 부여, 중복 순위 다음 값은 앞에 중복된 값을 개수 이후 순위 부여

<br>

__예시__

student 테이블

|name|score|
|------|---|
|a|10|
|b|20|
|c|30|
|d|20|

```sql
SELECT RANK() OVER (ORDER BY score DESC) rank_no, name, score

FROM student;
```

__결과__

|rank_no|name|score|
|------|---|---|
|1|c|30|
|2|b|20|
|2|d|20|
|4|a|10|


<br>

1.DENSE_RANK

중복 값은 동일 순위 부여, 중복 순위 다음 값은 앞에 중복된 값을 개수 상관없이 다음 순위 부여

<br>

__예시__

student 테이블

|name|score|
|------|---|
|a|10|
|b|20|
|c|30|
|d|20|

```sql
SELECT DENSE_RANK() OVER (ORDER BY score DESC) rank_no, name, score

FROM student;
```

__결과__

|rank_no|name|score|
|------|---|---|
|1|c|30|
|2|b|20|
|2|d|20|
|3|a|10|

<br>

1.ROW_NUMBER

중복 값은 동일 순위 부여하지 않고 순차적으로 순위 부여

<br>

__예시__

student 테이블

|name|score|
|------|---|
|a|10|
|b|20|
|c|30|
|d|20|

```sql
SELECT ROW_NUMBER() OVER (ORDER BY score DESC) rank_no, name, score

FROM student;
```

__결과__

|rank_no|name|score|
|------|---|---|
|1|c|30|
|2|b|20|
|3|d|20|
|4|a|10|

<br>

