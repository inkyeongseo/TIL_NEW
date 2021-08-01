## compareTo()
___

두 개의 값을 비교하여 int값으로 반환해 주는 함수이다.


```java
public int compareTo(){
    return A.compateTo(B);
}

```
A와 B의 값을 비교하여 값을 리턴 것이다
* A와 B가 같으면 0
* A > B 이면 1,
* A < B 이면 -1

<br>
<br>

__split__

특정 문자열을 기준으로 구분하여 배열에 넣는 메소드

<br>

```java
String v1 = "8.5.2.4";
String[] v1Array = v1.split("\\.");
```
위와 같은 경우 구분자 .을 기준으로 하여 배열에 넣는다.

따라서 v1Array[0]은 8,v1Array[1]은 5 이런식으로 들어간다.

<br>
<br>

__비교하는 값의 길이가 짧을 경우__
```java
Integer v1Int = i < v1StrArray.length ? Integer.parseInt(v1StrArray[i]) :0;
```
예를 들어 v1=1이고 v2 = 1.0.1인 경우 자릿수가 맞지 않으므로 빈자리에 0을 집어 넣어야 한다.


<br>

<br><br>

출처

* 인프런 - 코딩테스트 전 꼭 알아야 할 개념과 문제(with 자바)
