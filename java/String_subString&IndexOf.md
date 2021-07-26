## subString()
---
특정 위치의 문자열을 가져오는 메소드
   
<br>

__subString(BeginIndex, endIndex);__

:beginIndex부터 endIndex-1번까지 값 가져오기 

__subString(Index)__

:Index번호부터 다 가져오기


__예시__
```java
String s = "12345678";
```
s.substring(0,8) = 12345678
s.substring(0) = 12345678

<br>
<br>
<br>


## IndexOf()
---
특정 문자의 위치를 찾는 메소드

<br>

__indexOf(String str)__

문자의 값(str)이 있으면 그 위치를 리턴, 없으면 -1을 리턴한다.

<br>

__indexOf(String str, int fromIndex)__

fromIndex 이후에 값이 있으면 위치를 리턴한다.

<br>

__예시__

```java
String s = "12341234";
```
s.indexOf("23"); => 1

:23이라는 숫자가 문자열에서 1번 위치부터 시작하므로 1 리턴

<br>

s.indexOf("23",2) => 5

:문자열에서 2번 위치 이후에 23이 5번에 있으므로 5 리턴

<br>
<br>
<br>
출처

* 인프런 - 코딩테스트 전 꼭 알아야 할 개념과 문제(with 자바)