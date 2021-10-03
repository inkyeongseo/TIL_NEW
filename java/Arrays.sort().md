## Arrays.sort()

<br>
배열을 정렬하는 방법으로 사용 방법이 헷갈려 새롭게 정리하였음

<br>

```java
int[] array = {7,1,5,3,2};
		
Arrays.sort(array);
```
Arrays.sort()를 사용하여 쉽게 정렬할 수 있다.

배열 타입과 상관없이 똑같은 방법으로 사용이 가능하다.

위의 방법으로 정렬하면 오름차순으로 정렬된다.

<출력결과>
```java
1 2 3 5 7
```

__내림차순으로 정렬__
```java
int[] array = {7,1,5,3,2};
		
Arrays.sort(array,Collections.reverseOrder());
```
<출력결과>
```java
7 5 3 2 1
```
위와 같은 방법으로 내림차순으로 정렬할 수 있다.