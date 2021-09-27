## Substr

특정 위치의 문자열을 가져온다.

<br>

__1.substr(컬럼명, 시작위치)__

<br>

시작 위치 이후의 문자열을 모두 가져온다.

<br>

__예시__

student 테이블

|name|score|
|------|---|
|thomas|10|
|john|20|
|amily|30|
|inkyeong|20|

```sql
SELECT name, score, substr(name, 3) as rename

FROM student;
```

<br>

__결과__
|name|score|rename|
|------|---|---|
|thomas|10|omas|
|john|20|hn|
|amily|30|ily|
|inkyeong|20|kyeong|

<br>

__2.substr(컬럼명, 시작위치,길이)__

<br>

문자열을 시작위치부터 길이만큼 출력한다.

<br>

__예시__

student 테이블

|name|score|
|------|---|
|thomas|10|
|john|20|
|amily|30|
|inkyeong|20|

```sql
SELECT name, score, substr(name, 3,2) as rename

FROM student;
```

<br>

__결과__
|name|score|rename|
|------|---|---|
|thomas|10|om|
|john|20|hn|
|amily|30|il|
|inkyeong|20|ky|

<br>

<br>

__데이터베이스 별 함수 명__

데이터베이스 별 함수명이 다르므로 주의해야 한다.

<br>

1. MySQL
    
    * substr()
    * substring()
2. Oracle
    * substr()
3. SQL Server
    * substring()

