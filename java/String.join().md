## String.join()

* 배열에 있는 문자를 결합하는 방법

* java8에 존재하는 메소드

<br>

__사용법__

String.join(결합할 문자열 사이에 들어갈 문자, 배열)

<br>

```java
String[] Data = {"a", "b", "c", "d"};
String result = String.join("",Data);
```
__결과__

```
abcd
```
<br>

```java
String[] Data = {"a", "b", "c", "d"};
String result = String.join(",",Data);
```
__결과__

```
a,b,c,d
```
","을 추가하여 문자열 사이 ,를 추가할 수 있다.

<br>
<br>
<br>

__기타__

문자열 연결하는 방법 중 StringBuilder도 있음

String.join(), StringBuilder() 중 적절히 사용
